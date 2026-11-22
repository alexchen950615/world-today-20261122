# World Today — 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/alexchen950615/world-today-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/alexchen950615/world-today-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image that sums up 22 November 2026's world news — a newspaper-style
front page with the six stories that defined the day.

## The six stories

1. **Brazil town clears rubble after deadly storm** — "We lost everything":
   residents pick through the wreckage after a fierce storm.
2. **Nvidia faces US accounting probe amid deepening turmoil** — regulators
   open an accounting inquiry as pressure mounts on the chip giant.
3. **Pentagon moves to restrict US-Canada defence ties** — Washington
   tightens military cooperation with its northern neighbour.
4. **Trump vows to cap credit card interest at 10%** — the president says
   he will work with Democrats to limit card interest rates.
5. **6.7-magnitude quake hits Peru** — a strong tremor shakes the country;
   no deaths reported so far.
6. **Houthis launch revenge strikes on Saudi capital** — missiles target
   Riyadh as regional tensions flare again.

Headlines verified against real 22 November 2026 reporting
(AFP / AP / Reuters via The Manila Times).

## Run it

```bash
python3 main.py
# writes /output/entry.png (1024x1024)
```

Requires Pillow (`pip install Pillow`). If Pillow is unavailable, `main.py`
does not crash: it copies the bundled `entry.png` shipped in this
repository to the output path instead, so a valid image is always produced.

## Files

- `main.py` — generates the image with Pillow (pure code, no assets)
- `entry.png` — the generated 1024×1024 image, also the fallback copy
- `README.md` — this file
- `LICENSE` — MIT

Built for the [make.fun bounty news-image-20261122](https://make.fun/bounty/news-image-20261122).
