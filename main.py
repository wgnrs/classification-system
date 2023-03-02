import pandas as pd

# lê os dados do arquivo CSV em um DataFrame do pandas
caminho_do_arquivo = 'caminho/do/arquivo'
df = pd.read_csv(caminho_do_arquivo)

# transforma tudo que é nullo para uma string
df = df.fillna("vazio")

# define as classificações
classificacoes = {
    'alimentação': ['aliment', 'lanchinho', 'vegan', 'almoco', 'almoço', 'batata', 'potato', 'bebida', 'bolacha',
                    'cafe', 'café', 'cardapio', 'cardápio', 'catering', 'comida', 'food', 'jantar', 'lanche', 'refeic',
                    'refeiçao', 'refeiçoes', 'refrigerante', 'sandu', 'sand', 'serviço de bordo', 'serviços de bordo',
                    'servicio', 'servico de bordo', 'snack', 'suco', 'meal', 'refeição', 'refeições', 'refeicao',
                    'refeicoes', 'almuerzo', 'almorzar', 'petisco', 'champagne', 'drink', 'snak', 'cereal', 'cereais'],
    'acomodação': ['abafado', 'lotação', 'superlotado', 'lotado', 'pequeno', 'usb', 'carregador', 'televisão',
                   'monitor', 'monitores', 'entretenimento', 'filmes', 'filme', 'música', 'musica', 'limpeza', 'limpa',
                   'higiene', 'higienizada', 'espaco','espacio', 'espaço', 'seat', 'poltrona', 'poltronas', 'cadeira',
                   'silla', 'carreador', 'asientos', 'asientos', 'assento', 'saneamiento', 'limpios' ,'sanitário',
                   'banheiro', 'toilet', 'toalete', 'bano', 'sujo'],
    'funcionário': ['funcionário', 'funcionario', 'aeromoça', 'aeromoca', 'aeromoço', 'aeromoco', 'comissário',
                    'comissario', 'comissaria', 'comissária', 'empleado', 'staff', 'pilot', 'piloto', 'comandante'],
    'internet': ['wifi', 'wifie', 'internet', 'wi-fi', 'wi fi'],
    'água': ['agua', 'água', 'water'],
    'vazio': ['vazio']
}

# transforma a coluna para o tipo string (comentário podem ser considerados do tipo int ou float pelo sistema).
df['Comentario_Durante_el_vuelo'] = df['Comentario_Durante_el_vuelo'].astype(str)

# classifica as linhas do DataFrame
classificacoes_encontradas = []
for i, row in df.iterrows():
    descricao = row['Comentario_Durante_el_vuelo'].lower()
    classificacao = None
    for categoria, palavras_chave in classificacoes.items():
        if any(word in descricao for word in palavras_chave):
            classificacao = categoria
            break
    classificacoes_encontradas.append(classificacao)

# adiciona a coluna de classificação ao DataFrame
df['classificacao'] = classificacoes_encontradas

# salva o resultado em um novo arquivo CSV
df.to_excel('caminho/do/novo/arquivo', index=False)
