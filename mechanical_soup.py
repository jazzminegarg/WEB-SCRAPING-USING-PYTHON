# First, let’s create a browser object:
import mechanicalsoup


browser = mechanicalsoup.StatefulBrowser()

# Now, open the webpage we want:
browser.open("http://httpbin.org/")
# The return value of open() is an object of type requests.Response. Actually, MechanicalSoup is using the requests library to do the actual requests to the website, so there’s no surprise that we’re getting such object. In short, it contains the data and meta-data that the server sent us. You see the HTTP response status, 200, which means “OK”, but the object also contains the content of the page we just downloaded.
#
# Just like a normal browser’s URL bar, the browser remembers which URL it’s browsing:
print(browser.url)
browser.follow_link("forms")
print(browser.url)


# We passed a regular expression "forms" to follow_link(), who followed the link whose text matched this expression. There are many other ways to call follow_link(), but we’ll get back to it.
#
# We’re now visiting http://httpbin.org/forms/post, which contains a form. Let’s see the page content:
print(browser.page)

# Actually, the return type of page() is bs4.BeautifulSoup. BeautifulSoup, aka bs4, is the second library used by Mechanicalsoup: it is an HTML manipulation library. You can now navigate in the tags of the pages using BeautifulSoup. For example, to get all the <legend> tags:
#
# >>> browser.page.find_all('legend')
# [<legend> Pizza Size </legend>, <legend> Pizza Toppings </legend>]

# To fill-in a form, we need to tell MechanicalSoup which form we’re going to fill-in and submit:browser.select_form('#login form')
# The argument to select_form() is a CSS selector. Here, we select an HTML tag named form having an attribute action whose value is "/post". Since there’s only one form in the page, browser.select_form() would have done the trick too.
browser.select_form('form[action="/post"]')




# For radio buttons, well, it’s simple too: radio buttons have several input tags with the same name and different values, just select the one you need ("size" is the name attribute, "medium" is the "value" attribute of the element we want to tick):
browser["custname"] = "Me"
browser["custtel"] = "00 00 0001"
browser["custemail"] = "nobody@example.com"
browser["size"] = "medium"
browser["topping"] = "onion"
browser["topping"] = ("bacon", "cheese")
browser["comments"] = "This pizza looks really good :-)"

# Uncomment to launch a real web browser on the current page.
# launch_browser() will launch a real web browser on the current page visited by our browser object, including the changes we just made to the form (note that it does not open the real webpage, but creates a temporary file containing the page content, and points your browser to this file). Try changing the boxes ticked and the content of the text field, and re-launch the browser.

# This method is very useful in complement with your browser’s web development tools. For example, with Firefox, right-click “Inspect Element” on a field will give you everything you need to manipulate this field (in particular the name and value attributes).
browser.launch_browser()

# Uncomment to display a summary of the filled-in form
# browser.form.print_summary()




# Assuming we’re satisfied with the content of the form, we can submit it (i.e. simulate a click on the submit button):
response = browser.submit_selected()


# The response is not an HTML page, so the browser doesn’t parse it to a BeautifulSoup object, but we can still see the text it contains:
print(response.text)