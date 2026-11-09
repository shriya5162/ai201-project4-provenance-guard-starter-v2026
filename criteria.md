# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives on human writing

Of 10 pieces of human writing (5 I wrote myself and 5 written plainly: short
sentences, everyday vocabulary, the way a second-language writer or a student
might write), **at most 1** is labeled high-confidence AI, on every one of the
three trials.

**Why this target:**

On a writing site, a wrong accusation costs the writer far more than a missed
detection costs the site, so this is the error I hold tightest. I included
plain writing on purpose: both of my signals read common words in even
sentences as AI-like, so these are the writers most likely to be accused. A
target tested only on my own prose would be too easy.

---

## 2. Score spread between clear cases

Across 5 clearly AI-generated texts and 5 clearly human texts, the **average
combined score of the AI texts is at least 0.30 higher** than the average of
the human texts, and **no clearly-AI text scores below any clearly-human
text**, on every trial.

**Why this target:**

If the clear cases don't separate, no choice of thresholds can make the labels
mean anything, and the uncertain cases have no chance. 0.30 is the width of
the default unsure band (0.35–0.65). A smaller gap means clear AI and clear
human text could land on either side of the same band. The no-overlap rule
stops one extreme pair from hiding a muddled middle in the average.

---

## 3. Every label is reachable, and borderline text lands in the middle

On a 15-input test set (5 clearly human, 5 clearly AI, and 5 borderline: AI
text I've lightly edited by hand), **each of the three labels is produced at
least twice**, and **at least 3 of the 5 borderline inputs are labeled
unsure**, on every trial.

**Why this target:**

A label no input can reach is a gap in my ranges, and the config notes that a
weighted average can get stuck in the middle of the scale. "Reachable once"
could be a fluke of one input, so I ask for twice. Lightly edited AI is the
case where saying "we're not sure" is the honest answer, so most of it should
land there and not in a confident verdict either way.

---

## 4. The appeal path

For 5 appeals on real `content_id`s, **5 of 5** return 200, and each appealed
item has an `under_review` entry in the log after its original decision, with
the original decision still in place. For 3 appeals on made-up ids, **3 of 3**
return 404 and add no `under_review` entry.

**Why this target:**

The appeal is the only thing standing between a wrong accusation and nothing,
so "most of the time" isn't good enough. One silent failure is a writer who
thinks they've been heard and hasn't. The made-up-id half checks the failure
the brief warns about: a typo that fails silently and looks like success.

---

## 5. Bad input never crashes the service

Of 6 malformed `/submit` requests (no `text`, empty `text`, whitespace-only
`text`, a one-word `text`, 50,000 characters of text, and a body that isn't a
JSON object), **6 of 6** get a 4xx response with an `error` code, **0** get a
500, and **6 of 6** leave a `rejected` entry in the audit log.

**Why this target:**

A crash on malformed input is one of the most common real failures, and next
unit's attack set will send exactly these. It has to be all six, because one
500 means someone can knock the service over on purpose. Logging the
rejections matters because an attack that shows up only as an absence can
never be found afterwards.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 9 — the extension (Shape A: deploy and instrument)

Five more criteria, about the timing and logging I added in unit 9 and the
run path in RUNNING.md. The unit 7 criteria above are unchanged.

Each is tested in three trials, with the service restarted before each trial.
I wrote these after Milestone 3's cost measurement (warm requests 280–515 ms
over 10 runs; cold starts of 18 s, 23 s, 57 s and 91 s across four sessions),
and before running any test against them.

---

## 6. Every request leaves a timed record

Of 12 requests covering every path (a scored submission; a missing-text 400;
an empty-text 400; a too-short 400; a too-long 413; a non-object-body 400; a
rate-limited 429; an accepted appeal; and appeals answered 400, 404 and 409;
plus one simulated crash 500), **12 of 12** add exactly one new entry to
`logs/audit.jsonl` that has `endpoint`, `http_status` and a numeric
`duration_ms`, and whose `http_status` matches what the caller received, in
every trial.

**Why this target:**

The whole extension is "the log answers how long, and for what, without new
code." One request that leaves no entry, or leaves two, means the log can't be
trusted to count anything, so anything less than all 12 is a miss. The 12
cover every branch in the route, because refusals and crashes are where a
missing record hides an attack.

---

## 7. Warm requests stay fast

After one warm-up request, **at least 19 of 20** submissions of 350–450
characters have a logged `duration_ms` **under 500 ms**, in every trial.

**Why this target:**

My 10-run measurement averaged 337 ms, but one run took 515 ms, so 500 ms is
not a target I already clear every time. A writer waiting more than half a
second after pressing submit starts to notice. 19 of 20 allows one slow
outlier without letting a slow tail hide behind a good average.

---

## 8. A cold start finishes within a minute

After restarting the service, the first submission returns **200 within
60 seconds**, and its log entry has `cold_start: true`, in **3 of 3**
restarts.

**Why this target:**

Every restart makes the next writer wait for GPT-2 to load. I've measured that
wait at 18 s, 23 s, 57 s and 91 s, so 60 s is a real line. A minute is about
as long as someone will look at a spinner before assuming the page is broken.
`cold_start: true` has to be there too, or the log can't tell a slow cold start
from a slow warm request.

---

## 9. When the model can't load, the service says so quickly and leaves a record

With the detector pointed at a model that doesn't exist
(`AI201_DETECTOR_MODEL=no-such-model`), **5 of 5** submissions get a **503**
JSON response (not an HTML error page) **within 10 seconds each**, and **5 of
5** leave a `rejected` entry with `reason: detector_unavailable` and a
`duration_ms`, in every trial.

**Why this target:**

This is the bad path. The service retries the load on every request, and a
missing model means a network lookup that could hang, so this might fail
slowly, not quickly. 10 seconds is the longest a caller should wait to be told
"not right now." Every failure has to be logged, or an outage looks like a
quiet afternoon.

---

## 10. Appeals stay fast as the log grows

With **at least 2,000 entries** in `logs/audit.jsonl`, **5 of 5** accepted
appeals have a logged `duration_ms` **under 100 ms**, in every trial.

**Why this target:**

My instrumentation showed that an appeal takes about 40 ms with 230 log
entries, because `/appeal` re-reads the whole log on every call. If that time
grows with the log, a real site would cross 100 ms within weeks. 2,000 entries
is about ten times today's log. 100 ms is where an appeal would start to feel
slower than a submission's refusal (2–4 ms) for no reason the writer can see.
