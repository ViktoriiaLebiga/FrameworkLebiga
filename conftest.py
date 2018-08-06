import pytest
from selenium import webdriver

@pytest.yield_fixture(scope="session")
def driver():
   _driver = webdriver.Chrome("D:\Phyton\FrameworkLebiga\drivers\chromedriver.exe")
   _driver.maximize_window()
   _driver.implicitly_wait(5)
   return _driver


@pytest.fixture(scope="session", autouse=True)
def stop(request, driver):
   def fin():
      driver.quit()
   request.addfinalizer(fin)
