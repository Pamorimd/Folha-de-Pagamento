import sys

funcionarios = []

def tela_inicial():
    print('\n', "-"*90, '\n')
    print(" "*25, 'BEM-VINDO AO MENU DA EMPRESA MARKETING É TUDO')
    print('\n', "-"*90, '\n')



def navegar(tela_atual):
    while True:
        telas[tela_atual]()
        print
        print ('\n', "-"*90, '\n')
        print ('Como podemos ajudar?')
        print ('Inserção de funcionário - digite "1"')
        print ('Remoção de funcionário - digite "2" ')
        print ('Determinar folha de pagamento - digite "3"')
        print ('Relatório com salário bruto e salário líquido de todos os funcionários - digite "4"')
        print ('Funcionário com o maior salário líquido - digite "5"')
        print ('Funcionário com o maior número de faltas - digite "6"')
        print ('Encerrar programa - digite "7"')
        print ('\n', "-"*90, '\n')
        print 
        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            print ('Você está na tela de inserção de funcionário')
            voltar = str(input('Deseja voltar à tela inicial? \n[SIM ou NÃO] \n ')).lower()
            if voltar == 'sim':
                tela_atual = 'inicial'
            elif voltar == 'nao':
                tela_atual = 'inserir'
        elif escolha == 2:
            print ('Você está na tela de remoção de funcionários')
            voltar = str(input('Deseja voltar à tela inicial? \n[SIM ou NÃO] \n ')).lower()
            if voltar == 'sim':
                tela_atual = 'inicial'
            elif voltar == 'nao':
                tela_atual = 'remover'
        elif escolha == 3:
            print ('Você está na tela de determinar a folha de pagamento de um funcionário')
            voltar = str(input('Deseja voltar à tela inicial? \n[SIM ou NÃO] \n ')).lower()
            if voltar == 'sim':
                tela_atual = 'inicial'
            elif voltar == 'nao':
                tela_atual = 'pagamento'
        elif escolha == 4:
            print ('Você está na tela de relatório com salário bruto e salário líquido de todos os funcionários')
            voltar = str(input('Deseja voltar à tela inicial? \n[SIM ou NÃO] \n ')).lower()
            if voltar == 'sim':
                tela_atual = 'inicial'
            elif voltar == 'nao':
                tela_atual = 'relatorio'
        elif escolha == 5:
            print ('Você está na tela com os dados do funcionário com o maior salário líquido')
            voltar = str(input('Deseja voltar à tela inicial? \n[SIM ou NÃO] \n ')).lower()
            if voltar == 'sim':
                tela_atual = 'inicial'
            elif voltar == 'nao':
                tela_atual = 'maior salario'
        elif escolha == 6:
            print ('Você está na tela com os dados do funcionário com o maior número de faltas')
            voltar = str(input('Deseja voltar à tela inicial? \n[SIM ou NÃO] \n ')).lower()
            if voltar == 'sim':
                tela_atual = 'inicial'
            elif voltar == 'nao':
                tela_atual = 'maior faltas'
        elif escolha == 7:
            print ('Você está na tela de encerramento')
            voltar = str(input('Deseja voltar à tela inicial? \n[SIM ou NÃO] \n ')).lower()
            if voltar == 'sim':
                tela_atual = 'inicial'
            elif voltar == 'nao':
                tela_atual = 'encerrar'
        else:
            print("Opção inválida. Por favor, escolha novamente.")


