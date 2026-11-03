# Healthcare IT Asset Health & Refresh Prioritization

![Python](https://img.shields.io/badge/python-3.10%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A Python tool that scores a multi-clinic inventory of workstations, network devices, and UPS units by risk, so IT teams can see what to upgrade or retire first.

> Built on a fictional inventory only. Scoring rules are illustrative.

## Why this exists

Clinic IT teams rarely have budget to refresh everything. Unsupported operating systems and worn-out hardware are the biggest exposure, but they are hard to spot in a flat inventory spreadsheet. This project applies a transparent scoring rule to turn an inventory into a ranked refresh list.

## How it works

- Each asset is scored using **OS support status** and **asset condition**.
- Assets are ranked into a prioritization list.
- Device counts are summarized by site for operations planning.

## Outputs

- A prioritization CSV (`asset_priorities.csv`)
- A static HTML summary (`summary.html`)

## Project structure

```
.
├── data/
│   └── assets.csv             # fictional inventory
├── src/
│   └── main.py                # risk scoring and reporting
├── tests/
│   └── test_main.py
├── output/
│   ├── asset_priorities.csv   # generated ranking
│   └── summary.html           # generated summary
├── LICENSE
└── README.md
```

## Quick start

Requires Python 3.10+ (standard library only). Run from the repository root.

```bash
python src/main.py                      # regenerates the files in output/
python -m unittest discover -s tests
```

## Limitations and next steps

- The scoring rule is deliberately simple and unweighted by clinical criticality.
- Static report; no live inventory feed.
- Possible extensions: weight by how critical the device is to patient care, factor in warranty and age, connect to an asset-management export, and add cost estimates for refresh planning.

## License

MIT. See [LICENSE](LICENSE).
