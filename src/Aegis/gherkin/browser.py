from datetime import timedelta
from typing import List, Any
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import BrowserManagementKeywords, JavaScriptKeywords, WaitingKeywords
from webdrivermanager import ChromeDriverManager, GeckoDriverManager, EdgeChromiumDriverManager, IEDriverManager, OperaChromiumDriverManager

class Browser(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.browser_management = BrowserManagementKeywords(ctx)
        self.javascript = JavaScriptKeywords(ctx)
        self.waiting = WaitingKeywords(ctx)

    @keyword("I open ${browser} browser with ${parameters}")
    def open_browser_parameters(self, browser: str, parameters: dict) -> str:
        url = parameters.get("url", "about:blank")
        alias = parameters.get("alias", None)
        remote_url = parameters.get("remote_url", False)
        desired_capabilities = parameters.get("desired_capabilities", None)
        ff_profile_dir = parameters.get("ff_profile_dir", None)
        options = parameters.get("options", None)
        service_log_path = parameters.get("service_log_path", None)
        executable_path = parameters.get("executable_path", None)
        
        if browser == "googlechrome" or browser == "chrome" or browser == "gc" or browser == "headlesschrome":
            exec = ChromeDriverManager()
        elif browser == "firefox" or browser == "ff" or browser == "headlessfirefox":
            exec = GeckoDriverManager()
        elif browser == "edge":
            exec = EdgeChromiumDriverManager()
        elif browser == "internetexplorer" or browser == "ie":
            exec = IEDriverManager()
        elif browser == "opera":
            exec = OperaChromiumDriverManager()
        else:
            if browser == "safari" or browser == "android" or browser == "iphone" or browser == "phantomjs" or browser == "htmlunit" or browser == "htmlunitwithjs":
                return self.browser_management.open_browser(url=url, browser=browser, alias=alias, remote_url=remote_url, desired_capabilities=desired_capabilities, ff_profile_dir=ff_profile_dir, options=options, service_log_path=service_log_path, executable_path=executable_path)
            else:
                raise Exception("Browser type not available")
        return self.browser_management.open_browser(url=url, browser=browser, alias=alias, remote_url=remote_url, desired_capabilities=desired_capabilities, ff_profile_dir=ff_profile_dir, options=options, service_log_path=service_log_path, executable_path=exec.download_and_install()[1])

    @keyword("I open ${browser} browser")
    def open_browser(self, browser: str) -> str:
        return self.open_browser_parameters(browser=browser, parameters={})
    
    @keyword("I close all browsers")
    def close_all_browsers(self) -> None:
        self.browser_management.close_all_browsers()
    
    @keyword("I close browser")
    def close_browser(self) -> None:
        self.browser_management.close_browser()

    @keyword("I switch browser ${index_or_alias}")
    def switch_browser(self, index_or_alias: str) -> None:
        self.browser_management.switch_browser(index_or_alias=index_or_alias)
    
    @keyword("I get browser ids")
    def get_browser_ids(self) -> List[str]:
        return self.browser_management.get_browser_ids()
    
    @keyword("I get browser aliases")
    def get_browser_aliases(self) -> List[str]:
        return self.browser_management.get_browser_aliases()
    
    @keyword("I get session id")
    def get_session_id(self) -> str:
        return self.browser_management.get_session_id()
    
    @keyword("I get source")
    def get_source(self) -> str:
        return self.browser_management.get_source()
    
    @keyword("I get title")
    def get_title(self) -> str:
        return self.browser_management.get_title()
    
    @keyword("I get location")
    def get_location(self) -> str:
        return self.browser_management.get_location()
    
    @keyword("I assert location should be ${url}")
    def location_should_be(self, url: str) -> None:
        self.browser_management.location_should_be(url=url)
    
    @keyword("I assert location should contain ${expected}")
    def location_should_contain(self, expected: str) -> None:
        self.browser_management.location_should_contain(expected=expected)
    
    @keyword("I log location")
    def log_location(self) -> str:
        return self.browser_management.log_location()
    
    @keyword("I log source with ${loglevel}")
    def log_source_level(self, loglevel: str) -> str:
        return self.browser_management.log_source(loglevel=loglevel)
    
    @keyword("I log source")
    def log_source(self, loglevel: str = "INFO") -> str:
        return self.log_source_level(loglevel=loglevel)
    
    @keyword("I log title")
    def log_title(self) -> str:
        return self.browser_management.log_title()
    
    @keyword("I assert title should be ${title}")
    def title_should_be(self, title: str) -> None:
        self.browser_management.title_should_be(title=title)
    
    @keyword("I go back")
    def go_back(self) -> None:
        self.browser_management.go_back()
        self.waiting.wait_until_element_is_visible(locator="tag:body")
    
    @keyword("I go forward")
    def go_forward(self) -> Any:
        self.javascript.execute_javascript("window.history.forward();")
        self.waiting.wait_until_element_is_visible(locator="tag:body")
    
    @keyword("I go to ${url}")
    def go_to(self, url: str) -> None:
        self.browser_management.go_to(url=url)
    
    @keyword("I reload page")
    def reload_page(self) -> None:
        self.browser_management.reload_page()
        self.waiting.wait_until_element_is_visible(locator="tag:body")
    
    @keyword("I get selenium speed")
    def get_selenium_speed(self) -> str:
        return self.browser_management.get_selenium_speed()
    
    @keyword("I get selenium timeout")
    def get_selenium_timeout(self) -> str:
        return self.browser_management.get_selenium_timeout()
    
    @keyword("I get selenium implicit wait")
    def get_selenium_implicit_wait(self) -> str:
        return self.browser_management.get_selenium_implicit_wait()
    
    @keyword("I set ${value} selenium speed")
    def set_selenium_speed(self, value: timedelta) -> str:
        return self.browser_management.set_selenium_speed(value=value)
    
    @keyword("I set ${value} selenium timeout")
    def set_selenium_timeout(self, value: timedelta) -> str:
        return self.browser_management.set_selenium_timeout(value=value)
    
    @keyword("I set ${value} selenium implicit wait")
    def set_selenium_implicit_wait(self, value: timedelta) -> str:
        return self.browser_management.set_selenium_implicit_wait(value=value)
    
    @keyword("I set ${value} browser implicit wait")
    def set_browser_implicit_wait(self, value: timedelta) -> None:
        self.browser_management.set_browser_implicit_wait(value=value)