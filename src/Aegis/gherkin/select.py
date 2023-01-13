from typing import List, Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import SelectElementKeywords
from selenium.webdriver.remote.webelement import WebElement

class Select(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.select = SelectElementKeywords(ctx)
    
    @keyword("I get ${locator} list items visible labels")
    def get_list_items_labels(self, locator: Union[WebElement, str]) -> List[str]:
        return self.select.get_list_items(locator=locator, values=True)

    @keyword("I get ${locator} list items")
    def get_list_items(self, locator: Union[WebElement, str]) -> List[str]:
        return self.select.get_list_items(locator=locator)
    
    @keyword("I get ${locator} selected list label")
    def get_selected_list_label(self, locator: Union[WebElement, str]) -> str:
        return self.select.get_selected_list_label(locator=locator)

    @keyword("I get ${locator} selected list labels")
    def get_selected_list_labels(self, locator: Union[WebElement, str]) -> List[str]:
        return self.select.get_selected_list_labels(locator=locator)

    @keyword("I get ${locator} selected list value")
    def get_selected_list_value(self, locator: Union[WebElement, str]) -> str:
        return self.select.get_selected_list_value(locator=locator)

    @keyword("I get ${locator} selected list values")
    def get_selected_list_values(self, locator: Union[WebElement, str]) -> List[str]:
        return self.select.get_selected_list_values(locator=locator)

    @keyword("I assert list selection ${locator} shoud be ${expected} option")
    def list_selection_should_be(self, locator: Union[WebElement, str], *expected: str) -> None:
        self.select.list_selection_should_be(locator=locator, *expected)

    @keyword("I assert list ${locator} should have no selections")
    def list_should_have_no_selections(self, locator: Union[WebElement, str]) -> None:
        self.select.list_should_have_no_selections(locator=locator)

    @keyword("I assert page should contain list ${locator} with ${loglevel} level")
    def page_should_contain_list_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.select.page_should_contain_list(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should contain list ${locator}")
    def page_should_contain_list(self, locator: Union[WebElement, str]) -> None:
        self.page_should_contain_list_level(locator=locator, loglevel="TRACE")

    @keyword("I assertpage should not contain list ${locator} with ${loglevel} level")
    def page_should_not_contain_list_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.select.page_should_not_contain_list(locator=locator, loglevel=loglevel)
    
    @keyword("I assertpage should not contain list ${locator}")
    def page_should_not_contain_list(self, locator: Union[WebElement, str]) -> None:
        self.page_should_not_contain_list_level(locator=locator, loglevel="TRACE")

    @keyword("I select all from list ${locator}")
    def select_all_from_list(self, locator: Union[WebElement, str]) -> None:
        self.select.select_all_from_list(locator=locator)

    @keyword("I select ${locator} from list by ${indexes} index")
    def select_from_list_by_index(self, locator: Union[WebElement, str], *indexes: str) -> None:
        self.select.select_from_list_by_index(locator=locator, *indexes)

    @keyword("I select ${locator} from list by ${values} value")
    def select_from_list_by_value(self, locator: Union[WebElement, str], *values: str) -> None:
        self.select.select_from_list_by_value(locator=locator, *values)

    @keyword("I select ${locator} from list by ${labels} label")
    def select_from_list_by_label(self, locator: Union[WebElement, str], *labels: str) -> None:
        self.select.select_from_list_by_label(locator=locator, *labels)

    @keyword("I unselect all ${locator} from list")
    def unselect_all_from_list(self, locator: Union[WebElement, str]) -> None:
        self.select.unselect_all_from_list(locator=locator)

    @keyword("I unselect ${locator} from list by ${indexes} index")
    def unselect_from_list_by_index(self, locator: Union[WebElement, str], *indexes: str) -> None:
        self.select.unselect_from_list_by_index(locator=locator, *indexes)

    @keyword("I unselect ${locator} from list by ${values} value")
    def unselect_from_list_by_value(self, locator: Union[WebElement, str], *values: str) -> None:
        self.select.unselect_from_list_by_value(locator=locator, *values)

    @keyword("I unselect ${locator} from list by ${labels} label")
    def unselect_from_list_by_label(self, locator: Union[WebElement, str], *labels: str) -> None:
        self.select.unselect_from_list_by_label(locator=locator, *labels)