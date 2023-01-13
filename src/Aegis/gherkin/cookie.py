from typing import Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords.cookie import CookieInformation, CookieKeywords

class Cookie(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.cookie = CookieKeywords(ctx)
    
    @keyword("I delete all cookies")
    def delete_all_cookies(self) -> None:
        self.cookie.delete_all_cookies()

    @keyword("I delete cookie ${name}")
    def delete_cookie(self, name) -> None:
        self.cookie.delete_cookie(name=name)

    @keyword("I get cookies string")
    def get_cookies_string(self) -> Union[str, dict]:
        return self.cookie.get_cookies(as_dict=False)
    
    @keyword("I get cookies dictionary")
    def get_cookies_dictionary(self) -> Union[str, dict]:
        return self.cookie.get_cookies(as_dict=True)

    @keyword("I get cookie ${name}")
    def get_cookie(self, name: str) -> CookieInformation:
        return self.cookie.get_cookie(name=name)

    @keyword("I add ${name} cookie ${value} value with ${parameters}")
    def add_cookie_parameters(self, name: str, value: str, parameters: dict) -> None:
        path = parameters.get("path", None)
        domain = parameters.get("domain", None)
        secure = parameters.get("secure", None)
        expiry = parameters.get("expiry", None)
        self.cookie.add_cookie(name=name, value=value, path=path, domain=domain, secure=secure, expiry=expiry)
    
    @keyword("I add ${name} cookie ${value} value")
    def add_cookie(self, name: str, value: str) -> None:
        self.add_cookie_parameters(name=name, value=value, parameters={})