# web_scraping_print_beautified_content.py

"""
Descripción:
    Obtén el contenido de una página web mediante requests.get() y, a continuación, utiliza BeautifulSoup para mostrar el contenido de forma legible.

    Más información: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

 
"""

from bs4 import BeautifulSoup
import requests


class WebScraping:
    def print_beautified_website_content(self, url) -> None:
        request = requests.get(url)

        soup = BeautifulSoup(request.content, 'html5lib')
        print(soup.prettify())


if __name__ == "__main__":
    web_scraping_content = WebScraping()
    web_scraping_content.print_beautified_website_content(
        'https://www.google.com')
