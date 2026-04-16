#!/usr/bin/env python3
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = [
    {"president": "George Washington", "term_start": 1789, "term_end": 1797, "party": "Independent", "age_inaug": 57, "vp": "John Adams", "terms": 2, "achievements": "Founded Cabinet, Two-term precedent", "rank_history": 1},
    {"president": "Thomas Jefferson", "term_start": 1801, "term_end": 1809, "party": "Democratic-Republican", "age_inaug": 57, "vp": "Aaron Burr", "terms": 2, "achievements": "Louisiana Purchase, Lewis & Clark", "rank_history": 3},
    {"president": "Abraham Lincoln", "term_start": 1861, "term_end": 1865, "party": "Republican", "age_inaug": 52, "vp": "Hannibal Hamlin", "terms": 2, "achievements": "Emancipation, Gettysburg Address", "rank_history": 1},
    {"president": "Franklin D. Roosevelt", "term_start": 1933, "term_end": 1945, "party": "Democratic", "age_inaug": 51, "vp": "John Nance Garner", "terms": 4, "achievements": "New Deal, WWII, Social Security", "rank_history": 3},
    {"president": "George H.W. Bush", "term_start": 1989, "term_end": 1993, "party": "Republican", "age_inaug": 64, "vp": "Dan Quayle", "terms": 1, "achievements": "End of Cold War, Gulf War", "rank_history": 20},
    {"president": "Barack Obama", "term_start": 2009, "term_end": 2017, "party": "Democratic", "age_inaug": 47, "vp": "Joe Biden", "terms": 2, "achievements": "ACA, Economic recovery, Marriage equality", "rank_history": 8},
    {"president": "John F. Kennedy", "term_start": 1961, "term_end": 1963, "party": "Democratic", "age_inaug": 43, "vp": "Lyndon Johnson", "terms": 1, "achievements": "Moon landing, Peace Corps", "rank_history": 6},
    {"president": "Ronald Reagan", "term_start": 1981, "term_end": 1989, "party": "Republican", "age_inaug": 69, "vp": "George H.W. Bush", "terms": 2, "achievements": "Tax cuts, Cold War end", "rank_history": 9},
    {"president": "Bill Clinton", "term_start": 1993, "term_end": 2001, "party": "Democratic", "age_inaug": 46, "vp": "Al Gore", "terms": 2, "achievements": "Economic surplus, NAFTA", "rank_history": 15},
    {"president": "Donald Trump", "term_start": 2017, "term_end": 2021, "party": "Republican", "age_inaug": 70, "vp": "Mike Pence", "terms": 1, "achievements": "Tax cuts, Judicial appointments", "rank_history": 45},
    {"president": "Joe Biden", "term_start": 2021, "term_end": 2025, "party": "Democratic", "age_inaug": 78, "vp": "Kamala Harris", "terms": 1, "achievements": "Infrastructure, CHIPS Act", "rank_history": 14},
    {"president": "Dwight D. Eisenhower", "term_start": 1953, "term_end": 1961, "party": "Republican", "age_inaug": 62, "vp": "Richard Nixon", "terms": 2, "achievements": "Interstate Highway, NASA", "rank_history": 5},
    {"president": "Jimmy Carter", "term_start": 1977, "term_end": 1981, "party": "Democratic", "age_inaug": 52, "vp": "Walter Mondale", "terms": 1, "achievements": "Camp David Accords", "rank_history": 22},
    {"president": "Andrew Jackson", "term_start": 1829, "term_end": 1837, "party": "Democratic", "age_inaug": 61, "vp": "Martin Van Buren", "terms": 2, "achievements": "Populist democracy", "rank_history": 18},
    {"president": "Ulysses S. Grant", "term_start": 1869, "term_end": 1877, "party": "Republican", "age_inaug": 46, "vp": "Schuyler Colfax", "terms": 2, "achievements": "Reconstruction, KKK suppression", "rank_history": 21},
]

with open('/tmp/presidents-analyzer/presidents.json', 'w') as f:
    json.dump(data, f, indent=2)

df = pd.DataFrame(data)
df['tenure_years'] = df['term_end'] - df['term_start']
df['party_abbr'] = df['party'].apply(lambda x: 'D' if 'Democratic' in x else ('R' if 'Republican' in x else 'I'))

print("=" * 60)
print("  PRESIDENTS ANALYZER")
print("  US Presidents | Tenure, Age, Party, Historical Rankings")
print("=" * 60)
print(f"\nTotal presidents: {len(df)}")

print("\n🏆 YOUNGEST AT INAUGURATION:")
for _, r in df.nsmallest(5, 'age_inaug').iterrows():
    print(f"   {r['president']}: {int(r['age_inaug'])} years old | {r['party_abbr']} | {int(r['term_start'])}")

