import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
import pytest


@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    landingPage = pc.LandingPage()
    landingPage.openLandingPage()
    dropdownPage = landingPage.clickDropdownLink()
    yield dropdownPage

    '''Teardown'''
    dropdownPage.navigateToHome()
    
@pytest.mark.minor
def test_header_footer(setup_teardown):
    dropdownPage = setup_teardown
    assert dropdownPage.isHeaderFooterDisplayed() == True

def test_dropdownValues(setup_teardown):
    expectedDropdownOptions = ['Please select an option','Option 1','Option 2']
    dropdownPage = setup_teardown
    actualDropdownOptions = [option.text for option in dropdownPage.dropdownSelectOptions]
    assert expectedDropdownOptions == actualDropdownOptions