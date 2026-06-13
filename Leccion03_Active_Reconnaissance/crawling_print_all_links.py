# crawling_print_all_links.py

"""
Descripción:
    Imprimir todos los enlaces de una página web utilizando BeautifulSoup.
    Más información: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    Aunque BeautifulSoup es un módulo muy potente y cubre la mayoría de las necesidades de rastreo, merece la pena echar un vistazo a urllib. Se pueden encontrar muchos ejemplos muy buenos de urllib en https://docs.python.org/3/howto/urllib2.html.
"""

from bs4 import BeautifulSoup
import requests


class WebCrawler:
    def print_beautified_website_content(self, url) -> None:
        request = requests.get(url)

        soup = BeautifulSoup(request.content, 'html5lib')

        for link in soup.find_all('a'):
            print(link.get('href'))


if __name__ == "__main__":
    web_crawler = WebCrawler()
    web_crawler.print_beautified_website_content('https://www.google.com')
