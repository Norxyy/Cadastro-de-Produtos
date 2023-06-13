prodList = list()
prodCodigo = int(0)

# cadastro de Produto.
def cadastrarProduto(prodCodigo):
    print('Cadastro de Produtos:')
    print(f'Código do Produto: {prodCodigo}')
    nomeProd = input('Digite o NOME do produto: ').upper()
    fabProduto = input('Digite a FABRICANTE do produto: ').upper()
    valorProduto = float(input('Digite o VALOR do produto: R$'))
    prodservi = dict({
        'prodCodigo': prodCodigo,
        'nomeProd': nomeProd,
        'fabProduto': fabProduto,
        'valorProduto': valorProduto
    })
    prodList.append(prodservi.copy())

# fazer a consulta do seu produto.
def consultarProduto():
    while (True):
        try:
            print('Consulta de Produtos:')
            opc = validaInt(
            'Consultar Produto(s).\n'
            '1. Consultar todos os Produtos.\n'
            '2. Consultar Produto por CÓDIGO.\n'
            '3. Consultar Produto(s) por FABRICANTE.\n'
            '4. Retornar.\n> ',1,4
            )
            if ((opc) == (int(1))):
                print('Consultando todos os Produtos!')
                for (prod) in (prodList):
                    for (chave, valor) in (prod.items()):
                        print(f'{chave}: {valor}')
            elif ((opc) == (int(2))):
                while (True):
                    try:
                        print('Consultando Código dos Produtos.')
                        entry = int(input('Digite o Código:\n> '))
                        for (prod) in (prodList):
                            if (prod['prodCodigo'] == (entry)):
                                for (chave, valor) in (prod.items()):
                                    print(f'{chave}: {valor}')
                                return
                    except:
                        print('Error desconhecido.')
                        continue
                    print('Código do Produto não localizado.')
                    return
            elif ((opc) == (int(3))):
                while (True):
                    try:
                        print('Consultando Produto por FABRICANTE.')
                        entry = input('Informe o Fabricante do Produto:\n> ').upper()
                        for (prod) in (prodList):
                            if (prod['fabricanteProd'] == (entry)):
                                for (chave, valor) in (prod.items()):
                                    print(f'{chave}: {valor}')
                        return
                    except:
                        print('Error desconhecido.')
                        continue
            else:
                return
        except:
            print('Error desconhecido.')
            continue

# remoção de produtos indesejados.
def removerProduto():
    print('Exclusão de Produtos:')
    while (True):
        try:
            print('Excluíndo por CÓDIGO.')
            entry = int(input('Informe o Código:\n> '))
            for (prod) in (prodList):
                if (prod['prodCodigo'] == (entry)):
                    prodList.remove(prod)
                    return
        except:
            print('Error desconhecido.')
            continue
        print('Código não localizado.')
        return

# validar entrada.
def validaInt(q, min, max):
    x = int(input(q))
    while (((x) < (min)) or ((x) > (max))):
        x = int(input(q))
    return x


# Identificação.
def identificacao():
    ident = 'Murilo Vergara'
    print(f'Olá seja bem-vindo ao Estoque de controle do {ident}.')


# Codigo principal.
identificacao()
while (True):
    try:
        op = int(validaInt(
            'Digite a opção desejada.\n'
            '1. Cadastro\n'
            '2. Filtro\n'
            '3. Exclusão\n'
            '4. Sair\n> ', 1, 4
        ))
        if ((op) == (int(1))):
            prodCodigo += 1
            cadastrarProduto(prodCodigo)
        elif ((op) == (int(2))):
            consultarProduto()
        elif ((op) == (int(3))):
            removerProduto()
        else:
            break
    except:
        print('Error desconhecido.')
        continue
