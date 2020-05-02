import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("language")
    # browser = None
    if browser_name == "es":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/")
    elif browser_name == "ru":
        print("\nstart firefox browser for test..")
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    else:
        raise pytest.UsageError("--language name should be indicated")
    yield browser
    print("\nquit browser..")
    browser.quit()