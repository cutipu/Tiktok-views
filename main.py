#public from NV
from playwright.sync_api import sync_playwright
import time
url = str(input("""[___________.__ __      __          __     ____   ____.__                     
\__    ___/|__|  | ___/  |_  ____ |  | __ \   \ /   /|__| ______  _  ________
  |    |   |  |  |/ /\   __\/  _ \|  |/ /  \   Y   / |  |/ __ \ \/ \/ /  ___/
  |    |   |  |    <  |  | (  <_> )    <    \     /  |  \  ___/\     /\___ \ 
  |____|   |__|__|_ \ |__|  \____/|__|_ \    \___/   |__|\___  >\/\_//____  >
                   \/                  \/                    \/           \/ ]""" "\ninput url："))
file_list = str(input("[#] socks4："))
pprr = open(file_list).readlines()

with sync_playwright() as p:
    for lines in list(pprr):
        proxy = lines.split(':')
        browser = p.firefox.launch(firefox_user_prefs={"security.cert_pinning.enforcement_level": 0, 
"security.tls.version.min": 1, 
"network.stricttransportsecurity.preloadlist": False, 
"network.proxy.socks": proxy[0],
"network.proxy.socks_port": int(proxy[1]), 
"network.proxy.socks_version": 4,
"network.proxy.type": 1,
"security.enterprise_roots.enabled": True,},
headless=True,
timeout=3000,
slow_mo=5000,
)
        page = browser.new_page()
        try:
                page.goto(url)
                time.sleep(15)
        except:
                pass
