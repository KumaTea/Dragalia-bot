from io import BytesIO
from time import sleep
from botSession import driver


def get_screenshot(url, delay=1):
    driver.get(url)
    if 'nga' in url:
        images = driver.find_elements_by_xpath('//button[normalize-space()="显示图片"]')
        if len(images) == 1:
            images[0].click()
    sleep(delay)
    screenshot = driver.get_screenshot_as_png()
    return BytesIO(screenshot)


def reset_browser():
    driver.get('about:blank')
    return True
