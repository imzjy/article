#!/bin/env python
#-*- coding:utf-8 -*-

import os
import re
import codecs
import markdown

output_dir = './html'

def get_markdown_files():
    results = []
    for root, dirs, files in os.walk('..'):
        for name in files:
            if name.endswith('.md'):
                full_name = os.path.join(root, name)
                
                # print full_name
                mo = re.search(r'(\d{4}-\d{2})/(\d{2}-\S*\.md)$', full_name)
                if mo:
                    results.append((root, name))

    return results

markdown_files = get_markdown_files()

for path, name in markdown_files:
    #create folder
    target_folder = os.path.join(output_dir, path)
    print target_folder
    if not os.path.exists(target_folder):
        os.mkdir(target_folder)


# year_mon, article_name = mo.groups()
# print year_mon, article_name

# #create folder
# target_folder = os.path.join(output_dir, year_mon)
# print target_folder
# if not os.path.exists(target_folder):
#     os.mkdir(target_folder)



# target_full_name = os.path.join(target_folder, name).rstrip('.md') + '.html'
# with codecs.open(full_name, 
# 		mode='r+', encoding="utf-8") as f, codecs.open(target_full_name, 'w+', 'utf-8') as w:
# 	md_text = f.read()
# 	print markdown.markdown(md_text, extensions=['markdown.extensions.fenced_code'])


# print '-'*80
