soma=0
cont=0
pares=0
impares=0
faixa1=0
faixa2=0
faixa3=0
faixa4=0
faixa5=0
soma1=0
soma2=0
soma3=0
soma4=0
soma5=0
n=int(input("Insira um número: "))
maior=n
menor=n
if n%2==0:
        print(n, "é par")
        pares=pares+1
else:
    print(n, "é ímpar")
    impares=impares+1
if n<0:
    print(n, "pertence a faixa 1")
    faixa1=faixa1+1
    soma1=soma1+n
elif n>=0 and n<15:
    print(n, "pertence a faixa 2")
    faixa2=faixa2+1
    soma2=soma2+n
elif n>=15 and n<100:
    print(n, "pertence a faixa 3")
    faixa3=faixa3+1
    soma3=soma3+n
elif n>=1000:
    print(n, "pertence a faixa 4")
    faixa4=faixa4+1
    soma4=soma4+n
elif n>=101 and n<1000:
    print(n, "pertence a faixa 5")
    faixa5=faixa5+1
    soma5=soma5+n
soma=soma+n
cont=cont+1
while True:
    s=str(input("Digite 'S' para continuar: "))
    if s!='s' and s!='S':
        break
    n=int(input("Insira um número: "))
    if n%2==0:
        print(n, "é par")
        pares=pares+1
    else:
        print(n, "é ímpar")
        impares=impares+1
    if n<0:
        print(n, "pertence a faixa 1")
        faixa1=faixa1+1
        soma1=soma1+n
    elif n>=0 and n<15:
        print(n, "pertence a faixa 2")
        faixa2=faixa2+1
        soma2=soma2+n
    elif n>=15 and n<100:
        print(n, "pertence a faixa 3")
        faixa3=faixa3+1
        soma3=soma3+n
    elif n>=1000:
        print(n, "pertence a faixa 4")
        faixa4=faixa4+1
        soma4=soma4+n
    elif n>=101 and n<1000:
        print(n, "pertence a faixa 5")
        faixa5=faixa5+1
        soma5=soma5+n
    if n>maior:
        maior=n
    if n<menor:
        menor=n
    soma=soma+n
    cont=cont+1
if cont>0:
    media=soma/cont
    print("A média dos números é", '%.2f' %media)
print("A quantidade de números pares é", pares, "e a quantidade de números ímpares é", impares)
print("A faixa 1 possui", faixa1, "elementos e a soma deles é", soma1)
print("A faixa 2 possui", faixa2, "elementos e a soma deles é", soma2)
print("A faixa 3 possui", faixa3, "elementos e a soma deles é", soma3)
print("A faixa 4 possui", faixa4, "elementos e a soma deles é", soma4)
print("A faixa 5 possui", faixa5, "elementos e a soma deles é", soma5)
print("O maior valor é", maior, "e o menor valor é", menor)
#coisa do diabo