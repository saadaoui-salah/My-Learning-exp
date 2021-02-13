from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


def connect(search,page=1):
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
    url    = f"https://www.amazon.com/s?k={search}&page={page}"
    driver.get(url)
    page_source = driver.page_source
    return page_source
    
def paginatoinm_and_element(source):    
    soup = BeautifulSoup(source,'lxml')
    navigation = soup.find_all('li',{'class':'a-disabled'})
    page_num = navigation[1]
    page_num = int(page_num.text)
    return page_num

def implement_data(title,price,url,img_url):
    product = {}
    product['Title']     = title
    product['price']     = price
    product['Url']       = url
    product['Image Url'] = img_url
    print(product)
    return product

def get_data(search,page_num):
    data = []
    i = 2
    while i < page_num:
        source = connect(search=search,page=i)
        soup   = BeautifulSoup(source,'lxml')
        cards  = soup.find_all('div',{'data-asin':True,'data-component-type':'s-search-result'})
        
        for card in cards:
            price_tag = card.find('span',{'class':'a-price-whole'})
            h2        = card.h2
            title     = h2.text.strip()
            url       = h2.a.get('href')
            img_url   = card.img.get("src")
            price     = None
            
            try:
                price = int(price_tag.text.strip(".").strip())
            except ValueError:
                price = int(price_tag.text.strip(".").strip().replace(",",""))
            except AttributeError:
                price = None
            product   = implement_data(title,price,url,img_url)
            data.append(product)
        
        i = i+1    
    return data 

def start_scraping():
    search = "tabllet"
    page_source = connect(search)
    page_num = paginatoinm_and_element(page_source)    
    data = get_data(search=search,page_num=page_num)
    return data

start_scraping()