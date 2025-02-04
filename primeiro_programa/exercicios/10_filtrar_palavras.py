'''
10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). 
Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa 
usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa 
demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima 
dessa quantidade de caracteres.

    Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.

'''

# Requisitando uma frase e separando-a pelos espaços. Usando replace para trocar
# pontuações por espaço.
frase = input("Digite uma frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando a frase no formato de lista, passando para a lista tamanho
# apenas as palavras com 5 ou mais caracteres e imprimindo-a na tela
tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)