import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    # my_driver = webdriver.Chrome()
    my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()
