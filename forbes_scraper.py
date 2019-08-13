from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import re
from sentiment import sentiment_analyzer_scores


def forbes_scraper(search):
    source = urlopen('https://www.forbes.com/search/?q=' + search)
    soup = BeautifulSoup(source,'lxml')

    lst = []
    for i in soup.findAll('a', {'class': "stream-item__title"}):
        title = i.text
        link = i.get('href')

        title = title.replace('\t','')
        title = title.replace('\n','')
        title = title.strip()

        lst.append({'title':title, 'link':link})

    df = pd.DataFrame.from_dict(lst)

    text_list = []
    for link in df['link']:
        source2 = urlopen(link)
        soup2 = BeautifulSoup(source2, 'lxml')
        text = soup2.findAll('p', text=re.compile("."))
        text_list.append(text)

    def cleanhtml(raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

    new_text_list = []
    for text in text_list:
        new_text_list.append(cleanhtml(str(text)))
        
    final_text_list = []
    for text in new_text_list:
        text = text.replace("[", "")
        text = text.replace("]", "")
        text = text.replace("\\", "")
        text = text.replace("\xa0", " ")
        final_text_list.append(text)
    return final_text_list

search = input('What would you like to search Forbes for?')


fb = forbes_scraper(search)

for article in fb:
    sentiment_analyzer_scores(article)