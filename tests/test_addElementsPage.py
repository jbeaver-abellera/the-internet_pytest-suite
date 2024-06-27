import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
import pytest
from conftest import suite_conftest

@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    suite_yield = suite_conftest
    landingPage = pc.LandingPage()
    landingPage.openLandingPage()
    addElementPage = landingPage.clickAddElementsLink()
    yield addElementPage

    '''Teardown'''
    addElementPage.navigateToHome()

@pytest.mark.minor
def test_header_footer(setup_teardown):
    addElementPage = setup_teardown
    assert addElementPage.isHeaderFooterDisplayed() == True

@pytest.mark.parametrize('n', [5])
def test_click_nTimes(n, setup_teardown):
    addElementPage = setup_teardown
    for i in range(n):
        addElementPage.clickAddElement()
    actualCount = addElementPage.getAddedElementCount()
    assert actualCount == n
    
@pytest.mark.parametrize('n', [6])
def test_delete_nTimes(n, setup_teardown):
    addElementPage = setup_teardown
    currentElementCount = addElementPage.getAddedElementCount()
    maxCount = min(n,currentElementCount)
    for i in range(maxCount):
        addElementPage.deleteFirstElement()
    
        