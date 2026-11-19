# create a generator function

def  generateNumbers():
    print("Generating numbers...")
    yield 1
    print("Generating 2nd value")
    yield 2
    print("Generating 3rd value")
    yield 3
    print("Generating 4th value")
    yield 4
    print("Generating 5th value")
    yield 5

result = generateNumbers()
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))