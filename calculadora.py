#Complete as funcoes a seguir

while True:
	def soma(a , b):
		#Insira o código aqui
		print(" a + b = ", a+b)

	def subtrai(a , b):
		#Insira o código aqui
		print("a - b = ", a-b)

	def multiplica(a , b):
		#Insira o código aqui

		print("a * b = " , a*b)

	def divide(a , b):
		#Insira o código aqui
		if(b != 0):
			print("a / b = " , a/b)
		else:
			print("Não é possível fazer esta operação, 'b' tem que ser diferente de 0 !")
		
	#Programa principal

	print("Calculadora simples")

	num1 = float(input("Insira o primeiro numero: "))
	num2 = float(input("Insira o segundo numero: "))

	soma(num1, num2)
	subtrai(num1, num2)
	multiplica(num1, num2)
	divide(num1, num2)


