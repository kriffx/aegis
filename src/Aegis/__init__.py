from datetime import timedelta
from typing import Optional
from SeleniumLibrary import SeleniumLibrary
from .gherkin import Alert, Browser, Element, Form, Waiting

class Aegis(SeleniumLibrary):
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(
        self,
        timeout=timedelta(seconds=5),
        implicit_wait=timedelta(seconds=0),
        run_on_failure="Capture Page Screenshot",
        screenshot_root_directory: Optional[str] = None,
        plugins: Optional[str] = None,
        event_firing_webdriver: Optional[str] = None,
    ):
        SeleniumLibrary.__init__(self, timeout, implicit_wait, run_on_failure, screenshot_root_directory, plugins, event_firing_webdriver)
        SeleniumLibrary.add_library_components(self, [Alert(self), Browser(self), Element(self), Form(self), Waiting(self)])