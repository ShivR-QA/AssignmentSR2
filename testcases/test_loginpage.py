import time
import pytest
from pages.loginpage import LoginPage
from packageutilities.Baseclass import Baseclass
from pages.adminpage import AdminPage

class TestLogin(Baseclass):

    #@pytest.fixture(autouse=True)
    #def classMethod(self):
    #    self.lp = LoginPage()

    def test_valid_login(self):
        lp = LoginPage(self.driver)
        lp.login("Admin","admin123")

    def test_user_search(self):
        ap = AdminPage(self.driver)
        ap.userSearch("Admin")
        result = ap.verifySuccessfulSearch()
        assert result == True

    def test_invalid_search(self):
        invalid = AdminPage(self.driver)
        invalid.invalidSearch("sfsdfd")
