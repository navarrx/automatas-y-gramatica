import re

url_regex = r'^(?:http[s]?://)?(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}(?:/[\w.-]*)*(?:\?[\w=&]*)?$'

def url_evaluator():
    url = str(input("\nInsert your URL here: "))
    if re.fullmatch(url_regex, url):
        print(f'The url "{url}" is approved!')
    else:
        print(f'The url "{url}" is denied. Please try again')


url_evaluator()