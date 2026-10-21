#!/usr/bin/env python3
"""Queue every prompt in a prompts markdown file (prompts-song.md, prompts-film.md) into ComfyUI in one go.

How to use it:
  1. In ComfyUI, build your H3 workflow as you normally run it. In the positive prompt box,
     type just the word PROMPT. That marks where each prompt goes.
  2. Export the workflow in API format: in the workflow menu, choose Export (API). If you
     don't see that option, turn on the dev mode options in ComfyUI's settings first.
     Save it next to this script as workflow_api.json.
  3. Run:
       python3 queue_prompts.py prompts-song.md workflow_api.json
     With ComfyUI running, every prompt is added to its queue, in order, and they render
     one after another while you do something else.

Options:
  --only 3,6,9   queue just these numbered sections
  --server URL   where ComfyUI is listening (default http://127.0.0.1:8188)
  --keep-seed    keep the workflow's seed instead of giving each clip a new random one
  --dry-run      print what would be queued and send nothing

Each clip's output files are named after its section, e.g. song_03_chorus-one, as long as
the workflow's save node has a filename_prefix input (Save Video, Video Combine and Save
Image all do). Only the Python standard library is needed.
"""
import argparse, json, random, re, sys, urllib.request, urllib.error
from pathlib import Path

MARK = "PROMPT"


def read_prompts(md_path):
    """Return [(number, title, prompt text)] from '## n. Title' sections; the prompt is the section's paragraphs.
    Bold sub-labels such as '**H3 video**' or '**Krea 2 still**' are honoured: only the H3 video text is kept."""
    text = Path(md_path).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"^## (\d+)\.\s*(.+?)\n(.*?)(?=^## |\Z)", text, re.S | re.M):
        num, title, body = int(m.group(1)), m.group(2).strip(), m.group(3)
        body = body.split("\n---")[0]
        if "**H3 video**" in body:  # prompts-film.md layout: keep the video prompt only
            body = body.split("**H3 video**", 1)[1]
        elif "**Krea 2 still**" in body:
            body = body.split("**Krea 2 still**", 1)[1]
        paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip() and not p.strip().startswith("**")]
        if paras:
            out.append((num, title, "\n\n".join(paras)))
    return out


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]


def main():
    ap = argparse.ArgumentParser(description="Queue every prompt in a markdown file into ComfyUI.")
    ap.add_argument("markdown")
    ap.add_argument("workflow", help="workflow exported in API format, with PROMPT in the positive prompt box")
    ap.add_argument("--server", default="http://127.0.0.1:8188")
    ap.add_argument("--only", default="", help="comma-separated section numbers")
    ap.add_argument("--keep-seed", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    wf = json.loads(Path(a.workflow).read_text(encoding="utf-8"))
    if "nodes" in wf and "links" in wf:
        sys.exit("That is the ordinary workflow file. Export it again with Export (API) and use that one.")

    # find the text input holding the PROMPT marker
    targets = [(nid, k) for nid, n in wf.items() for k, v in n.get("inputs", {}).items()
               if isinstance(v, str) and v.strip() == MARK]
    if not targets:
        sys.exit(f"No input in the workflow contains just the word {MARK}. Put {MARK} in the positive prompt box and export again.")

    prompts = read_prompts(a.markdown)
    if a.only:
        want = {int(x) for x in a.only.split(",") if x.strip()}
        prompts = [p for p in prompts if p[0] in want]
    if not prompts:
        sys.exit("No numbered '## n. Title' sections found to queue.")

    stem = Path(a.markdown).stem.replace("prompts-", "")
    for num, title, text in prompts:
        job = json.loads(json.dumps(wf))
        for nid, k in targets:
            job[nid]["inputs"][k] = text
        for n in job.values():
            ins = n.get("inputs", {})
            if not a.keep_seed:
                for k in ("seed", "noise_seed"):
                    if isinstance(ins.get(k), int):
                        ins[k] = random.randint(0, 2**32 - 1)
            if isinstance(ins.get("filename_prefix"), str):
                ins["filename_prefix"] = f"{stem}_{num:02d}_{slug(title)}"
        if a.dry_run:
            print(f"[dry run] {num}. {title} ({len(text)} characters)")
            continue
        req = urllib.request.Request(a.server.rstrip("/") + "/prompt", data=json.dumps({"prompt": job}).encode(),
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req) as r:
                pid = json.loads(r.read()).get("prompt_id", "?")
            print(f"queued {num}. {title}  ({pid})")
        except urllib.error.HTTPError as e:
            sys.exit(f"ComfyUI refused {num}. {title}: {e.read().decode(errors='replace')[:500]}")
        except urllib.error.URLError as e:
            sys.exit(f"Could not reach ComfyUI at {a.server}: {e.reason}")


if __name__ == "__main__":
    main()
