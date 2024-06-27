import PageClasses as pc
from selenium.webdriver.remote.webelement import WebElement
import pytest
from conftest import suite_conftest
# 
@pytest.fixture(scope='module')
def setup_teardown(suite_conftest):
    '''Setup'''
    landingPage = pc.LandingPage()
    landingPage.openLandingPage()
    brokenImagePage = landingPage.clickBrokenImageLink()
    yield brokenImagePage

    '''Teardown'''
    brokenImagePage.navigateToHome()

@pytest.mark.minor
def test_header_footer(setup_teardown):
    brokenImagePage = setup_teardown
    assert brokenImagePage.isHeaderFooterDisplayed() == True

def test_isImageValid(setup_teardown):
    brokenImagePage = setup_teardown
    imgLinkLists = brokenImagePage.ImgLinksList
    brokenImgLinkList = []
    for imgLink in imgLinkLists:
        actualContent, actualStatusCode = brokenImagePage.openImageURL(imgLink)
        if actualStatusCode != 200: brokenImgLinkList.append(imgLink) 
    assert len(brokenImgLinkList) == 0, f'Image links not found: {brokenImgLinkList}'
    