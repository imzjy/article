#!/bin/env python
#-*- coding:utf-8 -*-

import os
import re
import codecs
import markdown

OUTPUT_DIR = './html'

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

def markdown_to_html(markdown_files):
    for path, name in markdown_files:

        #create folder
        dest_folder = os.path.join(OUTPUT_DIR, path)
        print dest_folder
        if not os.path.exists(dest_folder):
            os.mkdir(dest_folder)

        #convert
        src_full_name = os.path.join(path, name)
        dest_full_name = os.path.join(dest_folder, name).rstrip('.md') + '.html'
        with codecs.open(src_full_name, mode='r', encoding="utf-8") as src, \
            codecs.open(dest_full_name, 'w', 'utf-8') as dest:
            
            md_text = src.read()
            html_text = markdown.markdown(md_text, extensions=['markdown.extensions.fenced_code'])
            dest.write(html_text)
            print html_text


def generate_index_html(markdown_files):

    markdown_files_in_full_name = [os.path.join(d, f) for d, f in markdown_files]

    start_html = u'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>blog</title>
            <meta http-equiv="content-type" content="text/html;charset=utf-8">
        </head>
        <body>
        <div class="container">
        <ol>

    '''

    for full_name in reversed(sorted(markdown_files_in_full_name)):
        with codecs.open(full_name, 'r', 'utf-8') as f:
            article_url = full_name.rstrip('.md') + '.html'
            start_html += u'<li><a href="{0}">{1}</a></li>\n'.format(article_url, f.readline().strip())

    end_html = u'''
        </ol>
        </div>
        </body>
        </html>
    '''

    with codecs.open(os.path.join(OUTPUT_DIR, 'index.html'), 'w+', 'utf-8') as f:
        f.write(start_html + end_html)


def main():
    markdown_files = get_markdown_files()

    markdown_to_html(markdown_files)
    generate_index_html(markdown_files) 


if __name__ == '__main__':
    main()


# print '-'*80
