
x=1

while x==1:	
	pergunta=input('---------------------------------\nQual operação você deseja fazer?\n---------------------------------\nDigite:\n[a] para adição [d] para divisão\n[m] para multiplicação [s] para subtração\n---------------------------------\n:')
	if	pergunta=='a':
			valor1=int(input('Digite o 1º que você deseja somar.\n:'))
			valor2=int(input('Digite o 2º que você deseja somar.\n:'))
			print('Resultado: ', valor1+valor2)
			pergunta2=input('---------------------------------\nDeseja fazer outra operãção?\n---------------------------------\nDigite[s] para sim [n] para não.\n:')
			if pergunta2=='s':
				x=1
			elif pergunta2=='n':
				x=2
				print('Obrigado por testar este programa :D\nMe siga no GitHub para me incentivar nessa jornada de aprendizado\n\nhttps://github.com/oficialjeffs\n\nSempre colocarei novas atualizações. :D')	
			else:
				print('Digite Valores válidos')	
	elif pergunta=='d':
			valor1=int(input('Digite o 1º que você deseja dividir.\n:'))
			valor2=int(input('Digite o 2º que você deseja dividir.\n:'))
			print('Resultado: ', valor1/valor2)
			pergunta2=input('---------------------------------\nDeseja fazer outra operãção?\n---------------------------------\nDigite[s] para sim [n] para não.\n:')
			if pergunta2=='s':
				x=1
			elif pergunta2=='n':
				x=2
				print('Obrigado por testar este programa :D\nMe siga no GitHub para me incentivar nessa jornada de aprendizado\n\nhttps://github.com/oficialjeffs\n\nSempre colocarei novas atualizações. :D')
			else:
				print('Digite Valores válidos')
	elif pergunta=='m':
			valor1=int(input('Digite o 1º que você deseja multiplicar.\n:'))
			valor2=int(input('Digite o 2º que você deseja multiplicar.\n:'))
			print('Resultado: ', valor1*valor2)
			pergunta2=input('---------------------------------\nDeseja fazer outra operãção?\n---------------------------------\nDigite[s] para sim [n] para não.\n:')
			if pergunta2=='s':
				x=1
			elif pergunta2=='n':
				x=2
				print('Obrigado por testar este programa :D\nMe siga no GitHub para me incentivar nessa jornada de aprendizado\n\nhttps://github.com/oficialjeffs\n\nSempre colocarei novas atualizações. :D')
			else:
				print('Digite Valores válidos')
	elif pergunta=='s':
			valor1=int(input('Digite o 1º que você deseja subtrair.\n:'))
			valor2=int(input('Digite o 2º que você deseja subtrair.\n'))
			print('Resultado: ', valor1-valor2)
			pergunta2=input('---------------------------------\nDeseja fazer outra operãção?\n---------------------------------\nDigite[s] para sim [n] para não.\n:')
			if pergunta2=='s':
				x=1
			elif pergunta2=='n':
				x=2
				print('Obrigado por testar este programa :D\nMe siga no GitHub para me incentivar nessa jornada de aprendizado\n\nhttps://github.com/oficialjeffs\n\nSempre colocarei novas atualizações. :D')
			else:
				print('Digite Valores válidos')
	else: 
		print('Digite Valores válidos')


