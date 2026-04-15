# 🏛️ US Presidents Analyzer

Analyzes **23 US Presidents** across tenure, electoral dominance, scandals, wars, and economic impact. Compares Democrat vs Republican records, identifies patterns in success and failure.

## What It Does

- **Electoral dominance** — Nixon 520 EV (1972), FDR 472 EV (1936), Reagan 489 EV (1984)
- **Scandal tracking** — Nixon 3 scandals, Trump/Grant 2 each
- **War presidents** — FDR & GW Bush led through 2 wars each
- **Economic growth** — FDR tops at 3.9% avg GDP growth
- **Age analysis** — JFK youngest (43), Biden oldest (78)
- **4 charts**: electoral vote ranking, scandals vs achievements, GDP by president, age vs electoral dominance

## Quick Start

```bash
pip install pandas matplotlib
python analyzer.py
```

## Key Findings

```
🏆 ELECTORAL DOMINANCE:
   Nixon: 520 EV | Reagan: 489 EV | LBJ: 486 EV | FDR: 472 EV

💥 SCANDALS:
   Nixon: 3 | Trump: 2 | Grant: 2

⚔️ WAR PRESIDENTS:
   FDR, GW Bush: 2 wars each
   Lincoln, Wilson, LBJ, GHW Bush: 1 war each

📈 GDP LEADERS:
   FDR: 3.9% | Grant: 3.1% | Reagan: 3.1% | Truman: 3.0%

👶👴 AGE EXTREMES:
   Youngest: JFK (43), Bill Clinton (46), Grant (46)
   Oldest: Biden (78), Trump (70), Reagan (69)
```

## Data Source

Compiled from official presidential records, C-SPAN Presidential Historians Survey, and BLS GDP data.

## Tech Stack

- Python 3
- pandas — data processing
- matplotlib — visualization
