from selenium import webdriver

browser = webdriver.Firefox()

# Lauren would like to register her daughter, Sarah, for nerdery kids.
# She visits the homepage and looks for an appropriate link for nerdery
# kids / minecraft servers.
browser.get("http://localhost:8000")

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
# She is told that crafter4000 has not been to a nerdery course before,
# so we'll need a bit more information, but we'll show her instructions 
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
# She is presented with a sign in form. She fills it in and clicks "Sign
# in"
#
# She is taken to the "Who are you signing up" page
#
# She fills in Trevor's details
#     Trevor
#     crafter3000
#     01/01/2007
#
# crafter3000 has been to a course before, so gets approved immediately.
#
# She is taken to the payment form and fills it in.
#
# She is told that the payment has been accepted and that crafter3000
# has been approved. She clicks on a link to instructions on how to
# install technic
