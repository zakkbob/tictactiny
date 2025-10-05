b=list("---\n"*3)
for i in range(9):
    s="XO"[i%2]
    print("It is",s+"'s turn")
    any((not((p:=input("Enter position (1-9) "))and 0 or not p.isdigit()or(p:=int(p)+(int(p)-1)//3-1)*0 or p<0 or p>10 or b[p]!="-"and(print("That space is taken")or 1))for _ in range(9**9)))
    b[p]=s
    print(''.join(b))
    any([set([b[j]for j in L])=={s}for L in[range(p//4,p//4+3),[p%4,p%4+4,p%4+8],[0,5,10],[2,5,8]]])and(print(s,"has won")or exit())
print("Draw!")
