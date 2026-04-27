enquanto=0
par=0
impares=0

while enquanto<10:
    n=int(input("digite um numero: "))
    enquanto +=1
    if n%2==0:
        par+=1
    elif n%2==1:
        impares+=1
print("pares :" ,par ,"impares:" , impares)
