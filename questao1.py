nome=str(input("Nome do funcionário: "))
salario=float(input("Salário: "))
if salario>=0:
    if salario<=400:
        aumento="15%"
        nsalario=salario+(salario/100)*15
    elif salario<=700:
        aumento="12%"
        nsalario=salario+(salario/100)*12
    elif salario<=1000:
        aumento="10%"
        nsalario=salario+(salario/100)*10
    elif salario<=1800:
        aumento="7%"
        nsalario=salario+(salario/100)*7
    elif salario<=1500:
        aumento="4%"
        nsalario=salario+(salario/100)*4
else:
    print("Valor inválido para o salário.")
print(nome)
print("Porcentagem de aumento:", aumento)
print("Salário atual:", '%.2f' %salario)
print("Novo salário:", '%.2f' %nsalario)
