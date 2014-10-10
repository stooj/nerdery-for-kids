from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest


class NewSignupTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_register_unfamiliar_child_to_nerdery_server(self):
        # Lauren would like to register her daughter, Sarah, for nerdery kids.
        # She visits the homepage.
        self.browser.get('http://localhost:8000')
        try:
            self.browser.find_element_by_id(
                'front_page')
        except NoSuchElementException:
            self.fail('front page was not found')

        # She looks for an appropriate link for nerdery servers
        try:
            nerdery_kids_link = self.browser.find_element_by_id(
                'nerdery_kids_link')
        except NoSuchElementException:
            self.fail('nerdery_kids_link not found')

        # She clicks on the link
        nerdery_kids_link.click()

        # She is taken to a page that shows what our servers are running and
        # displays a small map of each.

        # At the top is a sign-up button which she clicks on.

        # She is taken to a sign-up page with username, email address and
        # password fields.

        # She fills in her details:
        #     laurenk
        #     lauren@example.com
        #     password123
        #
        # She clicks next
        #
        # She is taken to the "who are you signing up" page
        #
        # She fills in Sarah's details
        #     Sarah
        #     crafter4000
        #     01/01/2005
        #
        # She is told that crafter4000 has not been to a nerdery course
        # before, so we'll need a bit more information, but we'll show
        # her instructions
        #
        # She is taken to a payment page and presented with a form which she
        # fills in.
        #
        # She is told that the payment has been accepted and that she can
        # activate her account by clicking on the link we sent in the email.
        # TODO: Proof of kid
        #
        #
        #
        # Lauren wants to add her son, Trevor.
        #
        # She visits the site and clicks the nerdery kids link
        #
        # She clicks the sign-up button.
        #
        # She is not logged in, so she is presented with the sign up form.
        # She clicks the "sign in" link
        #
        # She is presented with a sign in form. She fills it in and
        # clicks "Sign in"
        #
        # She is taken to the "Who are you signing up" page
        #
        # She fills in Trevor's details
        #     Trevor
        #     crafter3000
        #     01/01/2007
        #
        # crafter3000 has been to a course before, so gets approved
        # immediately.
        #
        # She is taken to the payment form and fills it in.
        #
        # She is told that the payment has been accepted and that crafter3000
        # has been approved. She clicks on a link to instructions on how to
        # install technic

        self.fail('Finish the test.')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
