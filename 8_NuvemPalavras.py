# Este código gera uma nuvem de palavras com as partes dispositivas dos acórdãos, excluindo as palavras de parada nele definidas.

import pandas as pd
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Carregando os dados
df = pd.read_excel(r"insira aqui o caminho para a planilha com a parte dispositiva dos acórdãos")

# Definindo as palavras de parada
stopwords = set(stopwords.words('portuguese'))
stopwords.update(['1°', '1ª', '1º', '2°', '2ª', '2º', '3°', '3º', '4°', '4º', '6°', '6º', '7°', '7º', 'a', 'à', 'ACORDAM', 'Acórdão', 'ainda', 'alínea', 'alíneas', 'ante', 'após', 'aposentadoria', 'art', 'art.', 'artigo', 'artigos', 'arts', 'arts.', 'assim', 'ato', 'autos', 'b', 'base', 'bem', 'c', 'cada', 'Caixa', 'Câmara', 'caput', 'caso', 'ciência', 'com', 'como', 'concessão', 'conforme', 'conhecer', 'considerá-la', 'Constituição', 'contado', 'contar', 'Contas', 'cópia', 'da', 'dar ciência', 'dar', 'data', 'de', 'dê', 'declaração', 'deliberação', 'desde', 'desta', 'deste', 'diante', 'dias', 'discutido', 'discutidos', 'do', 'Econômica', 'em', 'embargos', 'encaminhar', 'essa', 'esse', 'esta', 'este', 'expostas', 'face', 'Federal', 'fulcro', 'Fundação', 'fundamentam', 'fundamento', 'I', 'II', 'III', 'inciso', 'incisos', 'Interno', 'IV', 'IX', 'Janeiro', 'junto', 'legislação', 'Lei c', 'Lei', 'logo', 'mil', 'Ministério', 'Ministro', 'Ministros', 'n  °', 'n  º', 'n °', 'n °', 'n º', 'n º', 'n.°', 'n.º', 'n°', 'na', 'Nacional', 'nas', 'no', 'nº', 'nos', 'o', 'p', 'para', 'parágrafo', 'partir', 'peça', 'perante', 'Plenário', 'presente', 'presentes', 'Primeira', 'Procuradoria', 'proveniente', 'quanto', 'que', 'quem', 'quinze', 'R', 'razões', 'reais', 'Regimento Interno', 'Regimento', 'relatada', 'relatadas', 'relatado', 'relatados', 'Relator', 'relatório', 'República', 'Resolução  TCU', 'Resolução TCU', 'Resolução', 'reunidos', 'RI', 'Rio', 'Saúde', 'se', 'sessão', 'sobre', 'TCU', 'termo', 'termos', 'Tesouro', 'tomada', 'Tribunal', 'trinta', 'União', 'único', 'Universidade', 'V', 'vigor', 'VIII', 'vista', 'vistas', 'visto', 'vistos', 'voto'])

# Criando a nuvem de palavras
wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(' '.join(df['Parte_Dispositiva']))

# Mostrando a imagem final
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
