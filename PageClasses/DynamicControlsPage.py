import requests
from selenium.webdriver.common.by import By
import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

class DynamicControlsPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @property
    def checkboxRemoveBtn(self):
        return self.driver.find_element(By.XPATH, '//*[@id="checkbox-example"]/button') 
    
    @property
    def textboxEnableBtn(self):
        return self.driver.find_element(By.XPATH, '//*[@id="input-example"]/button') 
    
    @property
    def checkbox(self):
        try:
            return self.driver.find_element(By.XPATH, '//*[@id="checkbox"]/input') 
        except NoSuchElementException as e:
            return None
    @property
    def checkboxLoadingMessage(self):
        try:
            return self.driver.find_element(By.XPATH, '//form[@id="checkbox-example"]//div[@id="loading"]') 
        except NoSuchElementException as e:
            return None
    @property
    def textbox(self):
        return self.driver.find_element(By.XPATH, '//*[@id="input-example"]/input') 
        
    @property #under a div, and isvisible ang maganda dito
    def textboxLoadingMessage(self):
        try:
            return self.driver.find_element(By.XPATH, '//form[@id="input-example"]//div[@id="loading"]') 
        except NoSuchElementException as e:
            return None
        
    def isCheckboxPresent(self):
        ''' Returns true if checkbox is present'''
        return self.checkbox is not None
        
    def isTextboxEnabled(self):
        ''' Returns true if textbox is present'''
        return self.textbox.is_enabled()
        
    def toggleCheckbox(self):
        self.checkboxRemoveBtn.click()
    
    def toggleTextbox(self):
        self.textboxEnableBtn.click()

