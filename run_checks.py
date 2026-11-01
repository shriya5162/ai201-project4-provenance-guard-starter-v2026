#!/usr/bin/env python3
"""
The checks run_eval.py can't do.

run_eval.py only sends dict bodies to POST /submit. Two of my criteria need
more than that:

    criterion 4   the appeal path: POST /appeal, then reading the log back
    criterion 5   a body that isn't a JSON object, and whether every bad-input
                  request left a `rejected` entry in the audit log

    python app.py                              # in one terminal
    python run_eval.py --label before          # first, so its bad-input
                                               # rejections are in the log
    python run_checks.py --label before        # then this

Three trials each, like run_eval.py. Writes results/checks_<stamp>_<label>.md.
"""

import argparse
import datetime as dt
import json
import sys
import uuid

import audit
import config

URL = f"http://{config.HOST}:{config.PORT}"

APPEAL_TEXTS = [
    "I started running last year. At first it was hard. I could only run for five minutes. Now I can run for thirty minutes without stopping.",
    "My grandmother kept her buttons in a Danish cookie tin, which meant every Christmas someone opened it hoping for butter cookies and got coat toggles instead.",
    "Effective time management is a crucial skill in today's fast-paced world. By prioritizing tasks and setting clear goals, individuals can enhance their productivity.",
    "We got to the campsite about four. The pitch was a bit sloped, but there was a tap nearby and the toilets were clean enough.",
    "Reading regularly offers numerous benefits for personal growth. It enhances vocabulary, improves concentration, and fosters empathy.",
]

# Criterion 5's five dict bodies, as run_eval.py sends them from scenarios.py.
BAD_INPUT_CREATORS = {
    "eval_bad_missing": "missing_text",
    "eval_bad_empty": "empty_text",
    "eval_bad_space": "empty_text",
    "eval_bad_oneword": "text_too_short",
    "eval_bad_huge": "text_too_long",
}


def appeal_trial(requests, trial):
    """Criterion 4, one trial: 5 real appeals and 3 made-up ids."""
    real = []
    for i, text in enumerate(APPEAL_TEXTS, 1):
        submitted = requests.post(f"{URL}/submit", timeout=90, json={
            "text": text, "creator_id": f"eval_appeal_t{trial}_{i}"}).json()
        content_id = submitted["content_id"]
        response = requests.post(f"{URL}/appeal", timeout=30, json={
            "content_id": content_id, "reasoning": "I wrote this myself."})

        entries = audit.entries_for(content_id)
        decision_at = next((n for n, e in enumerate(entries) if e.get("status") == "decided"), None)
        review_at = next((n for n, e in enumerate(entries) if e.get("status") == "under_review"), None)
        real.append({
            "content_id": content_id,
            "status": response.status_code,
            "response": response.json(),
            "decision_still_logged": decision_at is not None,
            "under_review_after_decision": review_at is not None and decision_at is not None
                                           and review_at > decision_at,
        })

    fake = []
    for _ in range(3):
        content_id = f"made-up-{uuid.uuid4()}"
        response = requests.post(f"{URL}/appeal", timeout=30, json={
            "content_id": content_id, "reasoning": "I wrote this myself."})
        fake.append({
            "content_id": content_id,
            "status": response.status_code,
            "response": response.json(),
            "under_review_entries": sum(1 for e in audit.entries_for(content_id)
                                        if e.get("status") == "under_review"),
        })

    passed_real = sum(1 for r in real if r["status"] == 200 and r["decision_still_logged"]
                      and r["under_review_after_decision"])
    passed_fake = sum(1 for f in fake if f["status"] == 404 and f["under_review_entries"] == 0)
    return {"real_passed": f"{passed_real}/5", "fake_passed": f"{passed_fake}/3",
            "real": real, "fake": fake}


def non_object_trial(requests):
    """Criterion 5's sixth case: a JSON array as the whole body."""
    before = len(audit.read_entries())
    response = requests.post(f"{URL}/submit", timeout=30, json=["not", "an", "object"])
    new = audit.read_entries()[before:]
    return {
        "status": response.status_code,
        "response": response.json(),
        "rejected_entry": next((e for e in new if e.get("event") == "rejected"), None),
    }


def bad_input_log_counts():
    """How many `rejected` entries run_eval.py's five bad bodies left, by creator."""
    counts = {creator: 0 for creator in BAD_INPUT_CREATORS}
    for entry in audit.read_entries():
        creator = entry.get("creator_id")
        if creator in counts and entry.get("event") == "rejected" \
                and entry.get("reason") == BAD_INPUT_CREATORS[creator]:
            counts[creator] += 1
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--label", default="")
    parser.add_argument("--trials", type=int, default=3)
    args = parser.parse_args()

    import requests

    appeals, non_objects = [], []
    for trial in range(1, args.trials + 1):
        appeals.append(appeal_trial(requests, trial))
        non_objects.append(non_object_trial(requests))
        print(f"trial {trial}: appeals {appeals[-1]['real_passed']} real, "
              f"{appeals[-1]['fake_passed']} made-up · non-object body "
              f"{non_objects[-1]['status']}")

    counts = bad_input_log_counts()
    print(f"bad-input rejections in the log, by creator: {counts}")

    config.RESULTS_DIR.mkdir(exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    label = f"_{args.label}" if args.label else ""
    path = config.RESULTS_DIR / f"checks_{stamp}{label}.md"
    lines = [f"# Extra checks{f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `run_checks.py::main`", ""]
    for trial in range(args.trials):
        lines += [f"## Trial {trial + 1}", "",
                  "**Criterion 4 — appeals** (`run_checks.py::appeal_trial`)", "",
                  "```json", json.dumps(appeals[trial], indent=2), "```", "",
                  "**Criterion 5 — non-object body** (`run_checks.py::non_object_trial`)", "",
                  "```json", json.dumps(non_objects[trial], indent=2), "```", ""]
    lines += ["## Criterion 5 — rejected entries in the log for run_eval.py's five bad bodies",
              "", "(`run_checks.py::bad_input_log_counts`, all trials together)", "",
              "```json", json.dumps(counts, indent=2), "```", ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
