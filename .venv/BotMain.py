from selenium import webdriver
import time
# from pudb
# pdb.set_trace()
# Set breakpoint() in Python to call pudb
# export PYTHONBREAKPOINT = "pudb.set_trace"

# import pagerduty


# driver = webdriver.Firefox()

# happy case - item is available
# driver.get("https://www.bestbuy.com/site/nvidia-titan-rtx-24gb-gddr6-pci-express-3-0-graphics-card/6320585.p?skuId=6320585")


driver = webdriver.Firefox(
    executable_path=r'C:\Users\sleba\AppData\Local\Programs\geckodriver-v0.28.0-win64\geckodriver.exe')
driver.get(
    'https://www.bestbuy.com/site/dynex-6-hdmi-cable-black/6405508.p?skuId=6405508')


class PagePoller:
    def __init__(self, url):
        self.url = url
        self.createBrowser()

    def createBrowser(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def refreshPage(self):
        self.driver.close()
        self.driver.quit()
        self.createBrowser()

    def checkAvailable(self):
        self.driver.find_element_by_xpath(
            "//button[@data-sku-id='6405508'].click()")


def checkAvailable(self):
    addToCartButton = self.driver.find_element_by_class_name(
        "add-to-cart-button")
    if ("btn-disabled" in addToCartButton.get_attribute("class")):
        return False
    else:
        addToCartButton.click()
        return True


# good
# <button class = "btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type = "button" style = "padding:0 8px" >
# </button >


# bad
# <button class = "btn btn-disabled btn-lg btn-block add-to-cart-button" disabled = "" type = "button" style = "padding: 0px 8px;" > Sold Out < /button >
