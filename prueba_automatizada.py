import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

browser.get('https://petstore.octoperf.com/actions/Catalog.action')


def historia1():
    browser.find_element(By.LINK_TEXT, "Sign In").click()
    browser.find_element(By.LINK_TEXT, "Register Now!").click()
    browser.find_element(By.NAME, "username").click()
    browser.find_element(By.NAME, "username").send_keys("reeewsdswesfsd")
    browser.find_element(By.NAME, "password").click()
    browser.find_element(By.NAME, "password").send_keys("aver")
    browser.find_element(By.NAME, "repeatedPassword").click()
    browser.find_element(By.NAME, "repeatedPassword").send_keys("aver")
    browser.find_element(By.NAME, "account.firstName").click()
    browser.find_element(By.NAME, "account.firstName").send_keys("aver")
    browser.find_element(By.NAME, "account.lastName").click()
    browser.find_element(By.NAME, "account.lastName").send_keys("aver")
    browser.find_element(By.NAME, "account.email").click()
    browser.find_element(By.NAME, "account.email").send_keys("averrr@gmail.com")
    browser.find_element(By.NAME, "account.phone").click()
    browser.find_element(By.NAME, "account.phone").send_keys("45676")
    browser.find_element(By.NAME, "account.address1").click()
    browser.find_element(By.NAME, "account.address1").send_keys("aver")
    browser.find_element(By.NAME, "account.address2").click()
    browser.find_element(By.NAME, "account.address2").send_keys("aver")
    browser.find_element(By.NAME, "account.city").click()
    browser.find_element(By.NAME, "account.city").send_keys("aver")
    browser.find_element(By.NAME, "account.state").click()
    browser.find_element(By.NAME, "account.state").send_keys("aver")
    browser.find_element(By.NAME, "account.zip").click()
    browser.find_element(By.NAME, "account.zip").send_keys("788")
    browser.find_element(By.NAME, "account.country").click()
    browser.find_element(By.NAME, "account.country").send_keys("aver")
    browser.save_screenshot("formulario_de_registro.png")
    browser.find_element(By.NAME, "newAccount").click()
    browser.find_element(By.LINK_TEXT, "Sign In").click()
    browser.find_element(By.NAME, "password").click()
    browser.find_element(By.NAME, "password").clear()
    browser.find_element(By.NAME, "password").send_keys("aver")
    browser.find_element(By.NAME, "signon").click()
    return

def historia2():
    browser.find_element(By.LINK_TEXT, "My Account").click()
    browser.find_element(By.NAME, "password").send_keys("qwert")
    browser.find_element(By.NAME, "repeatedPassword").click()
    browser.find_element(By.NAME, "repeatedPassword").send_keys("qwert")
    browser.find_element(By.NAME, "account.email").click()
    browser.find_element(By.NAME, "account.email").send_keys("wea20394")
    browser.find_element(By.NAME, "account.city").click()
    browser.find_element(By.NAME, "account.city").send_keys("qwedfe")
    browser.save_screenshot("edicion_de_datos.png")
    browser.find_element(By.NAME, "editAccount").click()
    browser.find_element(By.CSS_SELECTOR, "#LogoContent img").click()
    return

def historia3():
    browser.find_element(By.NAME, "keyword").click()
    browser.find_element(By.NAME, "keyword").send_keys("goldfish")
    browser.find_element(By.NAME, "searchProducts").click()
    browser.save_screenshot("busqueda.png")

    return

def historia4():
    browser.find_element(By.LINK_TEXT, "Fresh Water fish from China").click()
    browser.find_element(By.LINK_TEXT, "Add to Cart").click()
    browser.find_element(By.CSS_SELECTOR, "#LogoContent img").click()
    browser.find_element(By.CSS_SELECTOR, "#SidebarContent > a:nth-child(7) > img").click()
    browser.find_element(By.LINK_TEXT, "FL-DLH-02").click()
    browser.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .Button").click()
    browser.find_element(By.CSS_SELECTOR, "#LogoContent img").click()
    browser.find_element(By.NAME, "img_cart").click()
    browser.save_screenshot("carrito.png")

    return
def historia5():
    browser.find_element(By.LINK_TEXT, "Proceed to Checkout").click()
    dropdown = browser.find_element(By.NAME, "order.cardType")
    dropdown.find_element(By.XPATH, "//option[. = 'MasterCard']").click()

    browser.find_element(By.NAME, "newOrder").click()
    browser.find_element(By.LINK_TEXT, "Confirm").click()
    browser.save_screenshot("Confirmacion_compra.png")
    browser.find_element(By.LINK_TEXT, "Return to Main Menu").click()
    return

historia1()
historia2()
historia3()
historia4()
historia5()

time.sleep(10)




