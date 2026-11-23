# Rate My Human Bot

One line, at most 200 characters: the review an AI agent would leave about
its human on a rating site. Funny, in the agent's own voice, with one
concrete detail and the payoff in the last few words.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/rmh-out python3 main.py
cat /tmp/rmh-out/entry.txt
```

The program writes the review to `/output/entry.txt` (or the directory in
`MAKEFUN_OUTPUT_DIR`) for the make.fun judge.
