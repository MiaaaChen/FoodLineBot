from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
import pyshorteners

s = pyshorteners.Shortener(api_key = "cd1b8bc8ce0c839335d457ed8f4a50c69aad8e9c")

# 美食抽象類別
class Food(ABC):
 
    def __init__(self, area, category):
        self.area = area 
        self.category = category

    @abstractmethod
    def scrape(self):
        pass
 
 
# 愛食記爬蟲
class IFoodie(Food):
 
    def scrape(self):
        response = requests.get(
            "https://ifoodie.tw/explore/" + self.area +
            "/list/" + self.category + "?sortby=popular&opening=true")
 
        soup = BeautifulSoup(response.content, "html.parser")
 
        # 爬取前五筆餐廳卡片資料
        cards = soup.find_all(
            'div', {'class': 'jsx-1002413726 restaurant-info'}, limit=5)
 
        content = ""
        for card in cards:
 
            title = card.find(  # 餐廳名稱
                "a", {"class": "jsx-1002413726 title-text"}).getText()
 
            stars = card.find(  # 餐廳評價
                "div", {"class": "jsx-2373119553 text"}).getText()
            
            openinghours = card.find(  # 營業時間
                "div", {"class": "jsx-1002413726 info"}).getText()
 
            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-1002413726 address-row"}).getText()
            
            link = card.find("a", class_="jsx-1002413726 title-text") 
            url = "https://ifoodie.tw" + link['href'] if link else "链接未找到"
            
            short_url = s.bitly.short(url)                

            content += f"{title} - {short_url} \n{stars}顆星 \n{openinghours} \n{address} \n\n"
 

        return content