# Healthcare IT Asset Health & Refresh Prioritization

> **Portfolio demonstration | Synthetic / fictional data only**

Summarizes fictional multi-clinic workstation, network device, and UPS inventory and highlights upgrade and support priorities.

## What this demonstrates
- Apply transparent risk scoring based on OS support status and asset condition
- Export a prioritization CSV and static HTML summary
- Provide operations-oriented device counts by site

## Quick start
```bash
python src/main.py
python -m unittest discover -s tests
```

Python 3.10+ is recommended. Core functionality uses the Python standard library; no API keys or patient records are required. Run commands from the repository root.

## Repository contents
- `data/assets.csv`: fictional inventory
- `src/main.py`: risk model and reporting
- `output/`: generated reporting artifacts

## Relevant skills
IT operations, inventory, infrastructure monitoring, risk scoring, reporting

## Data and privacy
All records, facilities, identifiers, events and organizations in this repository are fabricated for demonstrations. This is **not** a production clinical system and does not contain real protected health information (PHI). Do not upload real patient data or confidential employer files. Outputs do not substitute for clinical, privacy, security, or regulatory review.

## How to discuss in an interview
Explain the input, validations or transformations, measurable outputs, tests, and what you would change for a real deployment (authentication, audit logs, monitoring, regulatory review, and secure storage). Describe this as a **personal portfolio project**, not as an implementation at an employer.

## License
MIT — see [LICENSE](LICENSE).
