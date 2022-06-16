import pytest
from selene.support.shared import browser

@pytest.fixture()
def browser_congif():
    browser.config.window_height = 860
    browser.config.window_width = 600