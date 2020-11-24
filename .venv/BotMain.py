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

foundButton = False

while not foundButton:

    addToCartButton = driver.find_element_by_class_name(
        "add-to-cart-button")

    if("btn-disabled" in addToCartButton.get_attribute("class")):
        time.sleep(3)
        driver.refresh()
    else:
        foundButton = True
        addToCartButton.click()

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

checkoutButton = driver.find_element_by_class_name(
    "add-to-cart-button")


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


# good
# <button class = "btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type = "button" style = "padding:0 8px" >
# </button >


# bad
# <button class = "btn btn-disabled btn-lg btn-block add-to-cart-button" disabled = "" type = "button" style = "padding: 0px 8px;" > Sold Out < /button >
