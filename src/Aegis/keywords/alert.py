from datetime import timedelta
from typing import Optional
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import AlertKeywords

class Alert(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.alert = AlertKeywords(ctx)
    
    @keyword("I input ${text} and ${action} alert with ${timeout} timeout")
    def input_text_into_alert_timeout(self, text: str, action: str, timeout: Optional[timedelta] = None) -> None:
        if action.upper() == "ACCEPT" or action.upper() == "DISMISS" or action.upper() == "LEAVE":
            self.alert.input_text_into_alert(text=text, action=action.upper(), timeout=timeout)
        else:
            raise Exception("Action type not available")
    
    @keyword("I input ${text} and ${action} alert")
    def input_text_into_alert(self, text: str, action: str) -> None:
        self.input_text_into_alert_timeout(text=text, action=action.upper(), timeout=None)
    
    @keyword("I assert alert should be present with ${timeout} timeout")
    def alert_should_be_present_timeout(self, timeout: Optional[timedelta] = None) -> None:
        self.alert.alert_should_be_present(timeout=timeout)
    
    @keyword("I assert alert should be present")
    def alert_should_be_present(self) -> None:
        self.alert_should_be_present_timeout(timeout=None)
    
    @keyword("I assert alert should not be present with ${timeout} timeout")
    def alert_should_not_be_present_timeout(self, timeout: Optional[timedelta] = None) -> None:
        self.alert.alert_should_not_be_present(timeout=timeout)
    
    @keyword("I assert alert should not be present")
    def alert_should_not_be_present(self) -> None:
        self.alert_should_not_be_present_timeout(timeout=None)
    
    @keyword("I ${action} alert with ${timeout} timeout")
    def handle_alert_timeout(self, action: str, timeout: Optional[timedelta]) -> str:
        if action.upper() == "ACCEPT" or action.upper() == "DISMISS" or action.upper() == "LEAVE":
            return self.alert.handle_alert(action=action.upper(), timeout=timeout)
        else:
            raise Exception("Action type not available")
    
    @keyword("I ${action} alert")
    def handle_alert(self, action: str) -> str:
        return self.handle_alert_timeout(action=action.upper(), timeout=None)