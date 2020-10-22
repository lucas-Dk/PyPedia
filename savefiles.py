# Modularização do PyPédia

def existe(nome):
	try:
		file = open(nome, 'rt')
	except:
		print("Arquivo não existe!")
	else:
		print('Aquivo já existe!')
		file.close()

def criar(nome):
	try:
		file = open(nome, 'wt+')
	except:
		print("impossível criar arquivo!")
	else:
		print("Arquivo criado!")
		file.close()
def adicionar(nome, pesquisa):
	try:
		file = open(nome, 'at')
	except:
		print("impossível adicionar a pesquisa ao arquivo!")
	else:
		try:
			file.write("\nPesquisa:\n\n{} \n".format(pesquisa))
		except:
			print("Pesquisa não adicionada")
			file.close()
		else:
			pass

