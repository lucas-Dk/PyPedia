import wikipedia
import os
print("""
██████╗ ██╗   ██╗██████╗ ███████╗██████╗ ██╗ █████╗ 
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗
██████╔╝ ╚████╔╝ ██████╔╝█████╗  ██║  ██║██║███████║
██╔═══╝   ╚██╔╝  ██╔═══╝ ██╔══╝  ██║  ██║██║██╔══██║
██║        ██║   ██║     ███████╗██████╔╝██║██║  ██║
╚═╝        ╚═╝   ╚═╝     ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝
\033[m""")
search = str(input("Tema a ser buscado: ")).lower()
language = wikipedia.set_lang("pt")
search_1 = wikipedia.summary(search)

print(search_1)

print("""
Digite P para fazer mas uma pesquisa

S ou Enter para voltar ao menu ou N para sair:
    """)
voltar = str(input("Escolha: ")).upper()
while voltar.strip() not in "P" and voltar.strip() not in "S" and voltar.strip() not in "N":
  voltar = str(input("Escolha: ")).upper()
if voltar == "P":
  save = str(input("Para salvar sua pesquisa digite S, para não salvar, digite N: ")).upper()
  if save == "S":
    print("Salvando...")
    time.sleep(0.4)
    savearq.adicionar(arq=arquivo,pesquisa=search,dados=search_1)
    print("Pesquisa salva!")
    print("Voltando ao menu...")
    time.sleep(1)
    os.system("clear")
  elif save == "N":
    print("Voltando para o menu...")
    time.sleep(1)
    os.system("clear")
elif voltar == "S" or voltar == "":
  print("Voltando...")
  time.sleep(1)
  os.system("clear")
  break
elif voltar == "N":
  print("Saindo...")
  time.sleep(1)
  sys.exit()
elif user_choice == "5" or user_choice == "05":
os.system("clear")
print("""\033[94m
