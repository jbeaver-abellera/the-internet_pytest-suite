import PageClasses as pc
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class FormAuthPage(pc.BasePage):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @property
    def usernameField(self):
        return self.driver.find_element(By.XPATH, '//*[@id="username"]')
    
    @property
    def passwordField(self):
        return self.driver.find_element(By.XPATH, '//*[@id="password"]')
    
    @property
    def loginBtn(self):
        return self.driver.find_element(By.XPATH, '//*[@id="login"]/button')

    def enterUsername(self, username: str):
        self.usernameField.send_keys(username)
        
    def enterPassword(self, password: str):
        self.passwordField.send_keys(password)
        
    def clickLogin(self):
        self.loginBtn.click()
        
    def clickLogout(self):
        self.logoutBth = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/a')
        self.logoutBth.click()
        
    def login(self, username: str, password: str):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLogin()
        return self.driver.find_element(By.XPATH, '//*[@id="flash"]')
        
