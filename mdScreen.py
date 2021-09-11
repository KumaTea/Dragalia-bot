from io import BytesIO
from time import sleep
from botSession import driver


def get_screenshot(url, delay=1):
    driver.get(url)
    sleep(delay)
    screenshot = driver.get_screenshot_as_png()
    return BytesIO(screenshot)
