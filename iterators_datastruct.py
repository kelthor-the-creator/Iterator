tupl = (6,"twelve",24)
tuplitr = iter(tupl)

for x in tupl:
    print("1: ",next(tuplitr))

lis = [5,"10",15,"30",60.0]
lisitr = iter(lis)

for y in lis:
    print("2: ",next(lisitr))


strng = "Kelthor"
strngitr = iter(strng)

for x in strng:
    print("3: ", next(strngitr))