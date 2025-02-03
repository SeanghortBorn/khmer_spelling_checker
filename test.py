from utils import *
from khmernltk import word_tokenize

# i numbers of articles
# j numbers of participants
g_art = {}
input_data = {}
for i in range(1, 7):
    path_groundtruth = f'groundtruths/art{i}.txt'
    g_art[i] = read_txt_file(f'groundtruths/art{i}.txt')
    g_art[i] = word_tokenize(clean_text(g_art[i]))
    for j in range(1, 17):
        path_input_file = f'keystrokes/p{j}/p{j}art{i}.xml'
        input_data[(j, i)] = extract_content_from_xml(f'keystrokes/p{j}/p{j}art{i}.xml')
        input_data[(j, i)] = word_tokenize(clean_text(input_data[(j, i)][0]))

        print(f'p{j}art{i} = {input_data[(j, i)]}')
    save_word_lists_to_excel([g_art[i]] + [input_data[(j, i)] for j in range(1, 17)], [f'g_art{i}'] + [f'p{j}art{i}' for j in range(1, 17)], f'compare_art{i}.xlsx')