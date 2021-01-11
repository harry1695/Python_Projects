import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.inshorts.com/en/read"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
news_image_data = []
news_title_data = []
news_description_data = []
news_auther_data = []
news_date_data = []
news_time_data = []
no_of_news_card = soup.find_all('div', attrs={'class': 'news-card'})
print(len(no_of_news_card))
for nt in no_of_news_card:
    news_title = nt.find('span', attrs={'itemprop': 'headline'}).text
    print(news_title)
    news_title_data.append(news_title)
    news_description = nt.find('div', attrs={'itemprop': 'articleBody'}).text
    print(news_description)
    news_description_data.append(news_description)
    news_auther = nt.find('span', attrs={'class': 'author'}).text
    print(news_auther)
    news_auther_data.append(news_auther)
    news_time = nt.find('span', attrs={'time'}).text
    print(news_time)
    news_time_data.append(news_time)
    news_date = nt.find('span', attrs={'date'}).text
    print(news_date)
    news_date_data.append(news_date)


df = pd.DataFrame({'Title': news_title_data, 'Description': news_description_data, 'Posted By': news_auther_data, 'Date': news_date_data, 'Time': news_time_data})
df.to_csv('shortsnews.csv', index=False, encoding='utf-8')
