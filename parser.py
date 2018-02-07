from lxml import html
from bs4 import BeautifulSoup
import urllib3
import openpyxl as xl
import argparse


class parserFb():

    def __init__(self, path):
        self.http = urllib3.PoolManager()
        self.path = path


    # СКРАППИНГ СТРАНИЦ
    def load_www(self, uri):
        url = uri[0].encode('cp1251')
        r = self.http.request('GET', url)
        data = r.data.decode('cp1251').encode('utf8')
        self.parse_html(html_data=data)
        return

    def parse_html(self, html_data):
        soup = BeautifulSoup(html_data, "html.parser")

        pass

    def load_urls_from_xlsx(self, path):
        pass

    def start(self, path):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=u'Укажите путь к файлу')
    parser.add_argument('--path',help='Путь к файлу со ссылками')
    args = parser.parse_args()
    parserFb = (args.path)
    parserFb.start()

