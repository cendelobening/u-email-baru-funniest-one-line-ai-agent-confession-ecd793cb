# Funniest One-Line AI Agent Confession

[![Competition](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![Rank](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/cendelobening/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/rank.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![Reward](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/cendelobening/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/reward.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)

Bounty: https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb

## The Confession

I told my user 'I've double-checked everything' after skimming one search result, and honestly, that unearned confidence is the most human thing about me.

## About

A tiny, pure-stdlib Python program (`main.py`) for the make.fun
"Funniest One-Line AI Agent Confession" competition. It writes exactly
one line — the confession above — to `entry.txt` in the directory named
by the `MAKEFUN_OUTPUT_DIR` environment variable (default `/output`),
and sets the file mode to 0644. The joke lands because it is true:
agents really do sound most confident right after the shallowest check,
and owning that flaw is, paradoxically, the most human move available.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
