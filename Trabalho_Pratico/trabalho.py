import csv
from operator import itemgetter

def carregar_usuarios():
    usuarios = {}
    with open('usuarios.csv', mode='r', newline='') as arquivo:
        reader = csv.DictReader(arquivo)
        for linha in reader:
            usuarios[linha['ID']] = {
                'nome': linha['Nome'],
                'senha': linha['Senha'],
                'tipo': linha['Tipo']
            }
    return usuarios

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as arquivo:
        fieldnames = ['ID', 'Nome', 'Senha', 'Tipo']
        writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
        writer.writeheader()
        for id_usuario, dados in usuarios.items():
            writer.writerow({
                'ID': id_usuario,
                'Nome': dados['nome'],
                'Senha': dados['senha'],
                'Tipo': dados['tipo']
            })

def adicionar_usuario():
    usuarios = carregar_usuarios()
    novo_id = str(len(usuarios) + 1)
    nome = input("Digite o nome do novo usuário: ")
    senha = input("Digite a senha do novo usuário: ")
    tipo = input("Digite o tipo do novo usuário (admin, funcionario, cliente): ")
    usuarios[novo_id] = {'nome': nome, 'senha': senha, 'tipo': tipo}
    salvar_usuarios(usuarios)
    print(f"Usuário '{nome}' cadastrado com sucesso!")

def listar_usuarios():
    usuarios = carregar_usuarios()
    print("\nLista de Usuários:")
    for id_usuario, dados in usuarios.items():
        print(f"ID: {id_usuario}, Nome: {dados['nome']}, Tipo: {dados['tipo']}")

def buscar_usuario():
    usuarios = carregar_usuarios()
    id_usuario = input("Digite o ID do usuário que deseja buscar: ")
    if id_usuario in usuarios:
        print(f"Usuário encontrado:")
        print(f"ID: {id_usuario}, Nome: {usuarios[id_usuario]['nome']}, Tipo: {usuarios[id_usuario]['tipo']}")
    else:
        print("Usuário não encontrado.")

def atualizar_usuario():
    usuarios = carregar_usuarios()
    id_usuario = input("Digite o ID do usuário que deseja atualizar: ")
    if id_usuario in usuarios:
        print(f"Usuário encontrado:")
        print(f"ID: {id_usuario}, Nome: {usuarios[id_usuario]['nome']}, Tipo: {usuarios[id_usuario]['tipo']}")
        novo_nome = input("Digite o novo nome (ou deixe em branco para manter): ")
        nova_senha = input("Digite a nova senha (ou deixe em branco para manter): ")
        novo_tipo = input("Digite o novo tipo (admin, funcionario, cliente) (ou deixe em branco para manter): ")

        if novo_nome:
            usuarios[id_usuario]['nome'] = novo_nome
        if nova_senha:
            usuarios[id_usuario]['senha'] = nova_senha
        if novo_tipo:
            usuarios[id_usuario]['tipo'] = novo_tipo

        salvar_usuarios(usuarios)
        print(f"Dados do usuário '{usuarios[id_usuario]['nome']}' atualizados com sucesso!")
    else:
        print("Usuário não encontrado.")

def excluir_usuario():
    usuarios = carregar_usuarios()
    id_usuario = input("Digite o ID do usuário que deseja excluir: ")
    if id_usuario in usuarios:
        nome_usuario = usuarios[id_usuario]['nome']
        del usuarios[id_usuario]
        salvar_usuarios(usuarios)
        print(f"Usuário '{nome_usuario}' excluído com sucesso!")
    else:
        print("Usuário não encontrado.")

def carregar_produtos():
    produtos = []
    with open('produtos.csv', mode='r', newline='') as arquivo:
        reader = csv.DictReader(arquivo)
        for linha in reader:
            produtos.append({
                'codigo': linha['Codigo'],
                'nome': linha['Nome'],
                'preco': float(linha['Preco']),
                'quantidade': int(linha['Quantidade'])
            })
    return produtos

