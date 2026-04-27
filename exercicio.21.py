print ("opções; 1 somar , 2 subtrair , 3 multiplicar , 4 dividir")
op= int(input("digite sua opção ou para sair: "))
n1= int(input("digite n1: "))
n2= int (input("digite n2: "))
while op!=0:
   if op ==1:
      print(n1+n2)
   elif op==2:
      if n1>n2:
        print(n1-n2)
      else:
         print(n2-n1)
   elif op==3:
      print(n1*n2)
   elif  op ==4:
      if n1>n2:
        print(n1/n2)
      else:
         print(n2/n1)
   op=int(input("digite a opção "))
        

      

          