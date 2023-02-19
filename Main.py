"""
// Théo César Zanotto da Silva

O algoritmo deve gerar a matriz termo documento, dos documentos recuperados da internet e
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

# chosen urls
urls = ('https://hbr.org/2022/04/the-power-of-natural-language-processing',
        'https://monkeylearn.com/natural-language-processing/',
        'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html',
        'https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/',
        'https://en.wikipedia.org/wiki/Natural_language_processing')

for url in urls:
    # obtaining all the content of the page
    html_page = urlopen(url).read()
    soup = BeautifulSoup(html_page, 'html.parser')

    # removing all the unnecessary tags
    for uw in soup(['style', 'script', 'head', 'header', 'meta', '[document]', 'title', 'footer', 'iframe', 'nav']):
        uw.decompose()

    # compacting the data
    end_r = ' '.join(soup.stripped_strings)

    # splitting the sentences in single words and appending it to the array.
    for j in end_r.split():
        sen = str(j)
        a = sen.split(" ")
        for a1 in a:
            if a1 not in array1:
                array1.append(a1)
            else:
                continue

    # counting the frequency of each word in the array.
    for sent in end_r.split():
        pav = str(sent).split()
        times = [0] * len(array1)
        for pav1 in pav:
            for index, pav2 in enumerate(array1):
                if pav2 == pav1:
                    times[index] += 1

        matrix.append(times)

# displaying the result using a pandas dataframe
df = pd.DataFrame(matrix[:100], columns = array1[:920])
df

