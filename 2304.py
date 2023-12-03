F = 0
r1, r2 = 0, 0
with open('04.' + str(F)) as file:
    for line in file:
        line=line.strip()
        print(line)


print("part 1:", r1)
print("part 2:", r2)
