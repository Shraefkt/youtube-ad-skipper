from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

try:
    pass
except KeyboardInterrupt:
    elem = driver.find_element_by_class_name("ytp-next-button ytp-button")
    elem.click()

while True:
    try:
        try:
            skip = driver.find_element_by_class_name("ytp-ad-skip-button-container")
            skip.click()
        except:
            continue
    except KeyboardInterrupt:
        elem = driver.find_element_by_class_name("ytp-next-button ytp-button")
        elem.click()
