# pylint: disable=no-self-use # pyATS-related exclusion


from pyats.aetest import Testcase, test
from pyats.topology import Device
from selenium.webdriver import Remote
from oct.pages.contact_us import ContactUsPage, ContactUsSuccessPage
from oct.browsers import Chrome
from oct.tests import run_testcase


class ContactUs(Testcase):
    @test
    def test(self, grid: str, device: Device) -> None:
        chrome: Remote = Chrome(grid)
        contact_us = ContactUsPage(chrome)
        contact_us.open(device)
        contact_us.fill_contact_details("Alex", "alex@gmail.com", "Test data test data")
        contact_us.press_submit()
        assert ContactUsSuccessPage(chrome).loaded()


if __name__ == "__main__":
    run_testcase()
