b = (["-"]*3+["\n"])*3

for i in range(9):
    s = "XO"[i % 2]

    print("It is", s+"'s turn")

    while True:
        try:
            p = int(input("Enter position (1-9):"))-1
        except ValueError:
            print("Enter a number from 1 to 9")
            continue
        if p < 0 or p > 8:
            print("Enter a number from 1 to 9")
            continue
        p += p//3
        if b[p] != "-":
            print("That space is taken :/")
            continue
        break

    b[p] = s

    print(''.join(b))

    if any([b[L[0]] == b[L[1]] and b[L[0]] == b[L[2]] and b[L[0]] != "-"
            for L in [[0, 1, 2], [4, 5, 6], [8, 9, 10],
                      [0, 4, 8], [1, 5, 9], [2, 6, 10],
                      [0, 5, 10], [2, 5, 8]]]):
        print(s, "has won!")
        exit()

print("Draw!")
