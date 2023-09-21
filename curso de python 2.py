# lógica de programação

# passo 0 - entender o desafio que você quer resolver

# passo 1 - percorrer todos os arquivos da pasta base de dados (pasta vendas)
import os
import pandas as pd
import plotly.express as px

pasta = "o caminho da sua pasta de vendas"
lista_arquivo = os.listdir(pasta)

tabela_total = pd.DataFrame()

# Passo 2 - Importar as bases de dados de vendas e concatená-las
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        caminho_arquivo = os.path.join(pasta, arquivo)
        tabela = pd.read_csv(caminho_arquivo)
        tabela_total = pd.concat([tabela_total, tabela])

# Passo 3 - Tratar/compilar as bases de dados

# Passo 4 - Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby("Produto")["Quantidade Vendida"].sum().reset_index()
tabela_produtos = tabela_produtos.sort_values(by="Quantidade Vendida", ascending=False)


# Passo 5 - Calcular o produto que mais faturou (e faturamento)
tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
produto_mais_faturou = tabela_total.groupby("Produto")["Faturamento"].sum().idxmax()
faturamento_mais_alto = tabela_total.groupby("Produto")["Faturamento"].sum().max()




# passo 6 - Calcular a loja/cidade que mais vendeu (em faturamento - criar um gráfico/dashboard)
tabela_lojas = tabela_total.groupby("Loja")["Faturamento"].sum().reset_index()
print(tabela_lojas)

grafico = px.bar(tabela_lojas, x="Loja", y="Faturamento")
grafico.show()
