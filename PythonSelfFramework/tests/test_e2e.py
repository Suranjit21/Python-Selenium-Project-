import confirm as confirm

from PythonSelfFramework.tests import checkoutpage, confirmpage
from PythonSelfFramework.tests.checkoutpage import Checkout
from PythonSelfFramework.tests.confirmpage import Confirmpage
from PythonSelfFramework.tests.homepage import Homepage
from PythonSelfFramework.utilities.BaseClass import BaseClass




import pytest
import self as self
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions



from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver





# @pytest.mark.usefixtures("ourSetup")
class TestTwo(BaseClass):

   def tests_e2e(self):

       home = Homepage(self.driver)
       home.clickshopbutton().click()
       cards = home.cardscountlist()





       i = -1
       for card in cards:
           i = i + 1
           cardText = card.text

           if cardText == "Blackberry":

                home.addblackberry().click()




       checkoutpage = home.clickcheckout()
       confirmpage = checkoutpage.clickcheckoutbutton()

       confirmpage.searchbar().send_keys("ind")

       self.waitmethod("India")

       confirmpage.confirmcountry().click()

       confirmpage.agreecheckbox().click()

       confirmpage.purchase().click()


