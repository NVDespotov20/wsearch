import sys

import requests
from bs4 import BeautifulSoup

def get_args():
    if len(sys.argv) == 2:
        return sys.argv[1]

    print("usage: reader.exe <url>")
    print("reader.exe: error: too few arguments")
    sys.exit(1)

def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    return soup

def get_text(soup):
    tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'p'])

    return generate_text(tags)

def generate_text(tags):
    text = ''

    for tag in tags:
        if tag.name.startswith('h'):
            text += "#" * int(tag.name[1:]) + " " + tag.text.strip()
        elif tag.name == 'p':
            text += tag.text.strip()
        
        text += '\n\n'

    return text

def main():
    url = get_args()

    soup = get_soup(url)

    text = get_text(soup)

    print(text)

if __name__ == "__main__":
    main()