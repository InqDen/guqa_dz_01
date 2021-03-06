from selene.support.shared import browser
from selene import be, have

def test_open_browser(browser_congif):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
#browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_one_looking():
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_looking_something():
    browser.element('[id= "search"]').should(have.text('Looking for something'))
