import pytest
import utils

@pytest.fixture(scope="session")
def suite_conftest():
    driver = utils.WebDriverSingleton.get_driver(isHeadless=True) 
    yield driver
    
    utils.WebDriverSingleton.quit_driver()
    
    