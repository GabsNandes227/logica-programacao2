#!/usr/bin/env python3

# ==========================================
# CALCULADORA SIMPLES EM PYTHON
# ==========================================
#
# Autor: Gabriel Fernandes
#
# Este programa realiza operações matemáticas
# básicas:
# - Soma
# - Subtração
# - Multiplicação
# - Divisão
#
# Como executar:
# python calculadora.py
#
# ==========================================

print("=== CALCULADORA SIMPLES ===")

# Solicita os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\nEscolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção desejada: ")

# Verifica qual operação foi escolhida
if opcao == "1":
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")

elif opcao == "2":
    resultado = numero1 - numero2
    print(f"Resultado: {resultado}")

elif opcao == "3":
    resultado = numero1 * numero2
    print(f"Resultado: {resultado}")

elif opcao == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: divisão por zero.")

else:
    print("Opção inválida.")