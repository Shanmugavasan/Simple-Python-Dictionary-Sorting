d={}
num=int(input("How many letters?"))
for i in range(num):
    letter = input("Enter a letter to sort: ")
    number = input("Enter a number: ")
    d[letter] = number

#sorting starts
rawi=d.items()
l=list(d.items())
l.sort()
d=dict(l)
print(d)