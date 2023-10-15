from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests

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
            
            link = card.find(
                "a", {"href": "jsx-1002413726 title-text"})
            
            url = link['href']    
            title_with_link = f"<a href='{url}'>{title}</a>"
                

            content += f"{title_with_link} \n{stars}顆星 \n{openinghours} \n{address} \n\n"
 
        return content