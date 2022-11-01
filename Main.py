"""
// Théo César Zanotto da Silva

ENUNCIADO

Sua tarefa será  gerar a matriz termo documento, dos documentos recuperados da internet e
imprimir esta matriz na tela. Para tanto:

a) Considere que todas as listas de sentenças devem ser transformadas em listas de vetores,
onde cada item será uma das palavras da sentença.

b) Todos  os  vetores  devem  ser  unidos  em  um  corpus  único  formando  uma  lista  de  vetores,
onde cada item será um lexema.

c) Este único corpus será usado para gerar o vocabulário.

d) O  resultado  esperado  será  uma  matriz  termo  documento  criada  a  partir  da  aplicação  da
técnica bag of Words em todo o corpus.

"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


array1 = []
a1 = []
matrix = []
urls = ('https://hbr.org/2022/04/the-power-of-natural-language-processing',
        'https://monkeylearn.com/natural-language-processing/',
        'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html',
        'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/',
        'https://en.wikipedia.org/wiki/Natural_language_processing')

for url in urls:
    html_page = urlopen(url).read()
    soup = BeautifulSoup(html_page, 'html.parser')

    for uw in soup(['style', 'script', 'head', 'header', 'meta', '[document]', 'title', 'footer', 'iframe', 'nav']):
        uw.decompose()

    end_r = ' '.join(soup.stripped_strings)

    for j in end_r.split():
        sen = str(j)
        a = sen.split(" ")
        for a1 in a:
            if a1 not in array1:
                array1.append(a1)
            else:
                continue

    for sent in end_r.split():
        pav = str(sent).split()
        times = [0] * len(array1)
        for pav1 in pav:
            for index, pav2 in enumerate(array1):
                if pav2 == pav1:
                    times[index] += 1

        matrix.append(times)

df = pd.DataFrame(matrix[:100], columns = array1[:919])
df

