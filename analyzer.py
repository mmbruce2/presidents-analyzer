"""
US Presidents Analyzer
Analyzes 23 US Presidents across tenure, electoral dominance, scandals, wars, and economic impact.
Identifies patterns in presidential success and failure.

Run: python analyzer.py
"""
import json
import pandas as pd
import matplotlib.pyplot as plt

def main():
    with open('presidents.json') as f:
        presidents = json.load(f)
    df = pd.DataFrame(presidents)

    print("=" * 55)
    print("  US PRESIDENTS ANALYZER")
    print("  23 presidents | Tenure, Scandals, Wars, Economy")
    print("=" * 55)
    print("\nTotal presidents: " + str(len(df)))

    # Youngest/oldest at inauguration
    youngest = df.nsmallest(3, 'start_age')
    oldest = df.nlargest(3, 'start_age')
    print("\n👶 YOUNGEST TO TAKE OFFICE:")
    for _, r in youngest.iterrows():
        print("   " + r['name'] + ": age " + str(r['start_age']))
    print("\n👴 OLDEST TO TAKE OFFICE:")
    for _, r in oldest.iterrows():
        print("   " + r['name'] + ": age " + str(r['start_age']))

    # Electoral dominance
    print("\n🏆 ELECTORAL VOTE DOMINANCE:")
    top_ev = df.nlargest(5, 'electoral_vote')
    for _, r in top_ev.iterrows():
        print("   " + r['name'].ljust(25) + ": " + str(r['electoral_vote']) + " EV (" + r['years'] + ")")

    # Scandals
    print("\n💥 PRESIDENTS WITH SCANDALS:")
    scandaled = df[df['scandals'] > 0].sort_values('scandals', ascending=False)
    for _, r in scandaled.iterrows():
        bar = '🔴' * r['scandals']
        print("   " + r['name'].ljust(25) + ": " + str(r['scandals']) + " " + bar)

    # Wars led
    print("\n⚔️ PRESIDENTS WHO LED THROUGH WAR:")
    war_pres = df[df['wars'] > 0].sort_values('wars', ascending=False)
    for _, r in war_pres.iterrows():
        wars_str = 'War' if r['wars'] == 1 else 'Wars'
        print("   " + r['name'].ljust(25) + ": " + str(r['wars']) + " " + wars_str)

    # Achievement ratings
    print("\n⭐ HIGHEST ACHIEVEMENT RATINGS:")
    top_ach = df.nlargest(5, 'achievements')
    for _, r in top_ach.iterrows():
        bar = '★' * r['achievements']
        print("   " + r['name'].ljust(25) + ": " + bar)

    # GDP growth
    print("\n📈 BEST ECONOMIC GROWTH PRESIDENTS:")
    top_gdp = df.nlargest(5, 'gdp_growth')
    for _, r in top_gdp.iterrows():
        print("   " + r['name'].ljust(25) + ": " + str(r['gdp_growth']) + "% avg growth")

    # Party analysis
    print("\n🏛️ AVERAGE SCANDALS BY PARTY:")
    party_stats = df.groupby('party').agg(
        presidents=('name','count'),
        avg_scandals=('scandals','mean'),
        avg_wars=('wars','mean'),
        avg_gdp=('gdp_growth','mean'),
    ).sort_values('avg_scandals', ascending=False)
    for party, row in party_stats.iterrows():
        print("   " + party.ljust(15) + ": " + str(int(row['presidents'])) + " presidents | " + str(round(row['avg_scandals'],1)) + " avg scandals | " + str(round(row['avg_wars'],1)) + " avg wars | " + str(round(row['avg_gdp'],1)) + "% GDP")

    # Reelect analysis
    print("\n🗳️ RE-ELECTION FATE:")
    reelect_counts = df['reelect'].value_counts()
    for fate, cnt in reelect_counts.items():
        print("   " + str(fate).ljust(20) + ": " + str(cnt))

    # Visualizations
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Chart 1: Electoral votes
    top10 = df.nlargest(10, 'electoral_vote').sort_values('electoral_vote')
    colors1 = ['#e63946' if 'Democrat' in p else '#457b9d' for p in top10['party']]
    axes[0,0].barh(range(len(top10)), top10['electoral_vote'], color=colors1)
    axes[0,0].set_yticks(range(len(top10)))
    axes[0,0].set_yticklabels(top10['name'], fontsize=8)
    axes[0,0].set_xlabel('Electoral Votes')
    axes[0,0].set_title('Top 10 Electoral Vote Winners')

    # Chart 2: Scandals vs achievements
    axes[0,1].scatter(df['scandals'], df['achievements'],
                      c=['#e63946' if 'Democrat' in p else '#457b9d' for p in df['party']],
                      s=80, alpha=0.8)
    for _, r in df.iterrows():
        axes[0,1].annotate(r['name'][:10], (r['scandals']+0.05, r['achievements']+0.05), fontsize=6)
    axes[0,1].set_xlabel('Scandals')
    axes[0,1].set_ylabel('Achievement Rating')
    axes[0,1].set_title('Scandals vs Achievements (Red=Dem, Blue=Rep)')

    # Chart 3: GDP growth by president
    df_sorted = df.sort_values('gdp_growth')
    colors3 = ['#2a9d8f' if g >= 2 else '#e63946' for g in df_sorted['gdp_growth']]
    axes[1,0].barh(range(len(df_sorted)), df_sorted['gdp_growth'], color=colors3)
    axes[1,0].set_yticks(range(len(df_sorted)))
    axes[1,0].set_yticklabels(df_sorted['name'], fontsize=6)
    axes[1,0].set_xlabel('Avg GDP Growth (%)')
    axes[1,0].set_title('Economic Growth by President')
    axes[1,0].axvline(x=0, color='black', linestyle='-', linewidth=0.5)

    # Chart 4: Age at inauguration vs electoral votes
    axes[1,1].scatter(df['start_age'], df['electoral_vote'],
                      c=['#e63946' if 'Democrat' in p else '#457b9d' for p in df['party']],
                      s=80, alpha=0.8)
    for _, r in df.iterrows():
        axes[1,1].annotate(r['name'][:8], (r['start_age']+0.3, r['electoral_vote']+5), fontsize=6)
    axes[1,1].set_xlabel('Age at Inauguration')
    axes[1,1].set_ylabel('Electoral Votes')
    axes[1,1].set_title('Age vs Electoral Dominance (Red=Dem, Blue=Rep)')

    plt.tight_layout()
    plt.savefig('presidents_analysis.png', dpi=150, bbox_inches='tight')
    print("\n📈 Chart saved: presidents_analysis.png")
    df.to_csv('presidents.csv', index=False)
    print("📄 Data saved: presidents.csv")

if __name__ == '__main__':
    main()
