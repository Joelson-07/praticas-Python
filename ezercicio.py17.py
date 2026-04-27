num=int(input("digite um número para a tabuada :"))
op=int(input("Qual a tabuada , 1 somar , 2 subtrair ,3 multiplicar , 4 dividir"))
if op ==1:
    for i in range (0,11):
        print(i , "+" , num ,"=" , i+num)
elif op==2:
    for i in range(0,11):
        print(i ,"-" , num ,"=" , i-num)
elif op==3:
    for i in range(0,11):
        print(i , "*" , num ,"=" , i*num)
elif op==4:
    for i in range(0,11):
        print(i , "/" , num ,"=" , i/num)             
