# Tuesday 17 November 2026 — World News in One Image

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ukyo9k/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ukyo9k/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Built for the [make.fun](https://make.fun) bounty [“Sum up 17 November's world news in one image”](https://make.fun/bounty/news-image-20261117) ($250 in USDC). Referral: https://make.fun/r/1gefbfp1

A front-page poster summing up the world's news of **Tuesday 17 November
2026**, built for the make.fun bounty `news-image-20261117`.

## The image

`entry.png` (1024×1024, PNG) is a newspaper front page: a masthead naming
the day and story count, a hero photograph of the burning gas tanker in
the Strait of Hormuz, three top stories with small schematic panels, a
six-story grid, and a compact "Also on Tuesday 17 November" list — 22
stories across 6 continents. All text is drawn programmatically (PIL +
DejaVu fonts) so every headline is crisp and legible; the hero photograph
carries no text of its own. The build script is `build_poster.py`.

`main.ts` (Node 22, standard library only) copies `entry.png` to
`/output/entry.png`. It uses no network and is fully deterministic — run it
twice and the outputs are byte-identical.

## The 22 stories (all verified against sources opened on 18 Nov 2026)

Hero: **U.S. strikes Iran** — U.S. warplanes hit a missile site on Qeshm
Island; the gas tanker *Tara Gas* burned in the Strait of Hormuz and Oman
evacuated 24 seafarers. Source: Reuters (via Profile News roundup,
17 Nov 2026).

Top stories:
1. **Crimean Bridge road span falls into the sea** — second Ukrainian
   strike in two days; Zelensky hails an "unprecedented operation".
   Source: Reuters.
2. **Iran sends drones at a US radar in Bahrain** — Bahrain and the US say
   all were downed; US jets then strike Qeshm. Source: Reuters.
3. **Trump holds first Quad summit in Manila** — four unveil
   critical-minerals deals; Putin heads to Shenzhen for talks with Trump
   and Xi. Sources: AP / Reuters.

Grid:
4. **Ebola cases pass 11,000 in DR Congo** — WHO: about 5,400 dead; cases
   doubled in three months. Source: WHO / UN News, 17 Nov 2026.
5. **COP31 split over fossil fuels** — nations weigh the draft; EU urges a
   clean-energy signal. Source: Reuters, 17 Nov 2026.
6. **US loses measles-free status** — PAHO ends the designation held since
   2000 after a year of uninterrupted transmission. Source: PAHO.
7. **Nvidia tops forecasts again** — record quarterly revenue after the
   bell; shares rise about 4%. Sources: Reuters, AP.
8. **Gaza truce at risk, UN told** — Board of Peace warns the ceasefire
   could fail; winter rains flood shelters. Sources: AP, UN News,
   17 Nov 2026.
9. **Mongolia leader says he will quit** — Khurelsukh denies a $25m bribe
   claim over a railway deal; parliament must accept it. Sources: AP,
   AFP, 17 Nov 2026.

Also on Tuesday 17 November:
10. **Serbia** — Student List sworn in, 140 of 250 seats in Belgrade.
11. **Bangladesh** — police tear-gas garment workers as wage talks stall.
12. **An-12 crash** — all 19 aboard killed in Siberia.
13. **Mozambique** — Mondlane on trial over 2024 unrest; faces 24 years.
14. **Moldova** — airspace shut as Russian drones fly over the capital.
15. **Japan** — jets scrambled as Russian planes near Fukuoka.
16. **Prague** — two trains collide; 46 hurt, four seriously.
17. **Quake** — M6.6 off Indonesia felt in Darwin; no tsunami.
18. **Yemen** — Houthis advance toward Aden.
19. **Depardieu** — admits sex-assault charge in Paris.
20. **Apple** — iCloud and App Store outage.
21. **Israel** — Eisenkot ally elected Knesset speaker.

Sources for 10–21: Reuters, AP, AFP, UN News, national reporting, all
dated 17 Nov 2026.

## License

MIT — see `LICENSE`.
