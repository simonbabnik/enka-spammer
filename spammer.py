from selenium import webdriver
from selenium.webdriver.common.keys import Keys

for i in range(10):
    url = "https://1ka.arnes.si/a/18591"

    driver = webdriver.Chrome()
    driver.get(url)

    # prva stran
    elem = driver.find_element_by_xpath('//*[@id="container"]/form/div[2]/input')
    elem.click()

    # druga stran
    elem = driver.find_element_by_xpath('//*[@id="spremenljivka_432396_vrednost_1317171"]')
    elem.click()

    elem.send_keys(Keys.RETURN)

    # zadnja stran
    zenska = driver.find_element_by_xpath('//*[@id="spremenljivka_387487_vrednost_1134443"]')
    zenska.click()

    starost = driver.find_element_by_xpath('//*[@id="spremenljivka_387489_vrednost_1134448"]')
    starost.click()

    doktorat = driver.find_element_by_xpath('//*[@id="spremenljivka_387497_vrednost_1134478"]')
    doktorat.click()

    osrednjeslovenska = driver.find_element_by_xpath('//*[@id="spremenljivka_387503_vrednost_1134522"]')
    osrednjeslovenska.click()

    zakljuci = driver.find_element_by_xpath('//*[@id="buttons_gru_89939"]/input[2]')
    zakljuci.click()

    konec = driver.find_element_by_xpath('//*[@id="container"]/div[3]/input[2]')
    konec.click()

    #driver.close()

    i += 1
