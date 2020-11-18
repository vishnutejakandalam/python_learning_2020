# rounds = int(input("Enter number of rounds"))
rounds = 5
player1 = [140, 89, 90, 102, 70]
player2 = [90, 88, 110, 137, 50]

# for i in range(rounds):
#     player1.append(int(input()))
#     player2.append(int(input()))
diff = []

for i in range(rounds):
    diff.append(player1[i]-player2[i])
diff2 = diff
diff = list(map(abs, diff))

print(max(diff),min(diff2))


if max(diff) == abs(min(diff2)):
    print("2")
else:
    print("1")
