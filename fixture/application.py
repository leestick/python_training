from selenium.webdriver.ie.webdriver import WebDriver, Options, RemoteWebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

__author__ = 'ioK'


class Application:

    def __init__(self):
        opts = Options()
        opts.require_window_focus = True
        # self.wd = WebDriver(options=opts)
        self.wd = RemoteWebDriver(command_executor='http://192.168.50.214:4444/wd/hub', options=opts)
        self.wd.implicitly_wait(5)
        self.wd.maximize_window()
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
