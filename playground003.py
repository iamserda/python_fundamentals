print(1 == 1)
print(1/3 != 3/9)
print("a" > "b")
print("a" < "b")
print(5 >= 5.0000000099)
print(7 <= 7.0000000001)

idx = 0

for i in range(100, 0, -23):
    idx += i
    print(f"i = {i}, idx = {idx}")