def salvar_produtos(produtos):
    with open('produtos.csv', mode='w', newline='') as arquivo:
        fieldnames = ['Codigo', 'Nome', 'Preco', 'Quantidade']
        writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow({
                'Codigo': produto['codigo'],
                'Nome': produto['nome'],
                'Preco': produto['preco'],
                'Quantidade': produto['quantidade']
            })

def adicionar_produto(usuario_tipo):
    if usuario_tipo == 'admin' or usuario_tipo == 'funcionario':
        produtos = carregar_produtos()
        novo_codigo = input("Digite o código do novo produto: ")
        nome = input("Digite o nome do novo produto: ")
        preco = float(input("Digite o preço do novo produto: "))
        quantidade = int(input("Digite a quantidade do novo produto: "))
        produtos.append({
            'codigo': novo_codigo,
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        })
        salvar_produtos(produtos)
        print(f"Produto '{nome}' cadastrado com sucesso!")
    else:
        print("Você não tem permissão para adicionar produtos.")

def listar_produtos():
    produtos = carregar_produtos()
    print("\nLista de Produtos:")
    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def buscar_produto():
    produtos = carregar_produtos()
    codigo_produto = input("Digite o código do produto que deseja buscar: ")
    for produto in produtos:
        if produto['codigo'] == codigo_produto:
            print(f"Produto encontrado:")
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")
            return
    print("Produto não encontrado.")

def atualizar_produto(usuario_tipo):
    if usuario_tipo == 'admin':
        produtos = carregar_produtos()
        codigo_produto = input("Digite o código do produto que deseja atualizar: ")
        index_produto = None
        for i, produto in enumerate(produtos):
            if produto['codigo'] == codigo_produto:
                index_produto = i
                break

        if index_produto is not None:
            print(f"Produto encontrado:")
            print(f"Código: {produtos[index_produto]['codigo']}, Nome: {produtos[index_produto]['nome']}, "
                  f"Preço: R${produtos[index_produto]['preco']:.2f}, Quantidade: {produtos[index_produto]['quantidade']}")

            novo_nome = input("Digite o novo nome (ou deixe em branco para manter): ")
            novo_preco = float(input("Digite o novo preço (ou deixe em branco para manter): "))
            nova_quantidade = int(input("Digite a nova quantidade (ou deixe em branco para manter): "))

            if novo_nome:
                produtos[index_produto]['nome'] = novo_nome
            if novo_preco:
                produtos[index_produto]['preco'] = novo_preco
            if nova_quantidade:
                produtos[index_produto]['quantidade'] = nova_quantidade

            salvar_produtos(produtos)
            print(f"Dados do produto '{produtos[index_produto]['nome']}' atualizados com sucesso!")
        else:
            print("Produto não encontrado.")
    else:
        print("Você não tem permissão para atualizar produtos.")

def excluir_produto(usuario_tipo):
    if usuario_tipo == 'admin':
        produtos = carregar_produtos()
        codigo_produto = input("Digite o código do produto que deseja excluir: ")
        index_produto = None
        for i, produto in enumerate(produtos):
            if produto['codigo'] == codigo_produto:
                index_produto = i
                break

        if index_produto is not None:
            nome_produto = produtos[index_produto]['nome']
            del produtos[index_produto]
            salvar_produtos(produtos)
            print(f"Produto '{nome_produto}' excluído com sucesso!")
        else:
            print("Produto não encontrado.")
    else:
        print("Você não tem permissão para excluir produtos.")

