def factorFinder(number):
    fac=[]
    for i in range(number):
        i=i+1
        if(number%i==0):
            fac.append(i)
    return fac


while True:
    number=input("수를 입력하세요 (나가려면 Q입력)")
    if(number=="Q"):
        break
    else:
        number=int(number)
        print(factorFinder(number))

