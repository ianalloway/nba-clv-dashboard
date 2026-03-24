"""FastAPI app."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from nba_clv_dashboard.demo_metrics import demo_payload

STATIC = Path(__file__).resolve().parent / "static"

app = FastAPI(title="NBA CLV Dashboard", version="0.1.0")
app.mount("/static", StaticFiles(directory=STATIC), name="static")


@app.get("/api/metrics")
def metrics():
    return demo_payload()


@app.get("/", response_class=HTMLResponse)
def index():
    return (STATIC / "index.html").read_text(encoding="utf-8")
