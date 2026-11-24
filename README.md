# Tuesday 24 November 2026 — World News in One Image

[![make.fun bounty](https://make.fun/badge/news-image-20261124.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/adhityanaufal26/news-image-20261124/rank.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/adhityanaufal26/news-image-20261124/reward.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![license: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A newspaper front page for **Tuesday 24 November 2026**, compiled at 02:45 UTC.
Because Tuesday was only hours old, every story is labelled by the day it
happened (TUE / MON / SUN) so nothing is misdated.

Stories shown:

- **Huang is back at Nvidia (Mon)** — the board unanimously reinstates Jensen
  Huang as CEO 11 days after his resignation; shares soar 31% in a day.
- **Russian jets set off island alert (Tue)** — military planes enter South
  Korea's air defence zone near Ulleung Island; jets scrambled, a shelter
  warning sounds at 07:52 and is lifted three minutes later; no airspace breach.
- **COP31 collapses (Sun, Antalya)** — the longest climate talks ever end with
  no deal after the final text omits fossil fuels; Pacific nations voice despair.
- **Ukraine sinks Russian corvette (Sun–Mon, Benghazi)** — maritime drones sink
  the *Merkury* in Benghazi port; the war reaches the Mediterranean.
- **Gaza strikes kill 3 (Mon–Tue)** — including a UN aid worker; Australia,
  Canada, Italy and the UK jointly demand unrestricted humanitarian access.
- **Singer flogged 74 times (Mon, Iran)** — an Iranian singer and four crew get
  74 lashes each; the US sanctions 24 targets in Iran's shadow-banking network.
- **Official sentenced to death (Tue, China)** — a state official is sentenced
  to death for leaking state secrets; 100 reports, 35 of them secret.
- **Drug lord 'Chapo Isidro' captured (Mon, Mexico)** — elite soldiers seize
  Fausto Isidro Meza Flores with US intelligence help.
- **Gold jumps to $3,670; Bitcoin tops $63,000 (Tue)** — safe-haven gold surges
  nearly 4% as the AI trade wobbles; Bitcoin bounces back above $63,000.
- Briefs: NATO to send AWACS jets to Poland (Mon), Murmansk governor detained
  on embezzlement charges (Tue), North Korea mulls closing its Swiss office
  (Tue), Trump halts Army detonation of a toxic stockpile in Iowa (Mon),
  Chicago O'Hare ground stop amid the Thanksgiving rush (Mon), US seeks $1.1bn
  in crypto from the North Korea-linked Binance hack (Mon), Oracle secures
  funding for its $300bn OpenAI computing deal (Mon) — plus a DATE CHECK box.

## Run

```bash
python3 main.py                        # copies entry.png to /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py # copies entry.png to out/entry.png
```

`build_image.py` regenerates `entry.png` (1024×1024) deterministically with
Pillow — fixed layout and fonts, no randomness, no network:

```bash
python3 build_image.py
```

## License

MIT — see [LICENSE](LICENSE).
