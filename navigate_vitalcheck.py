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
        obscuringHelpMeBox = driver.find_elements_by_xpath("//div[@class='pull-right help-me-box col-md-4 col-sm-8 col-xs-12']")

        if len(obscuringHelpMeBox) != 0:
            print("Hiding help me box")
            driver.execute_script("arguments[0].style.visibility='hidden'", obscuringHelpMeBox[0])

        button.click()  # Click the button to complete the screening
    except Exception as e:
        print("Error:", str(e))
        return False


    driver.close()
    return True
