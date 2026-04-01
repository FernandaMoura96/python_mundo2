# Essa é uma calculadora de preços condicionada ao metodo de pagamento
compra = float(input("Qual o valor da compra? R$ "))

metodo= print('''Escolha como quer pagar:
[1] À vista no dinheiro
[2] À vista no cartão
[3] Em 2 parcelas
[3] Em 3 ou mais parcelas ''')
opção  = int(input("Qual o método de pagamento?"))

if opção  == 1:
   total = compra - (compra * 10/100)
elif opção == 2:
      total = (compra - (compra * 5/100))
elif  opção == 3:
      total = compra
elif opção == 4 :
      total = compra + (compra * 20/100)
else : print("Opção inválida!")
print(f"O valor a ser total da sua compra é de R$ {total:.2f}  ")


