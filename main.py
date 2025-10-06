b,i,s,p=list("---\n"*3),0,'',0
while not(any([set([b[j]for j in L])=={s}for L in[range(p//4,p//4+3),[p%4,p%4+4,p%4+8],[0,5,10],[2,5,8]]])and(print(s,"has won")or 1)or(i>8 and (print("Draw!")or 1))or print("It is",(s:="OX"[(i:=i+1)%2])+"'s turn")or ((any((not((p:=input("Enter position (1-9) "))and 0 or not p.isdigit()or(p:=int(p)+(int(p)-1)//3-1)*0 or p<0 or p>10 or b[p]!="-"and(print("That space is taken")or 1))for _ in range(9**9))))*0)):
    b[p]=s
    print(''.join(b))
