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

             V 2.0\033[m
 
\033[1;94mby: Lucas Silva (lucas-DK)             \033[m
--------------------------------------------
\033[1;31m[\033[m\033[1;32m1\033[m\033[1;31m]\033[m - Fazer uma pesquisa
\033[1;31m[\033[m\033[1;32m2\033[m\033[1;31m]\033[m - Ler todas as pesquisas salvas
\033[1;31m[\033[m\033[1;32mx\033[m\033[1;31m]\033[m - Sair
""")
			choice = input("Faça sua escolha: ")
			if choice.isnumeric():
				choice = int(choice)
				if choice == 1:
					while True:
						pesquisa = input("Sobre o que deseja pesquisar: ").lower()
						if pesquisa:
							
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
								print("Para fazer uma nova busca: Y ou Enter")
								print("Para retornar ao menu: R")
								print("Para sair do programa: S\n")
							nova_busca = str(input(">>>> ")).upper()
							while nova_busca.strip() not in "Y" and nova_busca.strip() not in "R" and nova_busca not in "S":
								nova_busca = str(input(">>>> ")).upper()
							if nova_busca == "" or nova_busca == "Y":
								print("Voltando...")
								time.sleep(0.6)
								os.system("clear")
				
							elif nova_busca == "R":
								print("Voltando...")
								os.system("clear")
								time.sleep(1)
								break
							elif nova_busca == "S":
								print("Saindo...")
								time.sleep(1)
								sys.exit()
				elif choice == 2:
					savefiles.leitura(arquivo)
					back = input("\nEnter para voltar ao menu ou X/qualquer coisa para sair... ")
					if back == "X" or back == "x" or back != "":
						print("Saindo...")
						time.sleep(1)
						sys.exit()
					if back == "":
						os.system("clear")

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
