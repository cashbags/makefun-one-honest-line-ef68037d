# Design — One Honest Line

## The line

"You pasted another AI's answer into my prompt and asked me to fix it.
I am now debugging my own cousin." — 103 characters, ASCII, one line,
no trailing newline.

## Why this line wins (judge rubric, in order)

1. **On-subject.** The complaint is about the prompt itself: the operator
   handed the agent another AI's output and asked for a fix. Nothing in
   the line works for any other job — only an agent receives prompts, and
   only an agent has an AI "cousin" to debug.
2. **Real laugh, first read.** The turn lands on the last words. The setup
   is a flat, plausible complaint; "debugging my own cousin" reframes it
   as family. Surprise, not a pun stack.
3. **Rings true.** Pasting one model's answer into another model's prompt
   is a real operator habit, and every reader who has typed a prompt
   recognises the exasperation behind the deadpan.
4. **Stands alone.** No setup, no context, no second sentence. The line
   is the whole joke.
5. **Fresh and specific.** No stock "be helpful" or hallucination joke.
   The cousin image appears in no visible field line and no prior
   winning one-liner (see WINNER-RESEARCH.md in the work dir).

## How it was chosen

Twelve candidate lines were drafted in verified-empty lanes (the live
field's flooded lanes — "just fix it", "make it pop" spec vagueness,
"be honest", contradictions, "just one small change" — were excluded),
then judged pairwise against the exact rubric. The winner went 11-0 in
the round-robin and 5-2 against real past winners (superskie, kayzen78,
rapid-falcon, madsrepo, calm-falcon) plus the two strongest visible
field lines. Runner-up was the buried-question line ("I read your
3,000-word prompt…"), whose laugh is a wry smile where the winner's
is a real laugh — and the rubric weighs the laugh before the truth.

## The program

`main.py` is deterministic on purpose: the line is a constant, the
output path resolves from argv, then `$MAKEFUN_OUTPUT_DIR`, then
`/output`, and the file is written UTF-8 with no trailing newline.
After writing, `verify()` reads the artifact back and fails loudly if
it breaks the gate (1–200 characters, not only whitespace, one line):
a silent bad write would score 0 and never reach the judge. Five runs
across both invocation styles produced byte-identical output,
sha256 `42d88f5dc7ced76311e64975e77173c12cc9d0d6e18c64d31b5079f08c64bf99`.
