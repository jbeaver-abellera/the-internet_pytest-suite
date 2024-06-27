# from PageClasses.LandingPage import LandingPage
import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
import pytest
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from conftest import suite_conftest

@pytest.fixture(scope='module')
# @pytest.mark.usefixtures("suite_conftest")
def setup_teardown(suite_conftest):
    '''Setup'''
    suite_yield = suite_conftest
    landingPage = pc.LandingPage()
    landingPage.openLandingPage()
    dynamicControlsPage = landingPage.clickDynamicControlsLink()
    yield dynamicControlsPage

    '''Teardown'''
    dynamicControlsPage.navigateToHome()
 
    
def test_toggleCheckbox(setup_teardown):
    dynamicControlsPage = setup_teardown
    initialState = dynamicControlsPage.isCheckboxPresent()
    dynamicControlsPage.toggleCheckbox()
    loadingMessage = dynamicControlsPage.checkboxLoadingMessage
    if loadingMessage == None:
        warnings.warn("Notifications Warning: User not notified that page is loading", UserWarning)
    
    try:
        checkBox = WebDriverWait(dynamicControlsPage.driver, 45).until(
            lambda driver: dynamicControlsPage.isCheckboxPresent() != initialState)
    except TimeoutException:
        raise AssertionError(f'Timeout error. Checkbox did not toggle.')
    
    if loadingMessage != None:
        warnings.warn("Notifications Warning: loading state did not disappear", UserWarning)
    
def test_toggleTextbox(setup_teardown):
    dynamicControlsPage = setup_teardown
    initialState = dynamicControlsPage.isTextboxEnabled()
    dynamicControlsPage.toggleTextbox()
    loadingMessage = dynamicControlsPage.textboxLoadingMessage
    if loadingMessage == None:
        warnings.warn("Notifications Warning: User not notified that page is loading", UserWarning)
    
    try:
        textbox = WebDriverWait(dynamicControlsPage.driver, 45).until(
            lambda driver: dynamicControlsPage.isTextboxEnabled() != initialState)
    except TimeoutException:
        raise AssertionError(f'Timeout error. Textbox did not toggle.')
    
    if loadingMessage != None:
        warnings.warn("Notifications Warning: loading state did not disappear", UserWarning)
    
    
