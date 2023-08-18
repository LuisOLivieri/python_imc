#Primeiro projeto - Python (IMC): Roteiro Aula Prática

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (pow(altura, 2))

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Voce está abaixo do peso!")
elif 18.5 <= imc < 24.9:
    print("Você está no peso normal!")
elif 25 <= imc < 30:
    print("Você está em sobrepeso!")
elif 30 <= imc < 35:
    print("Você está em Obesidade Grau I!")
elif 35 <= imc < 39.9:
    print("Você está em Obesidade Grau II!")
else:
    print("Você está em Obseidade Grau III ou Mórbido!!!")


