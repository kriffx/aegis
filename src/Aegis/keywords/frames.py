from typing import Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import FrameKeywords
from selenium.webdriver.remote.webelement import WebElement

class Frames(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.frame = FrameKeywords(ctx)
    
    @keyword("I select frame ${locator}")
    def select_frame(self, locator: Union[WebElement, str]) -> None:
        self.frame.select_frame(locator=locator)

    @keyword("I unselect frame")
    def unselect_frame(self) -> None:
        self.frame.unselect_frame()

    @keyword("I assert current frame should contain ${text} text with ${loglevel} level")
    def current_frame_should_contain_level(self, text: str, loglevel: str) -> None:
        self.frame.current_frame_should_contain(text=text, loglevel=loglevel)
    
    @keyword("I assert current frame should contain ${text} text")
    def current_frame_should_contain(self, text: str) -> None:
        self.current_frame_should_contain_level(text=text, loglevel="TRACE")

    @keyword("I assert current frame should not contain ${text} text with ${loglevel} level")
    def current_frame_should_not_contain_level(self, text: str, loglevel: str) -> None:
        self.frame.current_frame_should_not_contain(text=text, loglevel=loglevel)
    
    @keyword("I assert current frame should not contain ${text} text")
    def current_frame_should_not_contain(self, text: str) -> None:
        self.current_frame_should_not_contain_level(text=text, loglevel="TRACE")

    @keyword("I assert frame ${locator} should contain ${text} text with ${loglevel} level")
    def frame_should_contain_level(self, locator: Union[WebElement, str], text: str, loglevel: str) -> None:
        self.frame.frame_should_contain(locator=locator, text=text, loglevel=loglevel)
    
    @keyword("I assert frame ${locator} should contain ${text} text")
    def frame_should_contain(self, locator: Union[WebElement, str], text: str) -> None:
        self.frame_should_contain_level(locator=locator, text=text, loglevel="TRACE")