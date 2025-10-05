b=list("---\n"*3)
for i in range(9):
    s="XO"[i%2]
    print("It is", s+"'s turn")
    while(p:=input("Enter position (1-9) "))and 0 or not p.isdigit()or(p:=int(p)+(int(p)-1)//3-1)*0 or p<0 or p>10 or b[p]!="-"and(print("That space is taken")or 1):
        1
    b[p]=s
    print(''.join(b))
    any([b[L[0]]==b[L[1]]and b[L[0]]==b[L[2]]and b[L[0]]!="-"for L in[range(p//4,p//4+3),[p%4,p%4+4,p%4+8],[0, 5, 10],[2, 5, 8]]])and(print(s,"has won")or exit())
print("Draw!")
