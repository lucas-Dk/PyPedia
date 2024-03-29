# Arquivo a ser gerado
arquivo = 'Pesquisas.txt'

# Importações
try:
	import wikipedia
	import time
	import os
	import sys
	import savefiles
	import urllib.request
	from tqdm import tqdm
except:
	print("\033[1;31m       :(     ")
	print("Erro ao entrar no arquivo")
	print("Digite > pip install -r requirements.txt")
	print("E tente novamente!\033[m")
else: 
	if not savefiles.existe(arquivo):
		savefiles.criar(arquivo)
		os.system("clear")
	if savefiles.existe == True:
		pass

	try:
		print("Verificando se você está na internet!")
		time.sleep(1.3)
		connection = urllib.request.urlopen("https://www.google.com.br")
	except urllib.error.URLError:
		print("\033[1;31mERROR: VOCÊ NÃO ESTÁ CONECTADO A INTERNET NO MOMENTO :( \033[m")
	else:
		os.system("clear")
		print("\033[1;31mCarregando PyPédia...\033[m")
		for loading in tqdm(range(1, 100 + 1)):
			time.sleep(0.1)
		print("\033[1;32mPyPédia carregado, faça sua busca!\033[m")
		time.sleep(1)
		os.system("clear")
		wikipedia.set_lang("pt")
		while True:
			print("""\033[1;95m
______                          _  _        
| ___ \                        | |(_)       
| |_/ / _   _  _ __    ___   __| | _   __ _ 
|  __/ | | | || '_ \  / _ \ / _` || | / _` |
| |    | |_| || |_) ||  __/| (_| || || (_| |
\_|     \__, || .__/  \___| \__,_||_| \__,_|
         __/ || |                           
        |___/ |_|                          
             V 1.1\033[m
OBS: Ele busca por palavras chaves
exemplo: Você quer buscar por dinossauros
então você digita dinossauros
--------------------------------------------
[1] - Fazer uma pesquisa
[x] - Sair
""")
			choice = input("Faça sua escolha: ")
			if choice.isnumeric():
				choice = int(choice)
				if choice == 1:
					while True:
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
								savefiles.adicionar(nome=arquivo, titulo_pesquisa=pesquisa, pesquisa=busca)
								time.sleep(0.5)
								print("\n\033[1;95mPesquisa adicionada!")
								print("E salva no arquivo Pesquisas.txt\033[m\n")
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
							print("Tente tirar os espaços!")

				else:
					print("Opção inválida!")
					time.sleep(0.7)
					os.system("clear")
			else:
				if choice == "X" or choice == "x":
					print("Saindo...")
					time.sleep(1)
					sys.exit()
				else:
					print("Opção inválida!")
					time.sleep(0.7)
					os.system("clear")
# Fim do script
