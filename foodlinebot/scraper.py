from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
import requests
import pyshorteners

s = pyshorteners.Shortener()

class Food(ABC):
 
    def __init__(self, area, category):
        self.area = area 
        self.category = category

    @abstractmethod
    def scrape(self):
        pass
 
 
class IFoodie(Food):
 
    def scrape(self):
        response = requests.get(
            "https://ifoodie.tw/explore/" + self.area +
            "/list/" + self.category + "?sortby=popular&opening=true")
 
        soup = BeautifulSoup(response.content, "html.parser")
 

        cards = soup.find_all(
            'div', {'class': 'jsx-1002413726 restaurant-info'}, limit=5)
 
        content = ""
        for card in cards:
 
            title = card.find(  
                "a", {"class": "jsx-1002413726 title-text"}).getText()
 
            stars = card.find(  
                "div", {"class": "jsx-2373119553 text"}).getText()
            
            openinghours = card.find( 
                "div", {"class": "jsx-1002413726 info"}).getText()
 
            address = card.find( 
                "div", {"class": "jsx-1002413726 address-row"}).getText()
            
            link = card.find("a", class_="jsx-1002413726 title-text") 
            url = "https://ifoodie.tw" + link['href'] if link else "链接未找到"
            
            short_url = s.tinyurl.short(url)                

            content += f"{title} \n{short_url} \n{stars}顆星 \n{openinghours} \n{address} \n\n"
 

        return content