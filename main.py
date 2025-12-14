from datetime import datetime
from babel import Locale
from playwright.sync_api import Page, expect,sync_playwright



locale = Locale('it')

current_month_text = datetime.now().strftime('%m') 
current_day_text = datetime.now().strftime('%d') 
current_year_text = datetime.now().strftime('%y') 
month_names = locale.months['format']['abbreviated']
month_abbreviated=month_names[int(current_month_text)]

finaldas=current_day_text+month_abbreviated+current_year_text
print(finaldas)

with sync_playwright() as p:
    context = p.firefox.launch_persistent_context(
        user_data_dir="C:/Users/akrom/OneDrive/Desktop/autoclick-the-autoclick/playwright-firefox-profile",
        headless=False
    )
    
    page = context.new_page()
    page.goto("https://puntateaste.it/")
    page.wait_for_selector("#seconds_0")
    page.fill("#seconds_0", "2")
    page.wait_for_selector("#auto0")
    page.click("#auto0")

    page.wait_for_timeout(200000)