# Healthcare IT Asset Refresh Prioritization

This is a scoring script for a pretend group of clinics with 36 devices across three sites: workstations, network switches and UPS units. Clinic IT never has the budget to replace everything at once, so I wanted a simple, transparent way to answer one question: which devices should we replace first?

The inventory is made up, and the scoring rules are my own.

## How the scoring works

Every asset in `data/assets.csv` starts at 0 points and picks up points like this:

| Rule                                       | Points |
|--------------------------------------------|--------|
| Condition is `warning`                     | +25    |
| Condition is `critical`                    | +60    |
| Workstation still on Windows 10            | +30    |
| Purchased in 2021 or earlier               | +15    |

The total is capped at 100. Then each asset gets a priority:

- **High**: 60 or more
- **Medium**: 25 to 59
- **Low**: under 25

I made a `critical` condition worth 60 on purpose, because that puts the device straight into High on its own. If a device is failing, it doesn't matter how new it is.

## Running it

You need Python 3.10 or newer. There's nothing to install.

```bash
python src/main.py
python -m unittest discover -s tests
```

Run both commands from the repo root. The script writes two files:

- `output/asset_priorities.csv`: every asset with its score and priority, sorted from highest risk down
- `output/summary.html`: a one-page count of High, Medium and Low

## What the sample data shows

There are 36 assets: **12 high**, **14 medium** and **10 low**.

The top of the list is mostly North site workstations that are critical, still on Windows 10, and bought in 2020:

| Asset    | Site  | Type        | Why                                       | Score |
|----------|-------|-------------|-------------------------------------------|-------|
| ASSET012 | North | workstation | critical + Windows 10 + 2020              | 100   |
| ASSET030 | North | workstation | critical + Windows 10 + 2020              | 100   |
| ASSET009 | North | workstation | critical + Windows 10                     | 90    |
| ASSET033 | North | workstation | critical + Windows 10                     | 90    |
| ASSET019 | West  | switch      | critical + 2021                           | 75    |

6 of the 12 high-priority assets are at North, compared with 4 at Central and 2 at West. If I only had budget for one site, I'd start with North.

## Some decisions I made

- **The Windows 10 penalty only applies to workstations.** Switches and UPS units don't run a desktop OS, so the end of Windows 10 support isn't their problem.
- **I used simple points instead of weights or formulas.** Anyone can look at a score of 70 and work out where it came from. I think that matters more than precision when you're asking someone to sign off on a budget.
- **The output is a CSV.** It opens in Excel, and that's where an IT manager would actually sort it and add notes.

## Files

```
data/assets.csv               fictional inventory (36 devices, 3 sites)
src/main.py                   scoring and report output
tests/test_main.py            unit tests for the scoring rule
output/asset_priorities.csv   generated ranked list
output/summary.html           generated summary page
```

## What I'd add next

- A high/medium/low breakdown by site in the HTML summary, since right now I'm working that out by hand
- Weighting by clinical criticality. A workstation in an exam room matters more than one in a back office.
- Warranty end dates and estimated replacement cost, so the list can turn into an actual budget
- Reading from an asset-management export instead of a hand-made CSV
