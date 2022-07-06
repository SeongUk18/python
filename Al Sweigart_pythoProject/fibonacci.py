def fibo(count):
    fibo_list=[]
    fibo_1=0
    fibo_2=1
    if(count==1):
        fibo_list=[0]
        return fibo_list
    elif(count==2):
        fibo_list=[0,1]
        return fibo_list
    else:
        fibo_list=[0,1]
        while count-2:
            temp=fibo_1+fibo_2
            fibo_list.append(temp)
            count=count-1
            fibo_1=fibo_2
            fibo_2=temp
    return fibo_list

while True:
    count=input("길이를 입력하세요 (나가려면 Q입력)")
    if(count=="Q"):
        break
    else:
        count=int(count)
        print(fibo(count))


