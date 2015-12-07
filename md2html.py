#!/bin/env python
#-*- coding:utf-8 -*-

import os
import re
import codecs
import datetime
from string import Template

import markdown
from rfeed import Item, Guid, Feed

# globals
BASE_URL = "http://blog.imzjy.com/"
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = os.path.join(SCRIPT_PATH, 'html')

class ExtNotFoundException(Exception):
    pass     

def replace_ext(path, old_ext, new_ext):
    if path[-len(old_ext):] == old_ext:
        return path[:-len(old_ext)] + new_ext
    else:
        raise ExtNotFoundException()

def get_tpl(tpl_name):
    with codecs.open(os.path.join(HTML_DIR, tpl_name), 'r', 'utf-8') as f:
        index_tpl = f.read()
        return (index_tpl or 'no content').strip()

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

def markdown_to_html(markdown_files):

    entry_tpl = Template(get_tpl('entry.tpl'))
    for path, name in markdown_files:

        #create folder
        dest_folder = os.path.join(HTML_DIR, path)
        if not os.path.exists(dest_folder):
            os.mkdir(dest_folder)

        #convert
        md_full_name = os.path.join(path, name)
        article_title = get_article_title(md_full_name)
        print 'processing:' + md_full_name
        html_full_name = replace_ext(os.path.join(dest_folder, name), '.md', '.html')
        with codecs.open(md_full_name, mode='r', encoding="utf-8") as src, \
            codecs.open(html_full_name, 'w', 'utf-8') as html:
            
            md_text = src.read()
            article_html = markdown.markdown(md_text, extensions=['markdown.extensions.fenced_code'])
            html.write(entry_tpl.substitute(article=article_html, title=article_title))


def generate_rss(markdown_files):

    rssEntries = []

    for path, name in markdown_files[:20]:

        md_full_name = os.path.join(path, name)
        article_title = get_article_title(md_full_name)
        article_url = os.path.join(BASE_URL, replace_ext(md_full_name, '.md', '.html'))
        with codecs.open(md_full_name, mode='r', encoding="utf-8") as src:
            md_text = src.read()
            article_html = markdown.markdown(md_text, extensions=['markdown.extensions.fenced_code'])

            # RSS Feed Entry
            date_groups = re.search(r'(\d{4})-(\d{2})/(\d{2})-\S*\.md$', md_full_name).groups()
            pubDate = datetime.datetime(int(date_groups[0]), int(date_groups[1]), int(date_groups[2]), 10, 00)

            rssEntry = Item(
                title = article_title,
                link = article_url, 
                description = article_html,
                author = "Jerry Chou",
                guid = Guid(article_url),
                pubDate = pubDate)
            rssEntries.append(rssEntry)
    
    # Generate RSS Feed
    feed = Feed(
        title = "佛与编程 - 周继元的博客",
        link =  os.path.join(BASE_URL, "rss.xml"),
        description = "佛与编程 - 周继元的博客",
        language = "zh-CN",
        lastBuildDate = datetime.datetime.now(),
        items = rssEntries)

    with codecs.open(os.path.join(HTML_DIR, "rss.xml"), 'w+', 'utf-8') as rss:
        rss.write(feed.rss().decode('utf-8'))


def generate_index_html(markdown_files):

    markdown_files_in_full_name = [os.path.join(d, f) for d, f in markdown_files]

    article_list = ''
    for full_name in markdown_files_in_full_name:
        article_url = replace_ext(full_name, '.md', '.html')
        article_date = full_name[2:2+10]
        article_list += u'<li><a href="{0}">{1}</a><small>{2}</small></li>\n'.format(article_url, get_article_title(full_name), article_date)

    index_tpl = Template(get_tpl('index.tpl'))
    with codecs.open(os.path.join(HTML_DIR, 'index.html'), 'w+', 'utf-8') as f:
        f.write(index_tpl.substitute(aritcle_list=article_list))


def main():
    markdown_files = list(reversed(sorted(get_markdown_files())))

    markdown_to_html(markdown_files)
    generate_rss(markdown_files)
    generate_index_html(markdown_files) 


if __name__ == '__main__':
    main()


# print '-'*80
