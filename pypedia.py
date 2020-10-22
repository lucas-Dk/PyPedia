# Importações 
arquivo = 'Pesquisas.txt'
try:
	import wikipedia
	import time
	import os
	import sys
	import savefiles
	import urllib.request
	from tqdm import tqdm
except:
	print("       :(     ")
	print("Erro ao entrar no arquivo")
	print("Digite > pip install requirements.txt")
	print("E tente novamente!")
else: 
	if not savefiles.existe(arquivo):
		savefiles.criar(arquivo)
		os.system("clear")
	else:
		pass

	try:
		print("Verificando se você está na internet!")
		time.sleep(1.3)
		connection = urllib.request.urlopen("https://www.google.com.br")
	except urllib.error.URLError:
		print("\033[1;31mERROR: VOCÊ NÃO ESTÁ CONECTADO A INTERNET NO MOMENTO :( \033[m")
	else:
		os.system("clear")
		print("Crregando PyPédia...")
		for loading in tqdm(range(1, 100 + 1)):
			time.sleep(0.1)
		print("PyPédia carregado, faça sua busca!")
		time.sleep(1)
		os.system("clear")
		wikipedia.set_lang("pt")
		while True:
			print("========= PyPedia =========")
			print()

			pesquisa = input("Sobre o que deseja pesquisar: ").lower().strip()

			if pesquisa.isalnum():
				print("Iniciando busca...\n")
				time.sleep(0.6)
				try:
					busca = wikipedia.summary(pesquisa)
				except:
					print("Não foi possivel conectar a wikipedia, tente novamente!")
				else:
					print(busca + '\n')
					print("Adicionando sua pesquisa no arquivo Pesquisas.txt...")
					savefiles.adicionar(arquivo, busca)
					time.sleep(0.5)
					print("Pesquisa adicionada!")
				nova_busca = str(input("Deseja fazer uma nova busca? Y ou enter para SIM ou N para NÃO: ")).upper()
				while nova_busca.strip() not in "Y" and nova_busca.strip() not in "N":
					nova_busca = str(input("Deseja fazer uma nova busca? Y ou enter para SIM ou N para NÃO: ")).upper()
				if nova_busca == "" or nova_busca == "Y":
					print("Voltando...")
					time.sleep(0.6)
					os.system("clear")
				
				elif nova_busca == "N":
					print("Saindo...")
					time.sleep(1)
					sys.exit()
			else:
				print("Digite letras, numeros ou os dois juntos!")
