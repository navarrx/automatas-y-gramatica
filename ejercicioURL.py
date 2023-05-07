import re

url_regex = re.compile(r'^(https?://)?(www\.)?[a-zA-Z0-9]+\.[a-zA-Z]+(/[a-zA-Z0-9]*)?(\?[a-zA-Z0-9=&]*)?$')

url = input("Ingrese la URL: ")

if url_regex.match(url):
    print(url + ' es una URL válida')
else:
    print(url + ' no es una URL válida')


