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
        time.sleep(2)
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
        time.sleep(7)


# NOTE <------------ INPUT CONTACT INFO ------------------->

first_name_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/section[1]/section[1]/div[1]/label[1]/div[1]/input[1]")
first_name_input.click()
first_name_input.clear()
first_name_input_string = "Spencer"
for char in first_name_input_string:
    first_name_input.send_keys(char)

time.sleep(1)

last_name_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/section[1]/section[1]/div[2]/label[1]/div[1]/input[1]")
last_name_input.click()
last_name_input.clear()
last_name_input_string = "LeBard"
for char in last_name_input_string:
    last_name_input.send_keys(char)

time.sleep(1)

address_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/section[1]/section[1]/div[3]/label[1]/div[2]/div[1]/div[1]/input[1]")
address_input.click()
address_input.clear()
address_input_string = "69th street america"
for char in address_input_string:
    address_input.send_keys(char)

time.sleep(1)

city_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/section[1]/section[1]/div[5]/div[1]/div[1]/label[1]/div[1]/input[1]")
city_input.click()
city_input.clear()
city_input_string = "Boise"
for char in city_input_string:
    city_input.send_keys(char)

time.sleep(1)

zip_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/section[1]/section[1]/div[6]/div[1]/div[1]/label[1]/div[1]/input[1]")
zip_input.click()
zip_input.clear()
zip_input_string = "69696"
for char in zip_input_string:
    zip_input.send_keys(char)

time.sleep(1)

email_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[2]/label[1]/div[1]/input[1]")
email_input.click()
email_input.clear()
email_input_string = "slebard69@gmail.com"
for char in email_input_string:
    email_input.send_keys(char)

time.sleep(1)

phone_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[2]/div[1]/section[1]/div[3]/label[1]/div[1]/input[1]")
phone_input.click()
phone_input.clear()
phone_input_string = "208-696-6969"
for char in phone_input_string:
    phone_input.send_keys(char)

time.sleep(1)

state_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/section[1]/section[1]/div[5]/div[1]/div[2]/label[1]/div[1]/div[1]/select[1]")
state_input.click()
state_input_string = "I"
state_input.send_keys(state_input_string)
state_input.click

time.sleep(1)

continue_to_payment__info_button = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[2]/form[1]/section[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
continue_to_payment__info_button.click()

time.sleep(5)


# NOTE <----------- ADDRESS CONFIRMATION ------------>

continue_to_payment__info_button_confirm = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[3]/div[2]/div[1]/div[1]/div[1]/button[1]")
continue_to_payment__info_button_confirm.click()

time.sleep(10)


# NOTE <----------- PAYMENT INPUT ------------>

card_number_input = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/section[1]/div[1]/div[1]/section[1]/div[1]/div[1]/input[1]")
card_number_input.click()
card_number_input.clear()
card_number_input_string = "6969696969696969"
for char in card_number_input_string:
    card_number_input.send_keys(char)

time.sleep(1)

place_order_button = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/main[1]/div[2]/div[3]/div[1]/section[1]/div[3]/button[1]")
place_order_button.click()

# console.log confirm y or n?


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
