import os
import sqlite3
from sqlite3 import Error
from colorama import Fore
from time import sleep
import tkinter



########## cria conexão
def bancoConex():
    caminho = "/storage/emulated/0/Python/cursoCFB/SQL/agenda.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con


vcon = bancoConex()


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print(f"{Fore.GREEN}operação realizada com sucesso{Fore.RESET}")
        conexao.close()


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    # conexao.close()
    return res


####### MENU PRINCIPAL

def menuMain():
    os.system('clear')
    print("=" * 19)
    print(f"{Fore.GREEN}### A G E N D A ###{Fore.RESET}")
    print("=" * 19)
    print("[1] INSERIR")
    print("[2] EXCLUIR")
    print("[3] ALTERAR")
    print("[4] CONSULRAR TODOS")
    print("[5] CONSULTAR POR NOME")
    print("[6] SAIR")
    print("=" * 18)


def menuInserir():
    os.system('clear')
    nome = input("Digite o nome >> ")
    tel = input("Digite o telefone >> ")
    email = input("Digite o email >> ")
    vsql = f"""INSERT INTO tb_contatos(
	T_NOMECONTATO,
	T_TELEFONECONTATO,
	T_EMAILCONTATO
	) VALUES('{nome}', '{tel}', '{email}')
	 """
    query(vcon, vsql)


def menuExcluir():
    os.system('clear')
    vid = int(input("Digite o ID que deseja excluir >> "))
    vsql = f"""DELETE FROM tb_contatos
	WHERE N_IDCONTATO = '{vid}'
	"""
    query(vcon, vsql)


def menuAlterar():
    os.system('clear')
    vid = int(input("Digite o ID do contato que deseja alterar  >> "))
    r = consultar(vcon, f"SELECT * FROM tb_contatos WHERE N_IDCONTATO = {vid}")
    if r == []:
        os.system('clear')
        print(f"{Fore.RED}ID não existe{Fore.RESET}")
        sleep(2)
        menuAlterar()
    rnome = r[0][1]
    rtel = r[0][2]
    remail = r[0][3]
    nome = input("Digite o nome >> ")
    tel = input("Digite o telefone >> ")
    email = input("Digite o email >> ")
    if len(nome) == 0:
        nome = rnome
    if len(tel) == 0:
        tel = rtel
    if len(email) == 0:
        email = remail
    vsql = f"""UPDATE tb_contatos SET 
	T_NOMECONTATO = '{nome}',
	T_TELEFONECONTATO = '{tel}',
	T_EMAILCONTATO = '{email}'
	WHERE N_IDCONTATO = '{vid}'
	    """
    query(vcon, vsql)


def menuConsultaId():
    vsql = "SELECT * FROM tb_contatos"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    print("\n")
    print("=" * 54)
    print("ID |          NOMES      |      TELEFONES   ")
    print("=" * 54)
    for r in res:
        print("{0: <3}|     {1: <15} |    {2: <14}".format(r[0], r[1], r[2]))
        print("-" * 54)
        vcont += 1
        if vcont >= vlim:
            break

    continua = input("Pressione qualquer tecla para voltar ao menu >> ")


def menuConsultaNome():
    nome = input("Digite um nome >> ")
    vsql = f"""SELECT * FROM tb_contatos
	WHERE T_NOMECONTATO LIKE '%{nome}%'
	"""

    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    print("\n")
    print("=" * 54)
    print("ID |          NOMES      |      TELEFONES   ")
    print("=" * 54)
    for r in res:
        print("{0: <3}|     {1: <15} |    {2: <14}".format(r[0], r[1], r[2]))
        print("-" * 54)
        vcont += 1
        if vcont >= vlim:
            break

    continua = input("Pressione qualquer tecla para voltar ao menu >> ")


opcao = 0
while opcao != 6:
    menuMain()
    opcao = int(input("Digite uma opção >> "))
    if opcao == 1:
        menuInserir()
        sleep(2)
    elif opcao == 2:
        menuExcluir()
        sleep(2)
    elif opcao == 3:
        menuAlterar()
        sleep(2)
    elif opcao == 4:
        menuConsultaId()
    elif opcao == 5:
        menuConsultaNome()
    elif opcao == 6:
        print("função de finalizar programa...")
        sleep(2)
        os.system('clear')
        print("=" * 20)
        print("     Feito por\n")
        print("  Kaique Miranda ©")
        print("=" * 20)
    else:
        os.system('cls')
        print(f"{Fore.RED}Opção inválida {Fore.RESET}")
        sleep(2)

# menuMain()

vcon.close()