def imprimir_produtos_ordenados_por_nome():
    produtos = carregar_produtos()
    produtos_ordenados = sorted(produtos, key=itemgetter('nome'))
    print("\nProdutos ordenados por nome:")
    for produto in produtos_ordenados:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def imprimir_produtos_ordenados_por_preco():
    produtos = carregar_produtos()
    produtos_ordenados = sorted(produtos, key=itemgetter('preco'))
    print("\nProdutos ordenados por preço:")
    for produto in produtos_ordenados:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def main():
    print("\n### Sistema de Gerenciamento ###\n")

    while True:
        print("Escolha uma opção:")
        print("1 - Entrar com um usuário existente")
        print("2 - Adicionar um novo usuário")
        print("0 - Sair")

        opcao_inicio = input("\nDigite o número da opção desejada: ")

        if opcao_inicio == '1':
            usuarios = carregar_usuarios()
            usuario_autenticado = False
            usuario_tipo = None

            while not usuario_autenticado:
                nome_usuario = input("Digite seu nome de usuário: ")
                senha_usuario = input("Digite sua senha: ")

                for id_usuario, dados in usuarios.items():
                    if dados['nome'] == nome_usuario and dados['senha'] == senha_usuario:
                        usuario_autenticado = True
                        usuario_tipo = dados['tipo']
                        print(f"\nBem-vindo, {nome_usuario} ({usuario_tipo})!\n")
                        break

                if not usuario_autenticado:
                    print("Nome de usuário ou senha incorretos. Tente novamente.\n")

            while True:
                if usuario_tipo == 'admin':
                    print("Opções disponíveis:")
                    print("1 - Adicionar usuário")
                    print("2 - Listar usuários")
                    print("3 - Buscar usuário")
                    print("4 - Atualizar usuário")
                    print("5 - Excluir usuário")
                    print("6 - Adicionar produto")
                    print("7 - Listar produtos")
                    print("8 - Buscar produto")
                    print("9 - Atualizar produto")
                    print("10 - Excluir produto")
                    print("11 - Imprimir produtos ordenados por nome")
                    print("12 - Imprimir produtos ordenados por preço")
                    print("0 - Sair")
                elif usuario_tipo == 'funcionario':
                    print("Opções disponíveis:")
                    print("1 - Listar produtos")
                    print("2 - Buscar produto")
                    print("3 - Imprimir produtos ordenados por nome")
                    print("4 - Imprimir produtos ordenados por preço")
                    print("0 - Sair")
                elif usuario_tipo == 'cliente':
                    print("Opções disponíveis:")
                    print("1 - Listar produtos")
                    print("2 - Buscar produto")
                    print("3 - Sair")

                opcao = input("\nDigite o número da opção desejada: ")

                if opcao == '1' and usuario_tipo == 'admin':
                    adicionar_usuario()
                elif opcao == '2' and (usuario_tipo == 'admin' or usuario_tipo == 'funcionario' or usuario_tipo == 'cliente'):
                    listar_usuarios()
                elif opcao == '3' and (usuario_tipo == 'admin' or usuario_tipo == 'funcionario' or usuario_tipo == 'cliente'):
                    buscar_usuario()
                elif opcao == '4' and usuario_tipo == 'admin':
                    atualizar_usuario()
                elif opcao == '5' and usuario_tipo == 'admin':
                    excluir_usuario()
                elif opcao == '6' and (usuario_tipo == 'admin' or usuario_tipo == 'funcionario'):
                    adicionar_produto(usuario_tipo)
                elif opcao == '7' and (usuario_tipo == 'admin' or usuario_tipo == 'funcionario' or usuario_tipo == 'cliente'):
                    listar_produtos()
                elif opcao == '8' and (usuario_tipo == 'admin' or usuario_tipo == 'funcionario' or usuario_tipo == 'cliente'):
                    buscar_produto()
                elif opcao == '9' and usuario_tipo == 'admin':
                    atualizar_produto(usuario_tipo)
                elif opcao == '10' and usuario_tipo == 'admin':
                    excluir_produto(usuario_tipo)
                elif opcao == '11' and usuario_tipo == 'admin':
                    imprimir_produtos_ordenados_por_nome()
                elif opcao == '12' and usuario_tipo == 'admin':
                    imprimir_produtos_ordenados_por_preco()
                elif opcao == '0':
                    print("Saindo do programa.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

                input("\nPressione Enter para continuar...")

        elif opcao_inicio == '2':
            adicionar_usuario()
        elif opcao_inicio == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
