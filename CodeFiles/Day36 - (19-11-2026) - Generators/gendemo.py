# print even numbers using generator

def printEvens(limit):
    for n in range(2,limit):
        if n%2==0:
            yield n


for n in printEvens(20):
    print(n)