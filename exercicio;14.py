nota1=int(input("escreva a primeira nota: "))
nota2=int(input("escreva a segunda nota: "))
nota3=int(input("escreva a terceira nota: "))
nota4=int(input("escreva a quarta nota: "))
media=(nota1+nota2+nota3+nota4)/4
print("a media é:" ,media)
if media>=6 :
    print("aprovado")
if media >=4 and media<6 :
    print("recuperação")  
if media<4 :
    print("reprovado")    


