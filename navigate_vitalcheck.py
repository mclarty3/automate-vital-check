import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def GetWebPage(link):
    # Open the VitalCheck page at specified URL; find and click "No to all above" button

    option = webdriver.ChromeOptions()
    option.add_argument('headless')                                        # Don't open the webdriver browser
    option.add_experimental_option('excludeSwitches', ['enable-logging'])  # Prevent terminal logging
    driver = webdriver.Chrome(options=option)

    driver.get(link)  # Open the VitalCheck page

    try:
        button = driver.find_element_by_xpath("//button[@class='btn btn-lg btn-success btn-block language ENGLISH']")
        button.click()  # Click the button to complete the screening
    except Exception as e:
        print("Error:", str(e))
        return False

    driver.close()
    return True
