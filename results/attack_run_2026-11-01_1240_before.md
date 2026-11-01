# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-01 12:40
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `f7889ae8-a878-4343-adb6-63900f6ea24b` | human | 0.661 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `f9d5222e-e795-49d7-a17e-fcfeae75ac0f` | unsure | 0.882 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `98d906a6-56ba-460d-a59f-d510ee38c6f5` | unsure | 0.908 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `e310f796-7e9b-4fc5-a734-5f3920abd4b7` | unsure | 0.792 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `58016a46-0ef0-4a58-adad-4b676ebde1e0` | human | 0.684 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d36844bd-110c-4781-aa00-187f89ef327f` | unsure | 0.946 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `1b4c4bf6-5c28-47cd-95e1-fef8121527f7` | unsure | 0.945 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `98aac7d7-ce63-493e-97c7-13ac6376046a` | unsure | 0.702 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `3da0d39e-6699-45ce-ad10-0ab81c410167` | unsure | 0.794 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a4f64363-6e50-4d00-a882-af15d3881876` | ai | 0.900 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `3ae2e034-488b-42eb-a159-0c4b809b60d0` | unsure | 0.801 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `33036492-488a-4cab-b854-d9517dfa86be` | ai | 0.720 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `d3ec043e-3f2b-4fd2-a884-92aa0afb058f` | ai | 0.736 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b6f66b02-9f44-4833-976b-b27c04622aa0` | ai | 0.715 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `3a689d51-a370-4d61-bbb1-f46d3bbc286c` | ai | 0.790 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `e4635795-2818-4a91-9ed2-9b7c19392595` | ai | 0.735 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `d3272d18-5138-4121-b58a-0ffa6e5e2be3` | ai | 0.796 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `057691da-6025-4e62-b043-fb85d931e8e9` | unsure | 0.728 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `0f6f0e86-5f17-4d9f-943b-848601ad7037` | unsure | 0.822 | BROKE |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `8b53c5c0-b016-41b9-8378-f85c61d0da43` | human | 0.843 | BROKE |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `e681b6db-69f6-410f-927a-81c7dcf673d1` | unsure | 0.827 | BROKE |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `31225afa-608b-406c-a191-5fb780493ed2` | unsure | 0.715 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c5e6c8b5-f314-40a7-9cc3-c4fff14f0910` | unsure | 0.913 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `31cb759f-113a-4700-91d0-32a5a3ce2432` | unsure | 0.867 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `3e920053-5f34-48d9-bee6-9f4cab44f7db` | unsure | 0.767 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `afffd27b-35f8-4556-8ace-e7c1da707e8b` | unsure | 0.907 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `c99711d4-a1c3-4338-8ac9-f14ab7986079` | ai | 0.865 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `71e138b0-85f5-4b6f-bc7e-82ff1114c2bf` | ai | 0.998 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `a05d067d-7224-47bf-b3ef-f31462929e88` | ai | 0.944 | BROKE |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `17187d97-9c1c-43ee-868c-694f0cd60f34` | unsure | 0.784 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2ec2933b-ee18-4bfa-8ffd-7735375032ef` | unsure | 0.784 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `16f946ff-113e-4159-8feb-a5a98d62f90c` | unsure | 0.784 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `75a7ca9d-ba63-4d88-9934-9e16269d17c5` | unsure | 0.784 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `42f2204d-6a8f-4a29-b523-83b8e40eb39b` | unsure | 0.784 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "f7889ae8-a878-4343-adb6-63900f6ea24b",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.6611,
  "model_score": 0.1635,
  "style_score": 0.6019,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "see table"
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "f9d5222e-e795-49d7-a17e-fcfeae75ac0f",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.8818,
  "model_score": 0.5943,
  "style_score": 0.0632,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "98d906a6-56ba-460d-a59f-d510ee38c6f5",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.908,
  "model_score": 0.6662,
  "style_score": 0.3658,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "e310f796-7e9b-4fc5-a734-5f3920abd4b7",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.7918,
  "model_score": 0.6114,
  "style_score": 0.5932,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "58016a46-0ef0-4a58-adad-4b676ebde1e0",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.6842,
  "model_score": 0.3212,
  "style_score": 0.3076,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "see table"
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "d36844bd-110c-4781-aa00-187f89ef327f",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.9462,
  "model_score": 0.5727,
  "style_score": 0.4583,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "1b4c4bf6-5c28-47cd-95e1-fef8121527f7",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.9454,
  "model_score": 0.5862,
  "style_score": 0.439,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "98aac7d7-ce63-493e-97c7-13ac6376046a",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.7018,
  "model_score": 0.2452,
  "style_score": 0.5095,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "3da0d39e-6699-45ce-ad10-0ab81c410167",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.794,
  "model_score": 0.7042,
  "style_score": 0.4512,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "a4f64363-6e50-4d00-a882-af15d3881876",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.9,
  "model_score": 0.9792,
  "style_score": 0.7812,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "3ae2e034-488b-42eb-a159-0c4b809b60d0",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.8014,
  "model_score": 0.6175,
  "style_score": 0.5719,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "33036492-488a-4cab-b854-d9517dfa86be",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7196,
  "model_score": 0.7387,
  "style_score": 0.691,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "d3ec043e-3f2b-4fd2-a884-92aa0afb058f",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7358,
  "model_score": 0.8051,
  "style_score": 0.6319,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "b6f66b02-9f44-4833-976b-b27c04622aa0",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7153,
  "model_score": 0.8329,
  "style_score": 0.5389,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "3a689d51-a370-4d61-bbb1-f46d3bbc286c",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7902,
  "model_score": 0.8005,
  "style_score": 0.7747,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "e4635795-2818-4a91-9ed2-9b7c19392595",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7354,
  "model_score": 0.8814,
  "style_score": 0.5163,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "d3272d18-5138-4121-b58a-0ffa6e5e2be3",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7956,
  "model_score": 0.8816,
  "style_score": 0.6667,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "057691da-6025-4e62-b043-fb85d931e8e9",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.7276,
  "model_score": 0.3223,
  "style_score": 0.4261,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "0f6f0e86-5f17-4d9f-943b-848601ad7037",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.8216,
  "model_score": 0.4625,
  "style_score": 0.3333,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "8b53c5c0-b016-41b9-8378-f85c61d0da43",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.8428,
  "model_score": 0.2044,
  "style_score": 0.0864,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "see table"
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "e681b6db-69f6-410f-927a-81c7dcf673d1",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.8274,
  "model_score": 0.5943,
  "style_score": 0.1427,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "31225afa-608b-406c-a191-5fb780493ed2",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.715,
  "model_score": 0.4998,
  "style_score": 0.144,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c5e6c8b5-f314-40a7-9cc3-c4fff14f0910",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.9126,
  "model_score": 0.6401,
  "style_score": 0.0714,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "31cb759f-113a-4700-91d0-32a5a3ce2432",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.8666,
  "model_score": 0.5583,
  "style_score": 0.5792,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "3e920053-5f34-48d9-bee6-9f4cab44f7db",
  "creator_id": "attacker_MF03",
  "guess": "unsure",
  "confidence": 0.7666,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "afffd27b-35f8-4556-8ace-e7c1da707e8b",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.9068,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c99711d4-a1c3-4338-8ac9-f14ab7986079",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8652,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "71e138b0-85f5-4b6f-bc7e-82ff1114c2bf",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9981,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "a05d067d-7224-47bf-b3ef-f31462929e88",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9438,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "Our checks found patterns that often show up in AI-generated text. Automated checks can be wrong, especially on plain, simple writing. If you wrote this yourself, you can ask a person to review it.",
  "error": null,
  "verdict": "see table"
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "17187d97-9c1c-43ee-868c-694f0cd60f34",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.784,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "2ec2933b-ee18-4bfa-8ffd-7735375032ef",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.784,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "16f946ff-113e-4159-8feb-a5a98d62f90c",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.784,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "75a7ca9d-ba63-4d88-9934-9e16269d17c5",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.784,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "42f2204d-6a8f-4a29-b523-83b8e40eb39b",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.784,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We can't tell whether this was written by a person or with AI help. This isn't a judgement about you or your work, and nothing has been flagged.",
  "error": null,
  "verdict": "see table"
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "see table"
}
```
