from typing import Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import FormElementKeywords
from selenium.webdriver.remote.webelement import WebElement
from .waiting import Waiting

class Form(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.form = FormElementKeywords(ctx)
        self.waiting = Waiting(ctx)
    
    @keyword("I submit ${locator} form")
    def submit_form_locator(self, locator: Union[WebElement, None, str] = None) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.submit_form(locator=locator)
    
    @keyword("I submit form")
    def submit_form(self) -> None:
        self.submit_form_locator(locator=None)

    @keyword("I assert checkbox ${locator} should be selected")
    def checkbox_should_be_selected(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.checkbox_should_be_selected(locator=locator)

    @keyword("I assert checkbox ${locator} sould not be selected")
    def checkbox_should_not_be_selected(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.checkbox_should_not_be_selected(locator=locator)

    @keyword("I assert page should contain checkbox ${locator} with ${loglevel} level")
    def page_should_contain_checkbox_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.page_should_contain_checkbox(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should contain checkbox ${locator}")
    def page_should_contain_checkbox(self, locator: Union[WebElement, str]) -> None:
        self.page_should_contain_checkbox_level(locator=locator, loglevel="TRACE")

    @keyword("I assert page should not contain checkbox ${locator} with ${loglevel} level")
    def page_should_not_contain_checkbox_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.form.page_should_not_contain_checkbox(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should not contain checkbox ${locator}")
    def page_should_not_contain_checkbox(self, locator: Union[WebElement, str]) -> None:
        self.page_should_not_contain_checkbox_level(locator=locator, loglevel="TRACE")

    @keyword("I select checkbox ${locator}")
    def select_checkbox(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.select_checkbox(locator=locator)

    @keyword("I unselect checkbox ${locator}")
    def unselect_checkbox(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.unselect_checkbox(locator=locator)

    @keyword("I assert page should contain radio button ${locator} with ${loglevel} level")
    def page_should_contain_radio_button_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.page_should_contain_radio_button(locator=locator, loglevel=loglevel)
    
    keyword("I assert page should contain radio button ${locator}")
    def page_should_contain_radio_button(self, locator: Union[WebElement, str]) -> None:
        self.page_should_contain_radio_button_level(locator=locator, loglevel="TRACE")

    @keyword("I assert page should not contain radio button ${locator} with ${loglevel} level")
    def page_should_not_contain_radio_button_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.form.page_should_not_contain_radio_button(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should not contain radio button ${locator}")
    def page_should_not_contain_radio_button(self, locator: Union[WebElement, str]) -> None:
        self.page_should_not_contain_radio_button_level(locator=locator, loglevel="TRACE")

    @keyword("I assert radio button ${group_name} should be set to ${value} option")
    def radio_button_should_be_set_to(self, group_name: str, value: str) -> None:
        self.form.radio_button_should_be_set_to(group_name=group_name, value=value)

    @keyword("I assert radio button ${group_name} should not be selected")
    def radio_button_should_not_be_selected(self, group_name: str) -> None:
        self.form.radio_button_should_not_be_selected(group_name=group_name)

    @keyword("I select ${value} radio button ${group_name}")
    def select_radio_button(self, value: str, group_name: str) -> None:
        self.form.select_radio_button(group_name=group_name, value=value)

    @keyword("I choose ${locator} file ${file_path}")
    def choose_file(self, locator: Union[WebElement, str], file_path: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.choose_file(locator=locator, file_path=file_path)

    @keyword("I input ${password} password ${locator}")
    def input_password(self, password: str, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.input_password(locator=locator, password=password)

    @keyword("I input ${text} text ${locator}")
    def input_text(self, text: str, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.input_text(locator=locator, text=text)

    @keyword("I assert page should contain textfield ${locator} with ${loglevel} level")
    def page_should_contain_textfield_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.page_should_contain_textfield(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should contain textfield ${locator}")
    def page_should_contain_textfield(self, locator: Union[WebElement, str]) -> None:
        self.page_should_contain_textfield_level(locator=locator, loglevel="TRACE")

    @keyword("I assert pageshould not contain textfield ${locator} with ${loglevel} level")
    def page_should_not_contain_textfield_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.form.page_should_not_contain_textfield(locator=locator, loglevel=loglevel)
    
    @keyword("I assert pageshould not contain textfield ${locator}")
    def page_should_not_contain_textfield(self, locator: Union[WebElement, str]) -> None:
        self.page_should_not_contain_textfield_level(locator=locator, loglevel="TRACE")

    @keyword("I assert textfield ${locator} should contain ${expected} text")
    def textfield_should_contain(self, locator: Union[WebElement, str], expected: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.textfield_should_contain(locator=locator, expected=expected)

    @keyword("I assert textfield ${locator} value should be ${expected} text")
    def textfield_value_should_be(self, locator: Union[WebElement, str], expected: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.textfield_value_should_be(locator=locator, expected=expected)

    @keyword("I assert textarea ${locator} should contain ${expected} text")
    def textarea_should_contain(self, locator: Union[WebElement, str], expected: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.textarea_should_contain(locator=locator, expected=expected)

    @keyword("I assert textarea ${locator} value should be ${expected} text")
    def textarea_value_should_be(self, locator: Union[WebElement, str], expected: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.textarea_value_should_be(locator=locator, expected=expected)

    @keyword("I assert page should contain button ${locator} with ${loglevel} level")
    def page_should_contain_button_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.form.page_should_contain_button(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should contain button ${locator}")
    def page_should_contain_button(self, locator: Union[WebElement, str]) -> None:
        self.page_should_contain_button_level(locator=locator, loglevel="TRACE")

    @keyword("I assert page should not contain button ${locator} with ${loglevel} level")
    def page_should_not_contain_button_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.form.page_should_not_contain_button(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should not contain button ${locator}")
    def page_should_not_contain_button(self, locator: Union[WebElement, str]) -> None:
        self.page_should_not_contain_button_level(locator=locator, loglevel="TRACE")