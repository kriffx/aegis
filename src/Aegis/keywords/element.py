from typing import List, Optional, Tuple, Union
from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary.keywords import ElementKeywords
from selenium.webdriver.remote.webelement import WebElement
from .waiting import Waiting

class Element(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)
        self.element = ElementKeywords(ctx)
        self.waiting = Waiting(ctx)
    
    @keyword("I get webelement")
    def get_webelement(self, locator: Union[WebElement, str]) -> WebElement:
        return self.element.get_webelement(locator=locator)

    @keyword("I get webelements")
    def get_webelements(self, locator: Union[WebElement, str]) -> List[WebElement]:
        return self.element.get_webelements(locator=locator)

    @keyword("I assert element ${locator} should contain ${expected} text")
    def element_should_contain(self, locator: Union[WebElement, str], expected: Union[None, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_should_contain(locator=locator, expected=expected)

    @keyword("I assert element ${locator} should not contain ${expected} text")
    def element_should_not_contain(self, locator: Union[WebElement, str], expected: Union[None, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_should_not_contain(locator=locator, expected=expected)

    @keyword("I assert page should contain ${text} with ${loglevel} level")
    def page_should_contain_loglevel(self, text: str, loglevel: str) -> None:
        self.waiting.wait_until_page_contains(text=text)
        self.element.page_should_contain(text=text, loglevel=loglevel)
    
    @keyword("I assert page should contain ${text}")
    def page_should_contain(self, text: str) -> None:
        self.page_should_contain_loglevel(text=text, loglevel="TRACE")

    @keyword("I assert page should contain element ${locator} with ${loglevel} level and ${limit} limit")
    def page_should_contain_element_loglevel_limit(self, locator: Union[WebElement, str], loglevel: str = "TRACE", limit: Optional[int] = None) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.page_should_contain_element(locator=locator, loglevel=loglevel, limit=limit)
    
    @keyword("I assert page should contain element ${locator} with ${loglevel} level")
    def page_should_contain_element_loglevel(self, locator: Union[WebElement, str], loglevel: str = "TRACE") -> None:
        self.page_should_contain_element_loglevel_limit(locator=locator, loglevel=loglevel, limit=None)
    
    @keyword("I assert page should contain element ${locator}")
    def page_should_contain_element(self, locator: Union[WebElement, str]) -> None:
        self.page_should_contain_element_loglevel(locator=locator, loglevel="TRACE")

    @keyword("I assert page should not contain ${text} with ${loglevel} level")
    def page_should_not_contain_loglevel(self, text: str, loglevel: str = "TRACE") -> None:
        self.waiting.wait_until_page_does_not_contain(text=text)
        self.element.page_should_not_contain(text=text, loglevel=loglevel)
    
    @keyword("I assert page should not contain ${text}")
    def page_should_not_contain(self, text: str) -> None:
        self.page_should_not_contain_loglevel(text=text, loglevel="TRACE")

    @keyword("I assert page should not contain element ${locator} with ${loglevel} level")
    def page_should_not_contain_element_loglevel(self, locator: Union[WebElement, str], loglevel: str = "TRACE") ->  None:
        self.element.page_should_not_contain_element(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should not contain element ${locator}")
    def page_should_not_contain_element(self, locator: Union[WebElement, str]) ->  None:
        self.page_should_not_contain_element_loglevel(locator=locator, loglevel="TRACE")

    @keyword("I assign id ${id} to element ${locator}")
    def assign_id_to_element(self, locator: Union[WebElement, str], id: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.assign_id_to_element(locator=locator, id=id)

    @keyword("I assert element ${locator} should be disabled")
    def element_should_be_disabled(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_should_be_disabled(locator=locator)

    @keyword("I assert element ${locator} should be enabled")
    def element_should_be_enabled(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_should_be_enabled(locator=locator)

    @keyword("I assert element ${locator} should be focused")
    def element_should_be_focused(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_should_be_focused(locator=locator)

    @keyword("I assert element ${locator} should be visible")
    def element_should_be_visible(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_should_be_visible(locator=locator)

    @keyword("I assert element ${locator} should not be visible")
    def element_should_not_be_visible(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_not_visible(locator=locator)
        self.element.element_should_not_be_visible(locator=locator)

    @keyword("I assert element ${locator} should be ${expected} text")
    def element_text_should_be(self, locator: Union[WebElement, str], expected: Union[None, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_text_should_be(locator=locator, expected=expected)

    @keyword("I assert element ${locator} should not be ${not_expected} text")
    def element_text_should_not_be(self, locator: Union[WebElement, str], not_expected: Union[None, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_text_should_not_be(locator=locator, not_expected=not_expected)

    @keyword("I get element ${locator} attribute ${attribute}")
    def get_element_attribute(self, locator: Union[WebElement, str], attribute: str) -> str:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.element.get_element_attribute(locator=locator, attribute=attribute)

    @keyword("I assert element ${locator} attribute ${attribute} value should be ${expected} text")
    def element_attribute_value_should_be(self, locator: Union[WebElement, str], attribute: str, expected: Union[None, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.element_attribute_value_should_be(locator=locator, attribute=attribute, expected=expected)

    @keyword("I get ${locator} horizontal position")
    def get_horizontal_position(self, locator: Union[WebElement, str]) -> int:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.element.get_horizontal_position(locator=locator)

    @keyword("I get element ${locator} size")
    def get_element_size(self, locator: Union[WebElement, str]) -> Tuple[int, int]:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.element.get_element_size(locator=locator)

    @keyword("I get cover element ${locator}")
    def cover_element(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.cover_element(locator=locator)

    @keyword("I get ${locator} value")
    def get_value(self, locator: Union[WebElement, str]) -> str:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.element.get_value(locator=locator)

    @keyword("I get ${locator} text")
    def get_text(self, locator: Union[WebElement, str]) -> str:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.element.get_text(locator=locator)

    @keyword("I clear element ${locator} text")
    def clear_element_text(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.clear_element_text(locator=locator)

    @keyword("I get ${locator} vertical position")
    def get_vertical_position(self, locator: Union[WebElement, str]) -> int:
        self.waiting.wait_until_element_is_visible(locator=locator)
        return self.element.get_vertical_position(locator=locator)

    @keyword("I click button ${locator} with ${modifier}")
    def click_button_modifier(self, locator: Union[WebElement, str], modifier: Union[bool, str] = False) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.click_button(locator=locator, modifier=modifier)
    
    @keyword("I click button ${locator}")
    def click_button(self, locator: Union[WebElement, str]) -> None:
        self.click_button_modifier(locator=locator, modifier=False)

    @keyword("I click image ${locator} with ${modifier}")
    def click_image_modifier(self, locator: Union[WebElement, str], modifier: Union[bool, str] = False) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.click_image(locator=locator, modifier=modifier)
    
    @keyword("I click image ${locator}")
    def click_image(self, locator: Union[WebElement, str]) -> None:
        self.click_image_modifier(locator=locator, modifier=False)
    
    @keyword("I click link ${locator} with ${modifier}")
    def click_link_modifier(self, locator: Union[WebElement, str], modifier: Union[bool, str] = False) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.click_link(locator=locator, modifier=modifier)
    
    @keyword("I click link ${locator}")
    def click_link(self, locator: Union[WebElement, str]) -> None:
        self.click_link_modifier(locator=locator, modifier=False)

    @keyword("I click element ${locator} with ${modifier}")
    def click_element_modifier(self, locator: Union[WebElement, str], modifier: Union[bool, str] = False) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.click_element(locator=locator, modifier=modifier)
    
    @keyword("I click element ${locator}")
    def click_element(self, locator: Union[WebElement, str]) -> None:
        self.click_element_modifier(locator=locator, modifier=False)

    @keyword("I click element ${locator} at coordinates ${xoffset}/${yoffset}")
    def click_element_at_coordinates(self, locator: Union[WebElement, str], xoffset: int, yoffset: int) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.click_element_at_coordinates(locator=locator, xoffset=xoffset, yoffset=yoffset)

    @keyword("I double click element ${locator}")
    def double_click_element(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.double_click_element(locator=locator)

    @keyword("I set focus to element ${locator}")
    def set_focus_to_element(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.set_focus_to_element(locator=locator)

    @keyword("I scroll element ${locator} into view")
    def scroll_element_into_view(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.scroll_element_into_view(locator=locator)

    @keyword("I drag ${locator} and drop ${target}")
    def drag_and_drop(self, locator: Union[WebElement, str], target: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.waiting.wait_until_element_is_visible(locator=target)
        self.element.drag_and_drop(locator=locator, target=target)

    @keyword("I drag and drop ${locator} by offset ${xoffset}/${yoffset}")
    def drag_and_drop_by_offset(self, locator: Union[WebElement, str], xoffset: int, yoffset: int) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.drag_and_drop_by_offset(locator=locator, xoffset=xoffset, yoffset=yoffset)

    @keyword("I mouse down ${locator}")
    def mouse_down(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.mouse_down(locator=locator)

    @keyword("I mouse out ${locator}")
    def mouse_out(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.mouse_out(locator=locator)

    @keyword("I mouse over ${locator}")
    def mouse_over(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.mouse_over(locator=locator)

    @keyword("I mouse up ${locator}")
    def mouse_up(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.mouse_up(locator=locator)

    @keyword("I open ${locator} context menu")
    def open_context_menu(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.open_context_menu(locator=locator)

    @keyword("I simulate ${locator} event ${event}")
    def simulate_event(self, locator: Union[WebElement, str], event: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.simulate_event(locator=locator, event=event)

    @keyword("I press ${keys} keys")
    def press_keys(self, *keys: str) -> None:
        self.element.press_keys(locator=None, *keys)

    @keyword("I get all links")
    def get_all_links(self) -> List[str]:
        return self.element.get_all_links()

    @keyword("I mouse down on link ${locator}")
    def mouse_down_on_link(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.mouse_down_on_link(locator=locator)

    @keyword("I assert page should contain link ${locator} with ${loglevel} level")
    def page_should_contain_link_loglevel(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.page_should_contain_link(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should contain link ${locator}")
    def page_should_contain_link(self, locator: Union[WebElement, str]) -> None:
        self.page_should_contain_link_loglevel(locator=locator, loglevel="TRACE")

    @keyword("I assert page should not contain link ${locator} with ${loglevel} level")
    def page_should_not_contain_link_loglevel( self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.element.page_should_not_contain_link(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should not contain link ${locator}")
    def page_should_not_contain_link( self, locator: Union[WebElement, str]) -> None:
        self.page_should_not_contain_link_loglevel(locator=locator, loglevel="TRACE")

    @keyword("I mouse down on image ${locator}")
    def mouse_down_on_image(self, locator: Union[WebElement, str]) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.mouse_down_on_image(locator=locator)

    @keyword("I assert page should contain image ${locator} with ${loglevel} level")
    def page_should_contain_image_loglevel(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.waiting.wait_until_element_is_visible(locator=locator)
        self.element.page_should_contain_image(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should contain image ${locator}")
    def page_should_contain_image(self, locator: Union[WebElement, str]) -> None:
        self.page_should_contain_image_loglevel(locator=locator, loglevel="TRACE")

    @keyword("I assert page should not contain image ${locator} with ${loglevel} level")
    def page_should_not_contain_image_level(self, locator: Union[WebElement, str], loglevel: str) -> None:
        self.element.page_should_not_contain_image(locator=locator, loglevel=loglevel)
    
    @keyword("I assert page should not contain image ${locator}")
    def page_should_not_contain_image(self, locator: Union[WebElement, str]) -> None:
        self.page_should_not_contain_image_level(locator=locator, loglevel="TRACE")

    @keyword("I get element ${locator} count")
    def get_element_count(self, locator: Union[WebElement, str]) -> int:
        return self.element.get_element_count(locator=locator)