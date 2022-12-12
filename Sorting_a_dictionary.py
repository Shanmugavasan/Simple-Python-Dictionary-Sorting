print("RAW DICTIONARY")
d={"b":100,"a":200,"c":300}
print(d)

print("==========================================================")
print("RAW ITEMS")
rawi=d.items()
print(rawi)

print("==========================================================")
print("CONVERTED TO LIST")
l=list(d.items())
print(l)

print("==========================================================")
print("SORTING THE LIST")
l.sort()
print(l)

print("==========================================================")
print("CONVERTING IT BACK TO A DICTIONARY")
d=dict(l)
print(d)
