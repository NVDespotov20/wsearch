import sys
import os
import string
import argparse
from requests_html import HTMLSession

def char_to_hex(char):
    to_hex = str(hex(ord(char)))

    return f'%{to_hex[2:]}'

def format_query(engine, input):
    query = ""
    skip = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + " ")

    for char in input:
        if char in skip:
            query += char
            continue
        
        query += (char_to_hex(char))

    if engine == 'neeva':
        query = query.replace(" ", "%20")
    else:
        query = query.replace(" ", "+")

    return query

def get_urls(engine, query):
    session = HTMLSession()

    url = f'https://{engine}.com/search?q={query}'

    r = session.get(url)
    links = r.html.links

    valid = []
    for link in links:
        if 'https://' in link:
            valid.append(link)

    return valid

def main():
    parser = argparse.ArgumentParser(description='Search the web from the command line')
    parser.add_argument('-q','--query', type=str, nargs='+', help='Search query')
    parser.add_argument('-e', '--engine', type=str, help='Search engine to use', default='neeva')

    args = parser.parse_args()

    engine = args.engine
    search = ''.join(args.query)

    query = format_query(engine, search)

    urls = get_urls(engine,query)

    for i, url in enumerate(urls):
        print(f'{i}. {url}\n')

    url_index = int(input("Select Url: "))
    
    os.system(f'reader.exe {urls[url_index]}')

if __name__ == "__main__":
    main()