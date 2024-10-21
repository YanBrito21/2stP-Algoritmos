#Divisão:

try:
    num1= float(input("Digite um numero: "))
    num2= float(input("Digite um numero: "))
    result= num1 / num2

except ZeroDivisionError:
    print("Erro: Divisão por zero. Não é possível dividir por zero.")
except ValueError:
    print("Erro: Valor inválido. Certifique-se de digitar um número válido.")


#Capturando exceções múltiplas:

try: 
    cores = {
    'vermelho': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul':(0, 0, 255)
    }
    cor = str(input("Digite a cor que deseja saber o codigo: "))
    result = cores[cor]
    print(result)

except KeyError:
    print("Erro: Chave inválida.")
except Exception as keyer:
    print(keyer)


# Bloco else e finally:

try:
    num = float(input("Digite um numero: "))
    if num > 10:
        print("Numero valido!")
    else:
        raise ValueError ("O programa foi executado com sucesso!")

except ValueError as e:
    print(e)
finally:
    print("Programa encerrado.")


# Exceções personalizadas:

import string
 
try:
    senha = input("digite a senha: ")
    def verif_senha(senha):
        if len(senha) >=8:
            num = [num for num in string.digits if num in senha]
            if num:
                print("A Senha é valida.")
            else:
                print("A senha tem o tamanho recomendado, porem não possui numeros.")
        else:
            print("A Senha é muito curta.")    
                
    verif_senha(senha)
    
except TypeError:
    print("Verifique se a variavel 'senha' foi informada na chamada da função '( )'.")
except Exception as error:
    print(error)

# Simulação de transações:

try:
    
    def transfer_bank(saldo, valor):
        result = saldo - valor
        if result < 0:
            raise ValueError ("Saldo insuficiente")
        else:
            print("Transferencia concluida.")
            
    saldo = float(input("Informe o saldo da conta: "))
    valor = float(input("Informe o valor da transferência: ")) 
    
    transfer_bank(saldo, valor)
    
except ValueError as e:
    print(e)
finally:
    print("Programa encerrado.")
    

