print("opçoes:1 somas,2 subtrais,3 multiplicas,dividir")
op=int(input("digite sua opção ou o para sair: "))
n1=int(input("digite um número: "))
n2=int(input("digite um número: "))
if op==0 and op>4:
   print("encerrado ou número invalido?")
else:
   while op !=0:
    if op==1:
      print(n1+n2)
    elif op==2:
      print(n1-n2)
    elif op==3:
     print(n1*n2)
    else:
      print(n1/n2)
    op=int(input("digite sua opção"))
