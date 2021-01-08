n=int(input("請輸入一個正整數:"))
if n<=1:
    print("沒有質數")
elif n==2:
    print("質數為2")
else:
    print("在{}內的質數有".format(n))
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j ==0:
                break;
        else:
            print(i)