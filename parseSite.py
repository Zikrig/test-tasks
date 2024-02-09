from urllib.request import urlopen
from chardet import detect
from bs4 import BeautifulSoup
import requests
import re

class ParseSite:
    def __init__(self, siteFile='forText.txt'):
        self.site = ''
        self.link = ''
        self.siteText = ''
        self.numbers = []
        self.result = {}
        self.siteFile = siteFile
        pass

    # Получает сайт и массив страниц
    # Формирует список ссылок на одном сайте
    # Собирает список телефонных номеров для каждой ссылки
    # Получает массив
    def workWithAllSite(self, site, pages):
        self.site = site.strip('/\\')
        self.numbersClear = []
        pagesList = {}

        for pItem in range(len(pages)):
            pages[pItem] = pages[pItem].strip('/\\ ')
            path = self.site + '/' + pages[pItem]

            self.getSiteText(path)
            # self.saveSite(self.siteFile)
            self.getNumbers()
            self.clearNumbers()
            
            pagesList[pages[pItem]] = self.numbersClear
        
        self.result[self.site] = pagesList
    
    # Получает текст сайта
    def getSiteText(self, link):
        self.link = link
        r = requests.get(self.link)
        self.siteText = BeautifulSoup(r.content, 'html.parser').prettify()

    # Сохраняет сайт в файл
    def saveSite(self, file):
        with open(file, 'w', encoding='utf-8') as f:
            f.write(self.siteText)

    # Парсит номера со странцы с помощью регулярки
    def getNumbers(self):
        reg = r"\"[^\d/\\\.]{,10}(?:\+?7|8?)(?:[\-\s\(\)]*\d{2,3})?[\-\s\(\)]*(?:[\-\s]*\d{3})(?:[\-\s]*\d{2})(?:[\-\s]*\d{2})\""
        
        self.numbers = re.findall(reg, self.siteText)

    #Очищает номера
    def clearNumbers(self):
        for num in range(len(self.numbers)):
            self.numbers[num] = re.sub('\D', '', self.numbers[num])

            if(len(self.numbers[num]) == 7):
                self.numbers[num] = '495' + self.numbers[num]

            if(len(self.numbers[num]) == 11 and self.numbers[num][0] == '7'):
                self.numbers[num] = self.numbers[num][1:]

            if(len(self.numbers[num]) == 10):
                self.numbers[num] = '8' + self.numbers[num]

            self.numbersClear = set(self.numbers)
            
                

    

