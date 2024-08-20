import time

import pyautogui
from pyvirtualdisplay import Display
from selenium import webdriver

# Start virtual display
display = Display(visible=0, size=(1024, 768))
display.start()

# Initialize Selenium WebDriver
driver = webdriver.Firefox()

try:
    # Navigate to a website
    driver.get("https://www.example.com")

    # Wait for page to load
    time.sleep(5)

    # Perform PyAutoGUI actions
    pyautogui.moveTo(100, 100)
    pos = pyautogui.position()
    print("POSITION ", pos )
    pyautogui.click()

    # Take a screenshot
    pyautogui.screenshot("screenshot.png")

    print("Actions completed successfully")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Clean up
    driver.quit()
    display.stop()