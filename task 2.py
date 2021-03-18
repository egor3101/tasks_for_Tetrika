import wikipediaapi
from collections import Counter

wiki_wiki = wikipediaapi.Wikipedia('ru')

page_py = wiki_wiki.page("Категория:Животные по алфавиту")
check_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", ]


def animals(categorymembers, level=0, max_level=1):
    for c in categorymembers.values():
        print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
        if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
            animals(c.categorymembers, level=level + 1, max_level=max_level)


end_data = list(page_py.categorymembers)
answer = dict(Counter(s[0] for s in end_data))
for x in check_list:
    del answer[x]
for key, value in answer.items():
    print("{0}: {1}".format(key, value))
