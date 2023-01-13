from typing import Any, Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import JavaScriptKeywords
from selenium.webdriver.remote.webelement import WebElement

class JavaScript(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.javascript = JavaScriptKeywords(ctx)
    
    @keyword("I execute javascript ${code} code")
    def execute_javascript(self, *code: Union[WebElement, str]) -> Any:
        return self.javascript.execute_javascript(*code)

    @keyword("I execute async javascript ${code} code")
    def execute_async_javascript(self, *code: Union[WebElement, str]) -> Any:
        return self.javascript.execute_async_javascript(*code)