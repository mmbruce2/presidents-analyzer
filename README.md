# 🏛️ Presidents Analyzer

Analyzes **15 US Presidents** — tenure, age at inauguration, party affiliation, historical rankings, terms served, and key achievements.

## What It Does

- **15 US Presidents** from Washington to Biden tracked
- **Youngest inauguration**: JFK 43, Clinton 46, Grant 46, Obama 47, FDR 51
- **Oldest inauguration**: Biden 78, Trump 70, Reagan 69, Bush 64, Eisenhower 62
- **Longest tenure**: FDR 12 years (4 terms), Washington/Jefferson/Obama/Reagan 8 years each
- **Top historical rankings**: Washington #1, Lincoln #1, Jefferson #3, FDR #3, Eisenhower #5, JFK #6
- **Party breakdown**: D: 8 presidents (54 yrs avg age), R: 6 (60 yrs avg age), I: 1 (Washington)
- **Terms**: 2-term presidents dominate (9), 1-term: 5, FDR 4-term unique
- **4 charts**: Party pie, age at inauguration, tenure length, age vs ranking

## Quick Start

```bash
pip install pandas matplotlib
python run.py
```

## Key Findings

```
🏆 YOUNGEST PRESIDENTS:
   JFK 43 | Clinton 46 | Grant 46 | Obama 47 | FDR 51

🧓 OLDEST PRESIDENTS:
   Biden 78 | Trump 70 | Reagan 69 | Bush 64

⏱️ LONGEST TENURE:
   FDR 12 yrs (4 terms) | Washington/Jefferson/Obama/Reagan 8 yrs

📊 TOP HISTORICAL RANKINGS:
   #1 Washington | #1 Lincoln | #3 Jefferson | #3 FDR | #5 Eisenhower
```

## Data Source

US Presidents historical data from presidential biographies, C-SPAN Historical Presidents Survey (2022), and Miller Center archives.

## Tech Stack

- Python 3
- pandas — data processing
- matplotlib — visualization