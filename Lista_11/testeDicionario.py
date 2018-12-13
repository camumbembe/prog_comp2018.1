from collections import OrderedDict

d = {
    34: 'fdfh',
    56: 'zjkdfk',
    23: 'hfuhei',
    75: 'aasfsa'
}

for oque in d:
    print(oque)



dd = OrderedDict(sorted(d.items(), key=lambda x: x[1]))



print(dd)