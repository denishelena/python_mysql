import MySQLdb


def conexaoBanco():
    BANCO = "DBestoque"
    USER = "root"
    PASSWD = "root"
    HOST = "10.105.54.173"

    try:
        con = MySQLdb.connect(db=BANCO, user=USER, passwd=PASSWD, host=HOST)
        print("Conseguiu conectar ao banco de dados")
    except MySQLdb as erro:
        print("Nao conectou ao banco de dados verifique os dados:", erro)
        menu()
    return con


def cadastro(con):
    print("Digite o nome: \n")
    nome = input("Nome:")
    fone = input("Fone:")
    email = input("Email:")
    cursor = con.cursor()
    sql = "insert into pessoa (pesnome,pesfone,pesmail) values ('" + nome + "','" + fone + "','" + email + "')"
    # print(sql)
    try:
        cursor.execute(sql)
        con.commit()
        print("Dados gravados com sucesso")
    except MySQLdb as erro:
        print("Erro ao cadastrar item no banco", erro)
    con.close()
    menu()


def listaTodos(con):
    cursor = con.cursor()
    sql = "select * from pessoa"
    try:
        cursor.execute(sql)
        dadosPessoa = cursor.fetchall()
        print("Dados lidos com sucesso")
        for dados in dadosPessoa:
            codigo = dados[0]
            nome = dados[1]
            email = dados[2]
            fone = dados[3]
            print("------Lista de Pessoas-----------")
            print("Codigo=%d, Nome=%s, Email=%s, Fone=%s" % (codigo, nome, email, fone))
    except MySQLdb as erro:
        print("Erro ao listar item no banco", erro)
    con.close()
    menu()


def excluir(con):
    print("Digite o codigo: \n")
    codigo = input("Codigo:")
    cursor = con.cursor()
    sql = "delete from pessoa where pesCodigo =" + codigo
    try:
        cursor.execute(sql)
        con.commit()
        print("Dados excluidos com sucesso")
    except MySQLdb as erro:
        print("Erro ao deletar item no banco", erro)
    con.close()
    menu()


def alterar(con):
    print("Digite o codigo: \n")
    codigo = input("Codigo:")
    nome = input("Nome:")
    cursor = con.cursor()
    sql = "update pessoa set pesNome='" + nome + "' where pesCodigo =" + codigo
    try:
        cursor.execute(sql)
        con.commit()
        print("Dados alterados com sucesso")
    except MySQLdb as erro:
        print("Erro ao alterar item no banco", erro)
    con.close()
    menu()


def pesquisar(con):
    print("Digite o nome: \n")
    nome = input("Nome:")
    cursor = con.cursor()
    sql = "select * from pessoa where pesNome like '%" + nome + "%'"
    try:
        cursor.execute(sql)
        dadosPessoa = cursor.fetchall()
        print("Dados listado com sucesso")
        for dados in dadosPessoa:
            codigo = dados[0]
            nome = dados[1]
            fone = dados[2]
            email = dados[3]
            print("Codigo=%d, Nome=%s, Email=%s, Fone=%s" % (codigo, nome, fone, email))
    except MySQLdb as erro:
        print("Erro ao listar item no banco", erro)
    con.close()
    menu()


def menu():
    opcaoEscolha = int(input(
        "Escolha uma opcao:\n\n1)Cadastrar\n2)Alterar\n3)Pesquisar\n4)Excluir\n5)Listar todos\n6)Sair\n\nOpcao\n "))
    try:
        if opcaoEscolha < 1 or opcaoEscolha > 6:
            print("Opcao invalida, escolha entre 1 e 6")
            menu()
    except:
        print("Opcao invalida escolha entra 1 e 6")
        menu()

    if opcaoEscolha == 1:
        con = conexaoBanco()
        cadastro(con)

    if opcaoEscolha == 5:
        con = conexaoBanco()
        listaTodos(con)

    if opcaoEscolha == 4:
        con = conexaoBanco()
        excluir(con)

    if opcaoEscolha == 3:
        con = conexaoBanco()
        pesquisar(con)

    if opcaoEscolha == 2:
        con = conexaoBanco()
        alterar(con)

    if opcaoEscolha == 6:
        exit()


menu()
