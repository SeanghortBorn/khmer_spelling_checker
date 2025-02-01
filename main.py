from outils import *
from khmernltk import word_tokenize
import pandas as pd

txt = open('groundtruths/art1.txt', 'r', encoding='utf-8').read().strip()
words_from_txt = word_tokenize(txt)
xml = read_xml_file('keystrokes/p1/p1art1.xml')
words_from_xml = word_tokenize(xml)
# res = "\n".join("{} \t|\t {}".format(x, y) for x, y in zip(words_from_txt, words_from_xml))

k = [x.replace(' ', '') for x in words_from_txt]
l = [x.replace(' ', '') for x in words_from_xml]
# print(k)

# rows = [words_from_txt,words_from_xml]
rows = [k,l]
# combine rows and column names into pandas dataframe
data = pd.DataFrame(rows)

# write data
data.to_excel(
    'art1.xlsx',
    sheet_name='new_sheet',
    index=False)