a = "jrypbzr"+ "vfy"+ "yno"
b = "Nghfb"+ "Vabzngn"
c = "Znkxk"+ "oy" + "grcgey" + "romnz" + "hknotj" + "znk" + "iruajy"

def caesar(s, n):
    ns = []
    for ch in s:
        # A - Z
        if ('A' <= ch and ch <= 'Z'):
            ns.append(chr((ord(ch) - ord('A') - n) % 26 + ord('A')))
        # a - z
        elif ('a' <= ch and ch <= 'z'):
            ns.append(chr((ord(ch) - ord('a') - n) % 26 + ord('a')))
        # no change for other characters
        else:
            ns.append(ch)
    return "".join(ns)
for i in range (26):
    result = caesar(a, i)
    print(result)

for i in range (26):
    result = caesar(b, i)
    print(result)

for i in range (26):
    result = caesar(c, i)
    print(result)

# a = welcomeisllab
# b = AtusoInomata 　Atusoになってる…
# c = Thereisalwayslightbehindtheclouds