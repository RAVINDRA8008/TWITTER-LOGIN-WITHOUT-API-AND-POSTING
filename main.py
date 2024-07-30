from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open Twitter/X login page
    driver.get('https://twitter.com/i/flow/login')
    wait = WebDriverWait(driver, 30)  # Increased timeout to 30 seconds for slower connections

    # Wait for the username field and enter the username
    username = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]'))
    )
    username.send_keys("USERNAME")  # Replace with your actual username

    # Simulate pressing the Enter key to proceed to the next step
    username.send_keys(Keys.RETURN)

    # Wait for the password field to be visible and enter the password
    password = wait.until(
        EC.presence_of_element_located((By.NAME, 'password'))
    )
    password.send_keys("PASSWORD")  # Replace with your actual password

    # Simulate pressing the Enter key to log in
    password.send_keys(Keys.RETURN)

    # Wait for the home page to load
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="AppTabBar_Home_Link"]'))
    )

    # Directly navigate to the compose post page
    driver.get('https://x.com/compose/post')

    # Wait for the rich text editor to be present
    tweet_text_area = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-offset-key]'))
    )

    # Use JavaScript to set the cursor and insert text
    tweet_text = "OM NAMO VENKATESHYA!!"
    script = """
    var element = arguments[0];
    var text = arguments[1];
    var range = document.createRange();
    var sel = window.getSelection();
    range.selectNodeContents(element);
    sel.removeAllRanges();
    sel.addRange(range);
    document.execCommand('insertText', false, text);
    """
    driver.execute_script(script, tweet_text_area, tweet_text)

    # Optionally, use sleep to ensure text insertion completes
    time.sleep(3)

    # Locate the file input element and upload the image
    file_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
    )
    file_path = r"C:\Users\ravin\OneDrive\Documents\TEST123.mp4"  # Replace with your actual file path
    file_input.send_keys(file_path)

    time.sleep(10)

    # Wait for the post button and click it
    post_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="tweetButton"]'))
    )
    post_button.click()

    time.sleep(4)
    print("Tweet posted successfully!")

finally:
    # Ensure the WebDriver is closed properly even if an error occurs
    driver.quit()
