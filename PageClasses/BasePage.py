import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self):
        self.driver = utils.WebDriverSingleton.get_driver(isHeadless=True) 
        
    def navigateToHome(self):
        self.driver.get(utils.Constants.WEBSITE_URL)
    
    def isHeaderFooterDisplayed(self):
        try:
            header = self.driver.find_element(By.XPATH, '/html/body/div[2]/a/img')
            footer = self. driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div')
            bothDisplayed = header.is_displayed() and footer.is_displayed()
            return bothDisplayed
        except Exception as e:
            print(f'Error finding headers and footers: {e}') 
            return None