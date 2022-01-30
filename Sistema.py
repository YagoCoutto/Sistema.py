from Interface.FunçoesInterface import *
from Arquivos.FunçoesArq import *

arq = 'cadastro.txt' #verificar se o arquivo existe
if not arquivoExiste(arq):
    criarArquivo(arq)

#Principal
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
    # Listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta ==3:
        cabeçalho('Saindo do Sistema.. Até logo!'.center(30))
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')