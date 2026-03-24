# nba-clv-dashboard — flagship: sports ML evaluation

[![CI](https://github.com/ianalloway/nba-clv-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/ianalloway/nba-clv-dashboard/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Employer-facing narrative:** This is my **top public repo** for sports-shaped ML: it shows how I communicate **calibration**, **rolling accuracy**, and **CLV-style** eval—not just a headline metric. Pair it with **[nba-ratings](https://github.com/ianalloway/nba-ratings)** (Elo / logistic / Kelly primitives on PyPI as `nba-edge`) and **[line-shop-cli](https://github.com/ianalloway/line-shop-cli)** for odds normalization + optional Kelly.

**One-pager for recruiters:** [Sports ML evaluation case study](https://ianalloway.xyz/papers/sports-ml-evaluation-case-study.html) (open → Print → Save as PDF).

---

**Problem:** Hiring teams see “68% accuracy” everywhere — they rarely see **calibration**, **rolling stability**, and **closing-line language** in one glance.

**Solution:** **FastAPI** serves `/api/metrics` (**demo JSON** today) and a **single-page Chart.js** view: calibration scatter, rolling accuracy, CLV summary block.

```bash
pip install -e .
uvicorn nba_clv_dashboard.app:app --reload --port 8765
# open http://127.0.0.1:8765
```

## Swap your metrics

Replace `demo_metrics.demo_payload()` with a loader from your parquet / eval pipeline. Keep the same JSON shape or adjust `static/index.html`.

## Non-goals

- **Not** a sportsbook integration — **evaluation honesty demo** only.
- **No** auth / multi-tenant — add if you deploy publicly.

## CI

pytest hits `/api/metrics` with httpx.

## Suggested GitHub topics

`fastapi` · `nba` · `calibration` · `sports-analytics` · `chartjs`

## Screenshot

_Add a browser screenshot of the two charts + KPI row._

## License

MIT
