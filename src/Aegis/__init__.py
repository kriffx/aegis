from .keywords import Alert, Browser, Cookie, Element, Form, Frames, JavaScript, Screenshot, Select, Table, Waiting, Window
from SeleniumLibrary import SeleniumLibrary
from datetime import timedelta
from typing import Optional

class Aegis(SeleniumLibrary):
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(
        self,
        timeout=timedelta(seconds=5),
        implicit_wait=timedelta(seconds=0),
        run_on_failure="I Capture Page Screenshot Embed",
        screenshot_root_directory: Optional[str] = None,
        plugins: Optional[str] = None,
        event_firing_webdriver: Optional[str] = None,
    ):
        SeleniumLibrary.__init__(self, timeout, implicit_wait, run_on_failure, screenshot_root_directory, plugins, event_firing_webdriver)
        SeleniumLibrary.add_library_components(self, [
            Alert(self),
            Browser(self),
            Cookie(self),
            Element(self),
            Form(self),
            Frames(self),
            JavaScript(self),
            Screenshot(self),
            Select(self),
            Table(self),
            Waiting(self),
            Window(self),
        ])