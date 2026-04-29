# quant-finance-foundations

A structured path to learn quantitative finance from the ground up.

> "Money is a story we tell ourselves. Quants tell it in math." — the goal here is to learn that language.

## Roadmap

Modules must be completed **in order**. Each builds on the last.

| # | Module | Key Topics | Status |
|---|--------|-----------|--------|
| 01 | Probability & Stochastic Processes | Measure theory, distributions, martingales, Brownian motion | 🔴 Not started |
| 02 | Statistics & Econometrics | Time series, regression, factor models, hypothesis testing | 🔴 Not started |
| 03 | Financial Theory | Portfolio theory, CAPM, EMH, derivatives pricing, Black-Scholes | 🔴 Not started |
| 04 | Numerical Methods | Monte Carlo, finite differences, binomial/trinomial trees | 🔴 Not started |
| 05 | Risk Management | VaR, CVaR, Greeks, stress testing, correlation | 🔴 Not started |
| 06 | ML for Finance | Feature engineering, backtesting, algo trading strategies | 🔴 Not started |
| 07 | Market Data Infrastructure | APIs, tick data, order books, Kafka, data pipelines | 🔴 Not started |

## Philosophy

- **Learn by building.** Every module ends with a project that implements the concepts in code.
- **Write to understand.** If you can't explain it in writing, you don't understand it.
- **Measure progress.** Each module has a clear set of deliverables.
- **No shortcuts.** Core math is non-negotiable. Skip it and you'll hit a ceiling fast.

## Structure

```
module-name/
├── notes/          # Writeups, derivations, explanations
├── resources/      # Links to papers, books, videos used
└── projects/       # Code projects for this module
```

Top-level `resources/` contains curated papers and books that span multiple modules.

## Setup

```bash
# Clone
git clone https://github.com/JorgeQuijano/quant-finance-foundations.git
cd quant-finance-foundations

# Environment (Python)
python -m venv .venv
source .venv/bin/activate
pip install numpy scipy pandas matplotlib jupyter notebook
```

## Contributing

- Work on a branch per module: `module-01-probability`
- Open a PR when the module is complete
- Commits follow [Conventional Commits](https://www.conventionalcommits.org/)
- Every project folder must have a `README.md` explaining what was built and what it demonstrates