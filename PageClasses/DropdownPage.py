from selenium.webdriver.common.by import By
import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select

class DropdownPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        
    @property
    def dropdownWebElement(self):
        return self.driver.find_element(By.XPATH, '//*[@id="dropdown"]') 
             
    @property
    def dropdownSelect(self):
        return Select(self.dropdownWebElement)
    
    @property
    def dropdownSelectOptions(self):
        return self.dropdownSelect.options
    
    