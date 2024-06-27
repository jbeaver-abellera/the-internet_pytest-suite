import PageClasses as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class AddElementPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @property
    def addElement(self):
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
    
    def clickAddElement(self):
        self.addElement.click()
        
    def getAddedElementCount(self):
        self.ElementList = self.driver.find_elements(By.XPATH, '//button[@class="added-manually"]')
        return len(self.ElementList)
    
    def deleteFirstElement(self):
        self.firstElement = self.driver.find_element(By.XPATH, '//*[@id="elements"]/button[1]')
        self.firstElement.click()