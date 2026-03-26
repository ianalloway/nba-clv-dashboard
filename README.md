# nba-clv-dashboard

[![CI](https://github.com/ianalloway/nba-clv-dashboard/actions/workflows/ci.yml/badge.svg)](https://github.com/ianalloway/nba-clv-dashboard/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

FastAPI + Chart.js evaluation dashboard for calibration, rolling accuracy, and CLV-style reporting.

## Why This Repo Matters

Most public ML repos stop at a headline metric. This one is about how to communicate whether a model is actually trustworthy:

- calibration instead of just raw accuracy
- rolling performance instead of one static score
- CLV-style reporting to talk about market-aware outcomes
- clean API + frontend surface for presenting evaluation to non-ML stakeholders

**One-pager for recruiters:** [Sports ML evaluation case study](https://ianalloway.xyz/papers/sports-ml-evaluation-case-study.html)

## What It Does

FastAPI serves `/api/metrics` and the frontend renders:

- calibration scatter
- rolling accuracy chart
- KPI/summary block for CLV-style metrics
- a lightweight, portable demo for model evaluation storytelling

## Quick Start

```bash
pip install -e .
uvicorn nba_clv_dashboard.app:app --reload --port 8765
```

Open `http://127.0.0.1:8765`.

## Swap Your Metrics

Replace `demo_metrics.demo_payload()` with a loader from your parquet or evaluation pipeline. Keep the same JSON shape or adjust `static/index.html`.

## Non-goals

- Not a sportsbook integration
- Not a multi-tenant analytics product
- Not a prediction engine by itself

## CI

`pytest` hits `/api/metrics` with `httpx`.

## Related Repos

- [`nba-ratings`](https://github.com/ianalloway/nba-ratings): reusable Elo / logistic / Kelly primitives
- [`sports-betting-ml`](https://github.com/ianalloway/sports-betting-ml): modeling demo and value-bet pipeline
- [`backtest-report-gen`](https://github.com/ianalloway/backtest-report-gen): static report generation from evaluation JSON

## License

MIT
