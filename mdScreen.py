from io import BytesIO
from time import sleep
from botSession import driver, logger


def get_screenshot(url, delay=1):
    try:
        logger.debug("Getting: %s" % url)
        driver.get(url)
        if 'nga' in url:
            images = driver.find_elements_by_xpath('//button[normalize-space()="显示图片"]')
            for image in images:
                try:
                    image.click()
                except:
                    pass
        sleep(delay)
        driver.execute_script("window.scrollTo(0, 0);")  # scroll to top
        screenshot = driver.get_screenshot_as_png()
        driver.close()
        return BytesIO(screenshot)
    except:
        return None
