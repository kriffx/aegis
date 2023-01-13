from typing import Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import TableElementKeywords, WaitingKeywords
from selenium.webdriver.remote.webelement import WebElement

class Table(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.table = TableElementKeywords(ctx)
        self.waiting = WaitingKeywords(ctx)
    
    @keyword("I get table ${locator} cell ${row}/${column} with ${loglevel} level")
    def get_table_cell_level(self, locator: Union[WebElement, None, str], row: int, column: int, loglevel: str) -> str:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.table.get_table_cell(locator=locator, row=row, column=column, loglevel=loglevel)
    
    @keyword("I get table ${locator} cell ${row}/${column}")
    def get_table_cell(self, locator: Union[WebElement, None, str], row: int, column: int) -> str:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.get_table_cell_level(locator=locator, row=row, column=column, loglevel="TRACE")

    @keyword("I assert table ${locator} cell ${row}/${column} should contain ${expected} text with ${loglevel} level")
    def table_cell_should_contain_level(self, locator: Union[WebElement, None, str], row: int, column: int, expected: str, loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.table.table_cell_should_contain(locator=locator, row=row, column=column, expected=expected, loglevel=loglevel)
    
    @keyword("I assert table ${locator} cell ${row}/${column} should contain ${expected} text")
    def table_cell_should_contain(self, locator: Union[WebElement, None, str], row: int, column: int, expected: str) -> None:
        self.table_cell_should_contain_level(locator=locator, row=row, column=column, expected=expected, loglevel="TRACE")

    @keyword("I assert table ${locator} column ${column} should contain ${expected} text with ${loglevel} level")
    def table_column_should_contain_level(self, locator: Union[WebElement, None, str], column: int, expected: str, loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.table.table_column_should_contain(locator=locator, column=column, expected=expected, loglevel=loglevel)
    
    @keyword("I assert table ${locator} column ${column} should contain ${expected} text")
    def table_column_should_contain(self, locator: Union[WebElement, None, str], column: int, expected: str) -> None:
        self.table_column_should_contain_level(locator=locator, column=column, expected=expected, loglevel="TRACE")

    @keyword("I assert table ${locator} footer should contain ${expected} text with ${loglevel} level")
    def table_footer_should_contain_level(self, locator: Union[WebElement, None, str], expected: str, loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.table.table_footer_should_contain(locator=locator, expected=expected, loglevel=loglevel)
    
    @keyword("I assert table ${locator} footer should contain ${expected} text")
    def table_footer_should_contain(self, locator: Union[WebElement, None, str], expected: str) -> None:
        self.table_footer_should_contain_level(locator=locator, expected=expected, loglevel="TRACE")
    
    @keyword("I assert table ${locator} header should contain ${expected} text with ${loglevel} level")
    def table_header_should_contain_level(self, locator: Union[WebElement, None, str], expected: str, loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.table.table_header_should_contain(locator=locator, expected=expected, loglevel=loglevel)
    
    @keyword("I assert table ${locator} header should contain ${expected} text")
    def table_header_should_contain(self, locator: Union[WebElement, None, str], expected: str) -> None:
        self.table_header_should_contain_level(locator=locator, expected=expected, loglevel="TRACE")

    @keyword("I assert table ${locator} row ${row} should contain ${expected} text with ${loglevel} level")
    def table_row_should_contain_level(self, locator: Union[WebElement, None, str], row: int, expected: str, loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.table.table_row_should_contain(locator=locator, row=row, expected=expected, loglevel=loglevel)
    
    @keyword("I assert table ${locator} row ${row} should contain ${expected} text")
    def table_row_should_contain(self, locator: Union[WebElement, None, str], row: int, expected: str) -> None:
        self.table_row_should_contain_level(locator=locator, row=row, expected=expected, loglevel="TRACE")

    @keyword("I assert table ${locator} should contain ${expected} text with ${loglevel} level")
    def table_should_contain_level(self, locator: Union[WebElement, None, str], expected: str, loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.table.table_should_contain(locator=locator, expected=expected, loglevel=loglevel)
    
    @keyword("I assert table ${locator} should contain ${expected} text")
    def table_should_contain(self, locator: Union[WebElement, None, str], expected: str) -> None:
        self.table_should_contain_level(locator=locator, expected=expected, loglevel="TRACE")