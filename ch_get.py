from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys #estrazione bash
import time

#estrazione link
url = sys.argv[1]

# Imposta la variabile d'ambiente per il percorso del driver di Chrome
chrome_driver_path = "chrome/chromedriver(mac)"
os.environ['PATH'] += ":" + chrome_driver_path

# Opzioni del browser Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_extension('chrome/sniffer.crx')

# Inizializzazione del driver di Chrome
browser = webdriver.Chrome(options=chrome_options)

browser.get(url)

# Attendi il caricamento completo dell'estensione
wait_extension = WebDriverWait(browser, 20)
extension_loaded = wait_extension.until(EC.presence_of_element_located((By.ID, 'myM3u8LayerId')))

wait = WebDriverWait(browser, 20)
links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))

for link in links:
    try:
        href = link.get_attribute('href')
        if href and ('javascript:' not in href):

            #la condizione dell'if è il filtro dei vari link
            if href.startswith('https://tv1.ipslow.com/tv') or href.startswith('https://tv.ipslow.com/tv') or href.endswith('.m3u8') or href.startswith('https://playback2.akamaized'):
                print(href)  # Stampa il link se soddisfa i criteri
    except StaleElementReferenceException:
        print("Elemento non più valido, continuo con il prossimo elemento...")
        continue

time.sleep(6) #protezione anti ip-ban
browser.quit()