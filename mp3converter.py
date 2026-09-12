from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
converter = "https://cnvmp3.com/v55"


# Get the list
with open("songs.txt", "r", encoding="utf-8") as file:
    content = file.readlines()
    song_list = []
    for i in content:
        stripped = i.strip()
        song_list.append(stripped)


for i in song_list:
    driver.get(f"https://www.youtube.com/results?search_query={i.replace(' ', '+')}")

    wait = WebDriverWait(driver, 60)

    first_video = wait.until(
        ec.presence_of_element_located((By.CSS_SELECTOR, "a#video-title"))
    )

    # Extract the href attribute
    video_url = first_video.get_attribute("href")


    # New tab
    driver.get(converter)


    # Find the input box
    input_box = wait.until(
        ec.presence_of_element_located((By.ID, 'video-url'))
    )
    input_box.send_keys(video_url)

    # Submit
    check = wait.until(
        ec.presence_of_element_located((By.ID, 'convert-button-1'))
    )
    check.click()

    # Wait for the download button to be clickable
    again = wait.until(
        ec.element_to_be_clickable((By.XPATH, '//*[@id="convert-again-btn"]'))
    )
