b = (["-"]*3+["\n"])*3

for i in range(9):
    s = "XO"[i % 2]

    print("It is", s+"'s turn")

    while 1:
        p = input("Enter position (1-9):")
        if not p.isdigit() or (p := int((int(p)-1)*1.35))*0 or p < 0 or p > 10:
            print("Enter a number from 1 to 9")
        elif b[p] != "-":
            print("That space is taken :/")
        else:
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
