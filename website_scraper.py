from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# Mention the URL of website here from which you want to scrape
url = 'https://www.poynter.org/ifcn-covid-19-misinformation/?covid_countries=0&covid_rating=0&covid_fact_checkers=0'

data=dict()
scraped_df = pd.DataFrame()

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.content, 'html.parser')
# results = soup.find_all(class='post-container')
page_elements = soup.find_all('div', attrs={'class': 'post-container'})
for ele in page_elements:
  temp = []
  ele_str= str(ele.text)
  else_str_split = ele_str.splitlines()
  fact_check_temp = else_str_split[2]
  fact_check = fact_check_temp
  data['Fact_checked_by'] = re.split('[-:]', fact_check_temp)[2]
  date_country = else_str_split[3]
  data['Date']  = re.split('[-|]', date_country)[0]
  data['Country']  = re.split('[-|]', date_country)[1]
  label_text = else_str_split[5]
  data['Text'] = re.split('[-:]', label_text)[1]
  data['Label'] = re.split('[-:]', label_text)[0]
  temp.append(data)
  scraped_df = scraped_df.append(temp)
scraped_df.head()
scraped_df.to_csv('Website_Scraped_Data.csv')
