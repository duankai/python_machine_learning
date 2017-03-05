# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 19:16:30 2016

@author: duankai
"""

import codecs
import gensim

def read_source_file(source_file_name):
    try:
        file_reader = codecs.open(source_file_name, 'r', 'utf-8',errors="ignore")
        lines = file_reader.readlines()
        print("Read complete!")
        file_reader.close()
        return lines
    except:
        print("There are some errors while reading.")


def get_similar_words_list(w, model, topn = 20):
    result_words = []
    try:
        similary_words = model.most_similar(w, topn=20)
        #print(similary_words)
        for (word, similarity) in similary_words:
            result_words.append(word)
        #print(result_words)
    except:
        print("There are some errors!" + w)
        
    return result_words

def load_models(model_path):
    return gensim.models.Word2Vec.load(model_path)
    
def main_function(target_words_file, model_path, source_file):
    target_words = read_source_file(source_file)
    model = load_models(model_path)
    result_lines = []
    oup = codecs.open(target_words_file, 'w', 'utf-8')
    index = 0
    for w in target_words:
        w = w.replace('\n','').strip()
        most_similar_words = get_similar_words_list(w, model)
        if len(most_similar_words) == 0:
            continue
        
        index = index + 1
        if index % 1000 == 0:
            print(index)
        
        most_similar_words_str = ','.join(most_similar_words)
        
        result_line = str(index) + '\t' + w + '\t' +  most_similar_words_str + '\r\n'
        result_lines.append(result_line)
        
    oup.writelines(result_lines)
        
        
if '__name__==__main__()':
    
    target_words_file = "d:\\data\\dk_information_final_20170217.txt"
    model_path = "E:\\pyproject\\simword\\0708\\information_model0830"
    source_file = "C:\\Users\\duankai\\Desktop\\部位词.txt"
    main_function(target_words_file, model_path,source_file)
        
    
