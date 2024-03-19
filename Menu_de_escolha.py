'''Crie um programa que sera uma calculadora. Nesta calculadora você deverá ter um módulo para as operações matemáticas
o arquivo principal deverá conter apenas um menu de escolha para o usuário (soma, subtração, multiplicação e divisão)'''

import Operacoes


def mostrar_menu():
    print('Escolha uma opcao:')
    print('1. Soma')
    print('2. subtracao')
    print('3. multiplicacao')
    print('4. divisao')
    print('5. sair')


def menu():
    while True:
        mostrar_menu()
        escolha = input('Digite o numero da opçao desejada: ')

        if escolha == '1':
            num1 = float(input('Digite um número: '))
            num2 = float(input('Digite outro número: '))
            print('A soma é: ', Operacoes.soma(num1, num2))
        elif escolha == '2':
            num3 = float(input('Digite uma numero: '))
            num4 = float(input('Digite outro numero: '))
            print('A subtração dos numeros é: ',
                  Operacoes.subtracao(num3, num4))

        elif escolha == '3':
            num5 = float(input('Digite um numero: '))
            num6 = float(input('Digite outro numero: '))
            print('A multiplicação dos números é: ',
                  Operacoes.multiplicacao(num5, num6))

        elif escolha == '4':
            num7 = float(input('Digite um numero: '))
            num8 = float(input('Digite outro numero: '))
            print('A divisão dos numeros é: ', Operacoes.divisao(num7, num8))

        elif escolha == '5':
            print('Saindo da calculadora...')
            break

        else:
            print('Opcao inválida. Por favor, escolha novamente.')


menu()
