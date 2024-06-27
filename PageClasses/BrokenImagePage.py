import requests
from selenium.webdriver.common.by import By
import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement

class BrokenImagePage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
    
    @property
    def ImgElements(self):
        return self.driver.find_elements(By.TAG_NAME, "img") # returns a list of 'img' web elements
        
    @property
    def ImgLinksList(self):
        return [img.get_attribute('src') for img in self.ImgElements]
    
    def openImageURL(self, url):
        try:
            response = requests.get(url)
            
            if response.status_code == 200: return response.content, response.status_code
            else: return None, response.status_code
        except Exception as e:
            return None, None
