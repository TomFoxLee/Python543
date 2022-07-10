# Ch.06 Exercise 6.4 Official Answer
# Print letters from entering strings by desc.

txt = input("Please enter strings in English: ")

counts = {}

ex = [",", ".", "?", "!", ":", ":", '"', ";"]

for i in txt:
    if (i == "") or (i in ex):
        continue
    else:
        if ord(i) < 97:
            i = chr(ord(i) + 32)

        counts[i] = counts.get(i, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for u in range(len(items)):
    alpha, count = items[u]
    print("{} -> {}".format(alpha, count))
