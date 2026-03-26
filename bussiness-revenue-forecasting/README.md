# Business Revenue Forecasting

A small notebook-first forecasting project for monthly business revenue.

## Overview

This repository explores a simple forecasting workflow using monthly business data:

- inspect the dataset and check data quality
- build a baseline forecast
- compare a feature-based regression approach

The project is organized around Jupyter notebooks, with shared helpers in `src/`.

## Project Structure

```text
.
├── data/
│   ├── README.md
│   └── raw/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_baseline_model.ipynb
│   └── 03_model_tuning.ipynb
├── src/
│   ├── __init__.py
│   └── notebook_common.py
├── requirements.txt
└── README.md
```

## Setup

1. Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Open the notebooks in order and select the project's Python interpreter.

- `notebooks/01_eda.ipynb`
- `notebooks/02_baseline_model.ipynb`
- `notebooks/03_model_tuning.ipynb`

In VS Code or Jupyter, choose the interpreter from `venv` so the notebooks run with the installed packages.

## Notes

- `venv/` is intentionally excluded from version control.
- Reusable notebook settings and shared imports live in `src/notebook_common.py`.
- The notebooks currently reference `data/row/business_revenue_forecasting.csv`.
- The CSV itself is not included in the public repository. See `data/README.md` for the expected local path.
