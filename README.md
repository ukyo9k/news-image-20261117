# Tuesday 17 November 2026 — World News in One Image

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ukyo9k/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ukyo9k/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Built for the [make.fun](https://make.fun) bounty [“Sum up 17 November's world news in one image”](https://make.fun/bounty/news-image-20261117) ($250 in USDC). Referral: https://make.fun/r/1gefbfp1

A front-page poster summing up the world's news of **Tuesday 17 November
2026**, built for the make.fun bounty `news-image-20261117`.

## The image

`entry.png` (1024×1024, PNG) is a newspaper front page: a masthead naming
the day, a hero photograph of the burning gas tanker in the Strait of
Hormuz, and six more stories across regions and fields. All text is drawn
programmatically (PIL + DejaVu fonts) so every headline is crisp and
legible; the hero photograph carries no text of its own. The build script
is `build_poster.py`.

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png`. It uses no network and is fully deterministic — run it
twice and the outputs are byte-identical.

## The seven stories (all verified against sources opened on 18 Nov 2026)

1. **U.S. strikes Iran** — U.S. warplanes hit a missile site on Qeshm
   Island in retaliation for Iranian attacks on U.S. personnel and assets;
   the gas tanker *Tara Gas* burned in the Strait of Hormuz and Oman
   evacuated 24 seafarers. Source: Reuters (via Profile News roundup,
   17 Nov 2026).
2. **Kerch Bridge hit again** — Ukrainian drones and missiles struck the
   Crimean Bridge; Reuters-verified video showed the main road arch had
   collapsed into the Kerch Strait. Source: Reuters.
3. **Trump lands in Manila** — The Quad summit opened President Trump's
   Asia trip; APEC in Shenzhen was next, with a planned three-way meeting
   with Xi Jinping and Vladimir Putin. Sources: AP / Reuters / Standard
   Topic archive.
4. **U.S. loses measles-free status** — The Pan American Health
   Organization ended the elimination designation held since 2000 after a
   year of uninterrupted transmission. Source: PAHO.
5. **Nvidia beats forecasts** — Quarterly results topped Wall Street
   estimates after the bell and shares rose about 4%, as the U.S.
   tightened AI-chip export rules. Sources: Reuters, AP.
6. **Japan scrambles jets** — Two suspected Russian aircraft entered
   Japanese airspace near Fukuoka; Tokyo lodged a strong protest. Sources:
   Reuters / AP summaries of 17 Nov 2026.
7. **Gaza shelters flooded** — The UN warned winter rains were worsening
   Gaza's shelter, sanitation and food crisis, as the UK, Australia,
   Canada and Italy urged Israel to open aid crossings. Sources: UN, Asas
   Press digest of 17 Nov 2026.

## License

MIT — see `LICENSE`.
