a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica"]

x = zip(a, b)
print(list(x))

x = zip(a, b)
y = zip(*x)

print(list(y))


fruit = ("apple", "banana", "cherry")
enum = enumerate(fruit)

print(list(enum))


def square(n):
    return n * n


numbers = (1, 2, 3, 4, 5)
result = map(square, numbers)
results = set(result)
print(results)
