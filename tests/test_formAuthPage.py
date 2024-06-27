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
    formAuthPage = landingPage.clickFormAuthLink()
    yield formAuthPage

    '''Teardown'''
    formAuthPage.navigateToHome()
    suite_yield = suite_conftest
    
@pytest.mark.minor
def test_header_footer(setup_teardown):
    formAuthPage = setup_teardown
    assert formAuthPage.isHeaderFooterDisplayed() == True    

@pytest.mark.positive
def test_correctLoginCreds(setup_teardown):
    username = 'tomsmith'
    password = 'SuperSecretPassword!'
    
    loginNotif = setup_teardown.login(username, password)
    actualLoginMessage = loginNotif.text
    expectedLoginMessage = "You logged into a secure area!\n×"
    assert actualLoginMessage == expectedLoginMessage
    setup_teardown.clickLogout()
    
@pytest.mark.negative
def test_incorrectUsername(setup_teardown):
    username = 'beaver'
    password = 'SuperSecretPassword!'
    
    loginNotif = setup_teardown.login(username, password)
    actualLoginMessage = loginNotif.text
    expectedLoginMessage = "Your username is invalid!\n×"
    assert actualLoginMessage == expectedLoginMessage

@pytest.mark.negative
def test_incorrectPassword(setup_teardown):
    username = 'tomsmith'
    password = 'NotSoSecretPassword :('
    
    loginNotif = setup_teardown.login(username, password)
    actualLoginMessage = loginNotif.text
    expectedLoginMessage = "Your password is invalid!\n×"
    assert actualLoginMessage == expectedLoginMessage
    
    