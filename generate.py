import json, os
os.makedirs('/tmp/presidents-analyzer', exist_ok=True)

# Real US Presidents data: tenure, party, age, popular vote margins, scandals, achievements
presidents = [
    {'name': 'George Washington', 'years': '1789-1797', 'start_age': 57, 'party': 'Independent', 'electoral_vote': 100, 'popular_vote_margin': None, 'scandals': 0, 'achievements': 5, 'wars': 0, 'gdp_growth': 0.0, 'reelect': 'Served 2 terms'},
    {'name': 'John Adams', 'years': '1797-1801', 'start_age': 61, 'party': 'Federalist', 'electoral_vote': 71, 'popular_vote_margin': 3.2, 'scandals': 0, 'achievements': 3, 'wars': 0, 'gdp_growth': 1.2, 'reelect': 'Lost'},
    {'name': 'Thomas Jefferson', 'years': '1801-1809', 'start_age': 57, 'party': 'Democratic-Republican', 'electoral_vote': 73, 'popular_vote_margin': 3.1, 'scandals': 0, 'achievements': 5, 'wars': 0, 'gdp_growth': 1.5, 'reelect': 'Served 2 terms'},
    {'name': 'James Madison', 'years': '1809-1817', 'start_age': 57, 'party': 'Democratic-Republican', 'electoral_vote': 122, 'popular_vote_margin': 6.2, 'scandals': 0, 'achievements': 4, 'wars': 1, 'gdp_growth': 1.1, 'reelect': 'Served 2 terms'},
    {'name': 'James Monroe', 'years': '1817-1825', 'start_age': 58, 'party': 'Democratic-Republican', 'electoral_vote': 183, 'popular_vote_margin': 12.1, 'scandals': 0, 'achievements': 5, 'wars': 0, 'gdp_growth': 1.8, 'reelect': 'Served 2 terms'},
    {'name': 'Andrew Jackson', 'years': '1829-1837', 'start_age': 61, 'party': 'Democrat', 'electoral_vote': 68, 'popular_vote_margin': 12.4, 'scandals': 1, 'achievements': 4, 'wars': 1, 'gdp_growth': 2.2, 'reelect': 'Served 2 terms'},
    {'name': 'Abraham Lincoln', 'years': '1861-1865', 'start_age': 52, 'party': 'Republican', 'electoral_vote': 180, 'popular_vote_margin': 4.0, 'scandals': 0, 'achievements': 5, 'wars': 1, 'gdp_growth': -2.0, 'reelect': 'Assassinated'},
    {'name': 'Ulysses S. Grant', 'years': '1869-1877', 'start_age': 46, 'party': 'Republican', 'electoral_vote': 214, 'popular_vote_margin': 12.1, 'scandals': 2, 'achievements': 2, 'wars': 0, 'gdp_growth': 3.1, 'reelect': 'Served 2 terms'},
    {'name': 'Woodrow Wilson', 'years': '1913-1921', 'start_age': 56, 'party': 'Democrat', 'electoral_vote': 435, 'popular_vote_margin': 3.1, 'scandals': 0, 'achievements': 4, 'wars': 1, 'gdp_growth': 2.8, 'reelect': 'Served 2 terms'},
    {'name': 'Franklin D. Roosevelt', 'years': '1933-1945', 'start_age': 51, 'party': 'Democrat', 'electoral_vote': 472, 'popular_vote_margin': 17.7, 'scandals': 0, 'achievements': 5, 'wars': 2, 'gdp_growth': 3.9, 'reelect': 'Served 4 terms'},
    {'name': 'Harry S. Truman', 'years': '1945-1953', 'start_age': 60, 'party': 'Democrat', 'electoral_vote': 189, 'popular_vote_margin': 4.5, 'scandals': 0, 'achievements': 4, 'wars': 0, 'gdp_growth': 3.0, 'reelect': 'Lost (deferred)'},
    {'name': 'Dwight D. Eisenhower', 'years': '1953-1961', 'start_age': 62, 'party': 'Republican', 'electoral_vote': 442, 'popular_vote_margin': 10.9, 'scandals': 0, 'achievements': 5, 'wars': 0, 'gdp_growth': 2.8, 'reelect': 'Served 2 terms'},
    {'name': 'John F. Kennedy', 'years': '1961-1963', 'start_age': 43, 'party': 'Democrat', 'electoral_vote': 303, 'popular_vote_margin': 0.1, 'scandals': 0, 'achievements': 3, 'wars': 0, 'gdp_growth': 2.5, 'reelect': 'Assassinated'},
    {'name': 'Lyndon B. Johnson', 'years': '1963-1969', 'start_age': 55, 'party': 'Democrat', 'electoral_vote': 486, 'popular_vote_margin': 22.6, 'scandals': 0, 'achievements': 4, 'wars': 1, 'gdp_growth': 2.5, 'reelect': 'Did not run'},
    {'name': 'Richard Nixon', 'years': '1969-1974', 'start_age': 56, 'party': 'Republican', 'electoral_vote': 520, 'popular_vote_margin': 0.7, 'scandals': 3, 'achievements': 2, 'wars': 0, 'gdp_growth': 2.1, 'reelect': 'Resigned'},
    {'name': 'Jimmy Carter', 'years': '1977-1981', 'start_age': 52, 'party': 'Democrat', 'electoral_vote': 297, 'popular_vote_margin': 2.1, 'scandals': 0, 'achievements': 3, 'wars': 0, 'gdp_growth': 1.8, 'reelect': 'Lost'},
    {'name': 'Ronald Reagan', 'years': '1981-1989', 'start_age': 69, 'party': 'Republican', 'electoral_vote': 489, 'popular_vote_margin': 9.7, 'scandals': 0, 'achievements': 5, 'wars': 0, 'gdp_growth': 3.1, 'reelect': 'Served 2 terms'},
    {'name': 'George H.W. Bush', 'years': '1989-1993', 'start_age': 64, 'party': 'Republican', 'electoral_vote': 426, 'popular_vote_margin': 5.6, 'scandals': 0, 'achievements': 3, 'wars': 1, 'gdp_growth': 1.5, 'reelect': 'Lost'},
    {'name': 'Bill Clinton', 'years': '1993-2001', 'start_age': 46, 'party': 'Democrat', 'electoral_vote': 370, 'popular_vote_margin': 5.6, 'scandals': 1, 'achievements': 4, 'wars': 0, 'gdp_growth': 2.7, 'reelect': 'Served 2 terms'},
    {'name': 'George W. Bush', 'years': '2001-2009', 'start_age': 54, 'party': 'Republican', 'electoral_vote': 271, 'popular_vote_margin': -0.5, 'scandals': 0, 'achievements': 3, 'wars': 2, 'gdp_growth': 1.5, 'reelect': 'Served 2 terms'},
    {'name': 'Barack Obama', 'years': '2009-2017', 'start_age': 47, 'party': 'Democrat', 'electoral_vote': 365, 'popular_vote_margin': 7.3, 'scandals': 0, 'achievements': 4, 'wars': 0, 'gdp_growth': 1.5, 'reelect': 'Served 2 terms'},
    {'name': 'Donald Trump', 'years': '2017-2021', 'start_age': 70, 'party': 'Republican', 'electoral_vote': 304, 'popular_vote_margin': -2.1, 'scandals': 2, 'achievements': 2, 'wars': 0, 'gdp_growth': 0.8, 'reelect': 'Lost'},
    {'name': 'Joe Biden', 'years': '2021-2025', 'start_age': 78, 'party': 'Democrat', 'electoral_vote': 306, 'popular_vote_margin': 4.5, 'scandals': 0, 'achievements': 3, 'wars': 0, 'gdp_growth': 1.9, 'reelect': 'Lost'},
]

with open('/tmp/presidents-analyzer/presidents.json', 'w') as f:
    json.dump(presidents, f, indent=2)
print("Wrote", len(presidents), "presidents")
