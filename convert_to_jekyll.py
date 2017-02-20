#!/bin/env python
#-*- coding:utf-8 -*-

import os
import re
import codecs
import datetime
from string import Template

# globals
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(SCRIPT_PATH, 'html')

class ExtNotFoundException(Exception):
    pass

def get_markdown_files():
    results = []
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.md'):
                full_name = os.path.join(root, name)
                
                # print full_name
                mo = re.search(r'(\d{4}-\d{2})/(\d{2}-\S*\.md)$', full_name)
                if mo:
                    results.append((root, name))

    return results

def get_article_title(article_md_file):
    with codecs.open(article_md_file, 'r', 'utf-8') as f:
        title = f.readline()
        return (title or 'untitled').strip()

def convrt_to_jekyll_post(markdown_files):

    # entry_tpl = Template(get_tpl('entry.tpl'))
    for path, name in markdown_files:

        jekyll_md_full_name = os.path.join(HTML_DIR, path + '-' + name)
        article_creation_time = os.path.basename(jekyll_md_full_name)[:10]

        #convert
        md_full_name = os.path.join(path, name)
        article_title = get_article_title(md_full_name)
        print 'processing:' + md_full_name
        with codecs.open(md_full_name, mode='r', encoding="utf-8") as src, \
            codecs.open(jekyll_md_full_name, 'w', 'utf-8') as html:
            
            md_text = src.read()
            # article_html = markdown.markdown(md_text, extensions=['markdown.extensions.fenced_code'])
            yaml_title = '''---
layout: post
title:  "%s"
date:   %s 08:42:42 +0800
tags:   []
---
''' % (article_title, article_creation_time)
            out_md = yaml_title + '\n'.join(md_text.split('\n')[2:])
            # print out_md
            html.write(out_md)


def main():
    markdown_files = list(reversed(sorted(get_markdown_files())))

    convrt_to_jekyll_post(markdown_files)


if __name__ == '__main__':
    main()


# print '-'*80
