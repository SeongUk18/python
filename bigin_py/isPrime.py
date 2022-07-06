def isPrime(number):
    isprime=True
    for k in range(2,number):
        if(number%k==0):
            isprime = False
    return isprime




number=input("원하는 범위를 입력하세요")
number=int(number)
for i in range(2,number):
    if(isPrime(i)):
        print(i)

