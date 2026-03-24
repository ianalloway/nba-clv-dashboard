"""Synthetic metrics for portfolio demo — swap with your backtest JSON."""

from __future__ import annotations


def demo_payload() -> dict:
    """Calibration bins + rolling accuracy + CLV summary."""
    return {
        "model_name": "Demo NBA Classifier",
        "overall_accuracy": 0.683,
        "brier": 0.198,
        "n_test": 1840,
        "calibration": [
            {"bin_mid": 0.1, "pred_mean": 0.11, "obs_freq": 0.09, "n": 180},
            {"bin_mid": 0.3, "pred_mean": 0.29, "obs_freq": 0.31, "n": 420},
            {"bin_mid": 0.5, "pred_mean": 0.51, "obs_freq": 0.50, "n": 510},
            {"bin_mid": 0.7, "pred_mean": 0.68, "obs_freq": 0.66, "n": 400},
            {"bin_mid": 0.9, "pred_mean": 0.87, "obs_freq": 0.85, "n": 330},
        ],
        "rolling_accuracy": [
            {"week": 1, "acc": 0.64},
            {"week": 2, "acc": 0.67},
            {"week": 3, "acc": 0.69},
            {"week": 4, "acc": 0.70},
            {"week": 5, "acc": 0.68},
            {"week": 6, "acc": 0.71},
        ],
        "clv_summary": {
            "mean_clv_cents": 1.8,
            "pct_bets_positive_clv": 0.54,
            "closing_line_value_note": "Positive mean vs closing implies price beat market efficiency on average (demo only).",
        },
    }
