import PageClasses as pc
import utils
from selenium.webdriver.common.by import By

class LandingPage(pc.BasePage):
    def __init__(self):
        super().__init__()
    
    def openLandingPage(self):
        self.driver.get(utils.Constants.WEBSITE_URL)
    
    @property
    def addElement(self):
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[2]/a')
        
    @property
    def brokenImageLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[4]/a')
    
    @property
    def dropdownLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[11]/a')
    
    @property
    def dynamicControlsLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[13]/a')
    
    @property
    def formAuth(self):
        return self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    
    
    def clickAddElementsLink(self):
        self.addElement.click()
        return  pc.AddElementPage(self.driver)
    
    def clickBrokenImageLink(self):
        self.brokenImageLink.click()
        return  pc.BrokenImagePage(self.driver)
    
    def clickDropdownLink(self):
        self.dropdownLink.click()
        return  pc.DropdownPage(self.driver)
    
    def clickDynamicControlsLink(self):
        self.dynamicControlsLink.click()
        return  pc.DynamicControlsPage(self.driver)
    
    def clickFormAuthLink(self):
        self.formAuth.click()
        return  pc.FormAuthPage(self.driver)
            