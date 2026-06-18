import time
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

print('Verificando ControlPort...')
with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    status = controller.get_info('status/bootstrap-phase')
    print('ControlPort status:', status)

print('Creando Chrome driver con Tor proxy...')
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get('https://check.torproject.org/')
    time.sleep(5)
    print('Driver page title:', driver.title)
    print('URL loaded:', driver.current_url)
    print('Page source snippet:', driver.page_source[:200])
finally:
    driver.quit()
print('Selenium test finished successfully.')
