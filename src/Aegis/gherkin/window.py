from typing import List, Optional, Tuple, Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import WindowKeywords

class Window(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.window = WindowKeywords(ctx)
    
    @keyword("I switch ${browser} window ${locator} with ${timeout} timeout")
    def switch_window_timeout(self, browser: str, locator: Union[list, str], timeout: Optional[str]) -> None:
        self.window.switch_window(locator=locator, timeout=timeout, browser=browser)
    
    @keyword("I switch ${browser} window ${locator}")
    def switch_window(self, browser: str, locator: Union[list, str]) -> None:
        self.switch_window_timeout(locator=locator, timeout=None, browser=browser)

    @keyword("I close window")
    def close_window(self):
        self.window.close_window()

    @keyword("I get ${browser} window handles")
    def get_window_handles(self, browser: str) -> List[str]:
        return self.window.get_window_handles(browser=browser)

    @keyword("I get ${browser} window identifiers")
    def get_window_identifiers(self, browser: str) -> List:
        return self.window.get_window_identifiers(browser=browser)

    @keyword("I get ${nrowser} window names")
    def get_window_names(self, browser: str) -> List[str]:
        return self.window.get_window_names(browser=browser)

    @keyword("I get ${browser} window titles")
    def get_window_titles(self, browser: str) -> List[str]:
        return self.window.get_window_titles(browser=browser)

    @keyword("I get ${browser} locations")
    def get_locations(self, browser: str) -> List[str]:
        return self.window.get_locations(browser=browser)

    @keyword("I maximize browser window")
    def maximize_browser_window(self):
        return self.window.maximize_browser_window()

    @keyword("I get window inner size")
    def get_window_inner_size(self) -> Tuple[float, float]:
        return self.window.get_window_size(inner=True)

    @keyword("I get window size")
    def get_window_size(self) -> Tuple[float, float]:
        return self.window.get_window_size()

    @keyword("I set window inner size ${width}/${height}")
    def set_window_inner_size(self, width: int, height: int):
        return self.window.set_window_size(width=width, height=height, inner=True)
    
    @keyword("I set window size ${width}/${height}")
    def set_window_size(self, width: int, height: int):
        return self.window.set_window_size(width=width, height=height)

    @keyword("I get window position")
    def get_window_position(self) -> Tuple[int, int]:
        return self.window.get_window_position()

    @keyword("I set window position ${x}/${y}")
    def set_window_position(self, x: int, y: int):
        return self.window.set_window_position(x=x, y=y)