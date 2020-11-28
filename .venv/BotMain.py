from selenium import webdriver
import time

driver = webdriver.Firefox(
    executable_path=r'C:\Users\sleba\AppData\Local\Programs\geckodriver-v0.28.0-win64\geckodriver.exe')
# NOTE PS5
# driver.get(
#     'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149')
# NOTE HDMI CORD
driver.get(
    'https://www.bestbuy.com/site/dynex-6-hdmi-cable-black/6405508.p?skuId=6405508')

time.sleep(2)

# NOTE <-------- FIND ADD TO CART BUTTON -------->

found_add_to_cart_button = False

while not found_add_to_cart_button:

    addToCartButton = driver.find_element_by_class_name(
        "add-to-cart-button")
    if("btn-disabled" in addToCartButton.get_attribute("class")):
        time.sleep(3)
        driver.refresh()
    else:
        found_add_to_cart_button = True
        addToCartButton.click()
        time.sleep(10)


# NOTE <-------- FIND CHECKOUT BUTTON --------->

found_checkout_button = False

while not found_checkout_button:

    checkout_button = driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/section[2]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]")
    if("btn-disabled" in checkout_button.get_attribute("class")):
        time.sleep(3)
        driver.refresh()
    else:
        found_checkout_button = True
        checkout_button.click()
        time.sleep(10)

# NOTE <----------- FIND CONTIUNUE AS GUEST BUTTON ------------>

found_continue_as_guest_button = False

while not found_continue_as_guest_button:

    continue_as_guest_button = driver.find_element_by_xpath(
        "/html[1]/body[1]/div[1]/div[1]/section[1]/main[1]/div[4]/div[1]/div[2]/button[1]")
    if("btn-disabled" in continue_as_guest_button.get_attribute("class")):
        time.sleep(3)
        driver.refresh()
    else:
        found_continue_as_guest_button = True
        continue_as_guest_button.click()


# def checkAvailable(self):
#     button = self.driver.find_element_by_xpath(
#         "/html[1]/body[1]/div[3]/main[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/button[1]")
#     button.click()
#     checkAvailable(self)

# class PagePoller:
#     def __init__(self, url):
#         self.url = url
#         self.createBrowser()

#     def createBrowser(self):
#         self.driver = webdriver.Firefox()
#         self.driver.get(self.url)

#     def refreshPage(self):
#         self.driver.close()
#         self.driver.quit()
#         self.createBrowser()

#     def checkAvailable(self):
#         self.driver.find_element_by_xpath(
#             "//button[@data-sku-id='6405508'].click()")


# def checkAvailable(self):
#     addToCartButton = self.driver.find_element_by_class_name(
#         "add-to-cart-button")
#     if ("btn-disabled" in addToCartButton.get_attribute("class")):
#         return False
#     else:
#         addToCartButton.click()
#         return True
