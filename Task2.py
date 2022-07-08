from mwclient import Site

site = Site("ru.wikipedia.org")
category = site.categories['Животные по алфавиту']

ans = dict()
for page in category:
    first_letter = page.name[0]
    ans[first_letter] = ans[first_letter] + 1 if first_letter in ans else 1

for k, v in ans.items():
    print(f"{k}:{v}")
