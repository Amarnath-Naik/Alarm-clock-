import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text,"lxml") # to make a text data

product = soup.find_all("a", class_ = "title")
# print(data)
product_name = []
for i in product:
    name = i.text
    product_name.append(name)

# print(product_name)

prices = soup.find_all("h4",class_="float-end price card-title pull-right")

price_values = []
for i in prices:
    value = i.text
    price_values.append(value)

# print(price_values)

desc = soup.find_all("p",class_ = "description card-text")

desc_list = []
for i in desc:
    des = i.text
    desc_list.append(des)

# print(desc_list)

review = soup.find_all("p",class_ = "float-end review-count")

review_list = []

for i in review:
    rev = i.text
    review_list.append(rev)
# print(review_list)


df = pd.DataFrame({"Produt name":product_name,"prices":price_values,"desc":desc_list,"review":review_list}) 
# you can change the column name as per your requirement

print(df)
# df.to_csv("product details.csv")
df.to_excel("product.xlsx")



