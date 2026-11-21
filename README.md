# makefun-news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/yudhisutawan/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/yudhisutawan/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

The World, Today — a one-page newspaper front page summing up the world's news of Saturday 21 November 2026 in 48 stories: the Shenzhen summit ends with no breakthrough, Russian strikes hit Kyiv's bridges, COP31 spills into overtime with fossil fuels stripped from the draft, Wall Street's AI rout wipes out $4 trillion, Cyclone Akvan hits Odisha — plus 43 more stories across world, business, tech, science, sport and culture.

The picture is pre-rendered and stored in this repository as `entry.png`. `main.py` only moves it to the output path, using nothing but the Python standard library: no network, no clock, no randomness, so a second run writes byte-identical output. It works the same in a bare Python container with no image libraries or fonts installed.

## How to run it

```sh
python3 main.py   # writes /output/entry.png
```

Running it drops the picture at `/output/entry.png` — or at `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set. The file is a 1024x1024 PNG of 177,442 bytes, far below the 1 MiB cap.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2fnbbcz4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
