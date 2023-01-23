from datetime import timedelta
from typing import Optional, Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import WaitingKeywords
from selenium.webdriver.remote.webelement import WebElement

class Waiting(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.waiting = WaitingKeywords(ctx)
    
    @keyword("I wait for condition ${condition} with ${timeout} timeout")
    def wait_for_condition_timeout(self, condition: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_for_condition(condition=condition, timeout=timeout)
    
    @keyword("I wait for condition ${condition}")
    def wait_for_condition(self, condition: str) -> None:
        self.wait_for_condition_timeout(condition=condition, timeout=None)
    
    @keyword("I wait until location is ${expected} with ${timeout} timeout")
    def wait_until_location_is_timeout(self, expected: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_location_is(expected=expected, timeout=timeout)
    
    @keyword("I wait until location is ${expected}")
    def wait_until_location_is(self, expected: str) -> None:
        self.wait_until_location_is_timeout(expected=expected, timeout=None)
    
    @keyword("I wait until location is not ${location} with ${timeout} timeout")
    def wait_until_location_is_not_timeout(self, location: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_location_is_not(location=location, timeout=timeout)
    
    @keyword("I wait until location is not ${location}")
    def wait_until_location_is_not(self, location: str) -> None:
        self.wait_until_location_is_not_timeout(location=location, timeout=None)
    
    @keyword("I wait until location contains ${expected} with ${timeout} timeout")
    def wait_until_location_contains_timeout(self, expected: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_location_contains(expected=expected, timeout=timeout)
    
    @keyword("I wait until location contains ${expected}")
    def wait_until_location_contains(self, expected: str) -> None:
        self.wait_until_location_contains_timeout(expected=expected, timeout=None)
    
    @keyword("I wait until location does not contain ${location} with ${timeout} timeout")
    def wait_until_location_does_not_contain_timeout(self, location: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_location_does_not_contain(location=location, timeout=timeout)
    
    @keyword("I wait until location does not contain ${location}")
    def wait_until_location_does_not_contain(self, location: str) -> None:
        self.wait_until_location_does_not_contain_timeout(location=location, timeout=None)
    
    @keyword("I wait until page contains ${text} text with ${timeout} timeout")
    def wait_until_page_contains_timeout(self, text: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_page_contains(text=text, timeout=timeout)
    
    @keyword("I wait until page contains ${text} text")
    def wait_until_page_contains(self, text: str) -> None:
        self.wait_until_page_contains_timeout(text=text, timeout=None)
    
    @keyword("I wait until page does not contain ${text} text with ${timeout} timeout")
    def wait_until_page_does_not_contain_timeout(self, text: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_page_does_not_contain(text=text, timeout=timeout)
    
    @keyword("I wait until page does not contain ${text} text")
    def wait_until_page_does_not_contain(self, text: str) -> None:
        self.wait_until_page_does_not_contain_timeout(text=text, timeout=None)
    
    @keyword("I wait until page contains element ${locator} with ${timeout} timeout and limit ${limit}")
    def wait_until_page_contains_element_timeout_limit(self, locator: Union[WebElement, None, str], timeout: Optional[timedelta] = None, limit: Optional[int] = None) -> None:
        self.waiting.wait_until_page_contains_element(locator=locator, timeout=timeout, limit=limit)
    
    @keyword("I wait until page contains element ${locator} with ${timeout} timeout")
    def wait_until_page_contains_element_timeout(self, locator: Union[WebElement, None, str], timeout: Optional[timedelta] = None) -> None:
        self.wait_until_page_contains_element_timeout_limit(locator=locator, timeout=timeout, limit=None)
    
    @keyword("I wait until page contains element ${locator}")
    def wait_until_page_contains_element(self, locator: Union[WebElement, None, str]) -> None:
        self.wait_until_page_contains_element_timeout(locator=locator, timeout=None)
    
    @keyword("I wait until page does not contain element ${locator} with ${timeout} timeout and limit ${limit}")
    def wait_until_page_does_not_contain_element_timeout_limit(self, locator: Union[WebElement, None, str], timeout: Optional[timedelta] = None, limit: Optional[int] = None) -> None:
        self.waiting.wait_until_page_does_not_contain_element(locator=locator, timeout=timeout, limit=limit)
    
    @keyword("I wait until page does not contain element ${locator} with ${timeout} timeout")
    def wait_until_page_does_not_contain_element_timeout(self, locator: Union[WebElement, None, str], timeout: Optional[timedelta] = None) -> None:
        self.wait_until_page_does_not_contain_element_timeout_limit(locator=locator, timeout=timeout, limit=None)
    
    @keyword("I wait until page does not contain element ${locator}")
    def wait_until_page_does_not_contain_element(self, locator: Union[WebElement, None, str]) -> None:
        self.wait_until_page_does_not_contain_element_timeout(locator=locator, timeout=None)
    
    @keyword("I wait until element is visible ${locator} with ${timeout} timeout")
    def wait_until_element_is_visible_timeout(self, locator: Union[WebElement, None, str], timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator, timeout=timeout)
    
    @keyword("I wait until element is visible ${locator}")
    def wait_until_element_is_visible(self, locator: Union[WebElement, None, str]) -> None:
        self.wait_until_element_is_visible_timeout(locator=locator, timeout=None)
    
    @keyword("I wait until element is not visible ${locator} with ${timeout} timeout")
    def wait_until_element_is_not_visible_timeout(self, locator: Union[WebElement, None, str], timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_element_is_not_visible(locator=locator, timeout=timeout)
    
    @keyword("I wait until element is not visible ${locator}")
    def wait_until_element_is_not_visible(self, locator: Union[WebElement, None, str]) -> None:
        self.wait_until_element_is_not_visible_timeout(locator=locator, timeout=None)
    
    @keyword("I wait until element is enabled ${locator} with ${timeout} timeout")
    def wait_until_element_is_enabled_timeout(self, locator: Union[WebElement, None, str], timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_element_is_enabled(locator=locator, timeout=timeout)
    
    @keyword("I wait until element is enabled ${locator}")
    def wait_until_element_is_enabled(self, locator: Union[WebElement, None, str]) -> None:
        self.wait_until_element_is_enabled_timeout(locator=locator, timeout=None)
    
    @keyword("I wait until element ${locator} contains ${text} text with ${timeout} timeout")
    def wait_until_element_contains_timeout(self, locator: Union[WebElement, None, str], text: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_element_contains(locator=locator, text=text, timeout=timeout)
    
    @keyword("I wait until element ${locator} contains ${text} text")
    def wait_until_element_contains(self, locator: Union[WebElement, None, str], text: str) -> None:
        self.wait_until_element_contains_timeout(locator=locator, text=text, timeout=None)
    
    @keyword("I wait until element ${locator} does not contains ${text} text with ${timeout} timeout")
    def wait_until_element_does_not_contain_timeout(self, locator: Union[WebElement, None, str], text: str, timeout: Optional[timedelta] = None) -> None:
        self.waiting.wait_until_element_does_not_contain(locator=locator, text=text, timeout=timeout)
    
    @keyword("I wait until element ${locator} does not contains ${text} text")
    def wait_until_element_does_not_contain(self, locator: Union[WebElement, None, str], text: str) -> None:
        self.wait_until_element_does_not_contain_timeout(locator=locator, text=text, timeout=None)