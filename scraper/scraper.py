from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

def scrape_data(share_link, timeout=10, headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(share_link)

    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-message-author-role]'))
        )
        print("Page loaded")
    except:
        print("Timeout: Tidak bisa memuat halaman.")
        driver.quit()
        return {"error": "Gagal mengambil data"}

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    user_chat = [msg.get_text().strip() for msg in soup.find_all("div", attrs={"data-message-author-role": "user"})]
    assistant_chat = [msg.get_text().strip() for msg in soup.find_all("div", attrs={"data-message-author-role": "assistant"})]

    driver.quit()

    conversation = []
    for i in range(len(user_chat)):
        conversation.append({"role": "user", "text": user_chat[i]})
        if i < len(assistant_chat):
            conversation.append({"role": "assistant", "text": assistant_chat[i]})

    return conversation if conversation else {"error": "Tidak ada percakapan ditemukan"}