print("\n🧓 OLDEST AT INAUGURATION:")
for _, r in df.nlargest(5, 'age_inaug').iterrows():
    print(f"   {r['president']}: {int(r['age_inaug'])} years old | {r['party_abbr']} | {int(r['term_start'])}")

print("\n⏱️ LONGEST TENURE:")
for _, r in df.nlargest(5, 'tenure_years').iterrows():
    print(f"   {r['president']}: {int(r['tenure_years'])} years | {r['party_abbr']} | {int(r['term_start'])}")

print("\n🏅 MOST TERMS SERVED:")
for _, r in df[df['terms'] > 1].nlargest(5, 'terms').iterrows():
    print(f"   {r['president']}: {int(r['terms'])} terms | {r['party_abbr']} | {int(r['term_start'])}")

print("\n📊 HISTORICAL RANKINGS (lower = better):")
for _, r in df.nsmallest(10, 'rank_history').iterrows():
    print(f"   #{int(r['rank_history'])} {r['president']} | {r['party_abbr']} | {r['achievements'][:40]}...")

print("\n🗳️ BY PARTY (avg tenure):")
by_party = df.groupby('party_abbr').agg(presidents=('president','count'), avg_age=('age_inaug','mean'), avg_tenure=('tenure_years','mean'))
for party, row in by_party.iterrows():
    print(f"   {party}: {int(row['presidents'])} presidents | {row['avg_tenure']:.1f} yrs avg tenure | {row['avg_age']:.0f} yrs avg age")

print("\n📈 TERMS DISTRIBUTION:")
term_counts = df['terms'].value_counts().sort_index()
for terms, count in term_counts.items():
    print(f"   {int(terms)} term(s): {count} presidents")

# Charts
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
party_colors = {'D': '#2E86AB', 'R': '#E63946', 'I': '#888888'}

# Chart 1: Presidents by party
party_counts = df['party_abbr'].value_counts()
axes[0,0].pie(party_counts.values, labels=party_counts.index, autopct='%1.0f%%', colors=[party_colors.get(p,'gray') for p in party_counts.index])
axes[0,0].set_title('Presidents by Party')

# Chart 2: Age at inauguration
sorted_age = df.sort_values('age_inaug')
axes[0,1].barh(range(len(sorted_age)), sorted_age['age_inaug'], color=[party_colors.get(p,'gray') for p in sorted_age['party_abbr']])
axes[0,1].set_yticks(range(len(sorted_age)))
axes[0,1].set_yticklabels(sorted_age['president'], fontsize=8)
axes[0,1].set_xlabel('Age at Inauguration')
axes[0,1].set_title('Presidents Age at Inauguration (Blue=D, Red=R)')
for i, v in enumerate(sorted_age['age_inaug']):
    axes[0,1].text(v+0.3, i, str(int(v)), va='center', fontsize=7)

# Chart 3: Tenure by president
sorted_tenure = df.sort_values('tenure_years')
axes[1,0].barh(range(len(sorted_tenure)), sorted_tenure['tenure_years'], color=[party_colors.get(p,'gray') for p in sorted_tenure['party_abbr']])
axes[1,0].set_yticks(range(len(sorted_tenure)))
axes[1,0].set_yticklabels(sorted_tenure['president'], fontsize=8)
axes[1,0].set_xlabel('Years in Office')
axes[1,0].set_title('Presidential Tenure (Blue=D, Red=R)')
for i, v in enumerate(sorted_tenure['tenure_years']):
    axes[1,0].text(v+0.2, i, str(int(v)), va='center', fontsize=7)

# Chart 4: Historical ranking vs age
axes[1,1].scatter(df['age_inaug'], df['rank_history'], c=[party_colors.get(p,'gray') for p in df['party_abbr']], s=80, alpha=0.8)
for _, r in df.iterrows():
    if r['rank_history'] <= 5 or r['age_inaug'] <= 45 or r['age_inaug'] >= 70:
        axes[1,1].annotate(r['president'][:12], (r['age_inaug'], r['rank_history']), fontsize=7)
axes[1,1].set_xlabel('Age at Inauguration')
axes[1,1].set_ylabel('Historical Rank (lower=better)')
axes[1,1].set_title('Age vs Historical Ranking (Blue=D, Red=R)')
axes[1,1].invert_yaxis()

plt.tight_layout()
plt.savefig('/tmp/presidents-analyzer/presidents_analysis.png', dpi=150, bbox_inches='tight')
print("\n📈 Chart saved: presidents_analysis.png")
df.to_csv('/tmp/presidents-analyzer/presidents.csv', index=False)
print("📄 Data saved: presidents.csv")
print("DONE")