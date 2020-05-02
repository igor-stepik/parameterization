import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    # browser = None
    if language == "es":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/")
    elif language == "ru":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")
    elif language == "fr":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/")
    elif language == "de":
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/de/catalogue/coders-at-work_207/")
    else:
        raise pytest.UsageError("--language name should be indicated")
    yield browser
    print("\nquit browser..")
    browser.quit()