def inserir_funci():
    print ('INSERIR FUNCIONÁRIOS')
    num=1
    while(num>0):
        funcionario={}
        matricula = int(input('Digite o código de matrícula do funcionário: '))
        print ()
        nome_funci = str(input('Digite o nome do funcionário: '))
        print ()
        num_faltas = int(input(f'Digite o número de faltas do mês do(a) funcionário(a) {nome_funci}: '))  
        print()
        cod_funcao = int(input('Digite o código da função \n101 para vendedor \n102 para administrativo \nCódigo: '))
        print()
        if (cod_funcao == 101):
            vendas = int(input(f'Digite o número de vendas feitas pelo(a) funcionário(a) {nome_funci}: '))
            print ()
            salario_fixo101 = 1500
            comissao = 0.09*vendas
            faltas101 = (salario_fixo101/30)*num_faltas
            salario_bruto101 = (salario_fixo101 + comissao) - faltas101 
            salario_liquido101 = 0
            if salario_bruto101 <= 2259.20:
                impostos = 0
                salario_liquido101 = salario_bruto101
            elif salario_bruto101 >=2259.21 and salario_bruto101 <=2828.65:
                impostos = 0.075
                salario_liquido101 = salario_bruto101 - (salario_bruto101*impostos)
            funcionario['matrícula'] = matricula
            funcionario['nome funcionário(a)'] = nome_funci
            funcionario['número de faltas'] = num_faltas
            funcionario['código da função'] = cod_funcao
            funcionario['salário bruto'] = salario_bruto101
            funcionario['impostos'] = impostos
            funcionario['salário líquido'] = salario_liquido101
            funcionarios.append(funcionario)
            print(f'O número de matrícula do(a) funcionário(a) {nome_funci} é {matricula}')
            print(f'O salário bruto do(a) funcionário(a) {nome_funci} é de {salario_bruto101}')
            print(f'O salário líquido do(a) funcionário(a) {nome_funci} é de {salario_liquido101}')
        if (cod_funcao == 102):
            salario_fixo102 = int(input(f'Digite o valor do salário do(a) funcionário(a) {nome_funci} da área administrativa: '))
            if salario_fixo102 < 2150 or salario_fixo102 > 6950:
                print('Os salários da área administrativa variam de R$2150,00 até R$6950,00. Tente novamente')
                inserir_funci()
                break    
            else:
                faltas102 = (salario_fixo102/30)*num_faltas
                salario_bruto102 = salario_fixo102 - faltas102
                if salario_bruto102 <= 2259.20:
                    impostos = 0  
                elif salario_bruto102 >= 2259.21 and salario_bruto102<=2828.65:
                    impostos = 0.075
                elif salario_bruto102 >= 2828.66 and salario_bruto102 <= 3751.05:
                    impostos = 0.150
                elif salario_bruto102 >=3751.06 and salario_bruto102 <= 4664.68:
                    impostos = 0.225    
                elif salario_bruto102 > 4664.68:
                    impostos = 0.275
                salario_liquido102 = salario_bruto102 - (impostos*salario_bruto102)
            funcionario['matrícula'] = matricula
            funcionario['nome funcionário(a)'] = nome_funci
            funcionario['número de faltas'] = num_faltas
            funcionario['código da função'] = cod_funcao
            funcionario['salário bruto'] = salario_bruto102
            funcionario['impostos'] = impostos
            funcionario['salário líquido'] = salario_liquido102
            funcionarios.append(funcionario)
            print(f'O número de matrícula do(a) funcionário(a) {nome_funci} é {matricula}')
            print(f'O salário bruto do(a) funcionário(a) {nome_funci} é de {salario_bruto102}')
            print(f'O salário líquido do(a) funcionário(a) {nome_funci} é de {salario_liquido102}')
        elif cod_funcao != 101 and cod_funcao !=102:
            print('Código da função inexistente, tente novamente.')
            inserir_funci()
        num=int(input('Digite qualquer número para inserir outro funcionário ou digite um número negativo para voltar ao menu'))
        print(funcionarios)

def remover_funci():
    cod1 = int(input('Digite o número da matrícula que deseja excluir: '))
    for i1 in funcionarios:
        if i1['matrícula'] == cod1:
            funcionarios.remove(i1)
            print(funcionarios)
            break
    else:
        print('Número de matrícula não encontrado. Tente novamente!')
        remover_funci()


def folha_pagamento():
    cod = int(input('Digite o número de matrícula do funcionário que deseja pesquisar: '))
    for i in funcionarios:
        if i['matrícula'] == cod:
            print()
            print("Matrícucla: ", i['matrícula'])
            print("Nome:", i['nome funcionário(a)'])
            print("Número de faltas: ", i['número de faltas'])
            print("Função: ", i['código da função'])
            print("Salário Bruto: :", i['salário bruto'])
            print("Impostos: ", i['impostos'])
            print("Salário liquído: ", i['salário líquido'])
            break
    else:
        print('Esse funcionário não existe. Tente novamente!')
        folha_pagamento()


def relatorio_salario():
    print('Relatório com Salário Bruto e Líquido de Todos os Funcionários:')
    print('Matrícula\tNome\tCódigo da Função\tSalário Bruto\tSalário Líquido')
    for funcionario in funcionarios:
        print(funcionario['matrícula'], '\t', funcionario['nome funcionário(a)'], '\t',
              funcionario['código da função'], '\t\t', funcionario['salário bruto'], '\t\t', funcionario['salário líquido'])
    else:
        print ('Nenhum funcionário cadastrado.')


def maior_salario():
    if funcionarios:
        funcionario_maior_salario = max(funcionarios, key=lambda x: x['salário líquido'])
        print('Informações do Funcionário com Maior Salário Líquido:')
        print('Matrícula:', funcionario_maior_salario['matrícula'])
        print('Nome:', funcionario_maior_salario['nome funcionário(a)'])
        print('Código da Função:', funcionario_maior_salario['código da função'])
        print('Salário Bruto:', funcionario_maior_salario['salário bruto'])
        print('Salário Líquido:', funcionario_maior_salario['salário líquido'])
    else:
        print('Nenhum funcionário cadastrado.')


def maior_faltas():
    if funcionarios:
        funcionario_maior_faltas = max(funcionarios, key=lambda x: x['número de faltas'])
        desconto = funcionario_maior_faltas['salário bruto'] / 30 * funcionario_maior_faltas['número de faltas']
        print('Informações do Funcionário com Maior Número de Faltas no Mês:')
        print('Matrícula:', funcionario_maior_faltas['matrícula'])
        print('Nome:', funcionario_maior_faltas['nome funcionário(a)'])
        print('Código da Função:', funcionario_maior_faltas['código da função'])
        print('Número de Faltas:', funcionario_maior_faltas['número de faltas'])
        print('Desconto no Salário:', desconto)
    else:
        print('Nenhum funcionário cadastrado.')


def encerrar():
    print('Sistema encerrado')
    sys.exit()

telas = {
    'inicial': tela_inicial,
    'inserir': inserir_funci,
    'remover': remover_funci,
    'pagamento': folha_pagamento,
    'relatorio': relatorio_salario,
    'maior salario': maior_salario,
    'maior faltas': maior_faltas,
    'encerrar': encerrar
}


def main():
    tela_atual = 'inicial'
    navegar(tela_atual)

main()
