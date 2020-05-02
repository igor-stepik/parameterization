import time

def test_guest_should_see_add_to_basket_button(browser):
    time.sleep(30)
    browser.find_element_by_class_name("btn-add-to-basket")
