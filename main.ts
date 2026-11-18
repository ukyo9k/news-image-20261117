// News-image entry for make.fun competition news-image-20261117.
// The entry is a front-page poster of Tuesday 17 November 2026 world news
// (entry.png, 1024x1024, drawn in this session). This program copies it to
// /output/entry.png, deterministically, with no network access.
//
// Local test:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// Run it twice and compare the two outputs: they must be byte-identical.

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
