from typing import Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import ScreenshotKeywords, WaitingKeywords
from selenium.webdriver.remote.webelement import WebElement

DEFAULT_FILENAME_PAGE = "selenium-screenshot-{index}.png"
DEFAULT_FILENAME_ELEMENT = "selenium-element-screenshot-{index}.png"
EMBED = "EMBED"

class Screenshot(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.screenshot = ScreenshotKeywords(ctx)
        self.waiting = WaitingKeywords(ctx)
    
    @keyword("I set screenshot directory ${path}")
    def set_screenshot_directory(self, path: Union[None, str]) -> str:
        return self.screenshot.set_screenshot_directory(path=path)

    @keyword("I capture page screenshot image")
    def capture_page_screenshot_image(self) -> str:
        return self.screenshot.capture_page_screenshot(filename=DEFAULT_FILENAME_PAGE)
    
    @keyword("I capture page screenshot embed")
    def capture_page_screenshot_embed(self) -> str:
        return self.screenshot.capture_page_screenshot(filename=EMBED)

    @keyword("I capture element ${locator} screenshot image")
    def capture_element_screenshot_image(self, locator: Union[WebElement, None, str]) -> str:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.screenshot.capture_element_screenshot(locator=locator, filename=DEFAULT_FILENAME_ELEMENT)
    
    @keyword("I capture element ${locator} screenshot embed")
    def capture_element_screenshot_embed(self, locator: Union[WebElement, None, str]) -> str:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.screenshot.capture_element_screenshot(locator=locator, filename=EMBED)