# Modularização do PyPédia

def existe(nome):
	try:
		file = open(nome, 'rt')
	except:
		print("Arquivo não existe!")
	else:
		return True
		file.close()

def criar(nome):
	try:
		file = open(nome, 'wt+')
	except:
		print("impossível criar arquivo!")
	else:
		print("Arquivo criado!")
		file.close()
def adicionar(nome, titulo_pesquisa, pesquisa):
	try:
		file = open(nome, 'at')
	except:
		print("impossível adicionar a pesquisa ao arquivo!")
	else:
		try:
			file.write("\nPesquisa sobre {}:\n{} \n".format(titulo_pesquisa, pesquisa))
		except:
			print("Pesquisa não adicionada")
			file.close()
		else:
			pass
def leitura(nome):
  try:
    file = open(nome)
  except:
    print("Erro ao abrir o arquivo!")
  else:
    try:
      ler = file.readlines()
    except:
      print("Impossível ler o arquivo!")
    else:
      for x in ler:
        print(x)
      

    
