import os
import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import keyboard
import re



class Browser:
    def __init__(self):
        self.driver = []
        self.lobby_table = []

    def open(self):
        dirr = os.path.abspath(os.curdir).rsplit("\\", 1)[0] + "\\userdata"
        options = Options()
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-gpu")
        options.add_argument("excludeSwitches")
        options.add_argument(r"user-data-dir={}".format(dirr))
        options.add_experimental_option(
            "excludeSwitches", ['enable-automation', 'enable-logging'])
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--remote-debugging-port=9222")
        # options.add_experimental_option("debuggerAddress", "127.0.0.1:9230")

        self.driver = webdriver.Chrome(
            chromedriver_autoinstaller.install(), options=options)
        # driver.maximize_window()

        self.driver.get('https://bc.game/crash')
        time.sleep(5)

        os.system('cls')

        print("\033[95m" + "=== INFO ===" + "\033[0m")
        print("\033[95m" +
              "After you login, Press 'Passkey' to continue" + "\033[0m")
        print("\033[95m" + "=== BC GAME CRASH ===" + "\033[0m")

        while True:
            if keyboard.is_pressed("0"):
                print("\nQ: pressed continuing...")
                break
        print("Betnomi star bot ver.1.0")
        self.driver.implicitly_wait(30)
        open("results.html", "w", encoding="utf8").write(
            self.driver.page_source)

        # frame = self.single_item('//iframe[@id="game"]')
        # self.driver.switch_to.frame(frame)

    def single_item(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath)
        except:
            print("Item doesn't exist :", xpath)
        return None

    def multi_items(self, xpath):
        try:
            return self.driver.find_elements(By.XPATH, xpath)
        except:
            print("Item doesn't exist :", xpath)
        return None

    def click_item(self, xpath):
        try:
            self.single_item(xpath).click()
        except:
            print("None clickable :", xpath)

    def sub_item(self, item, xpath):
        return item.find_element(By.XPATH, xpath)

    def get_history_numbers(self):
        ii = 0
        flag = False
        _series_que = [{"id":0, "value":100}, {"id":1, "value":100}]
        index = len(self.multi_items(f'/html/body/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div') )
        
        while True:
            _series_que[ii].clear()
            

            try:
                _series_que[ii]["id"] = int(self.single_item(f'/html/body/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[{index}]/div[1]').text)
                _series_que[ii]["value"]= int(100*(0.001+float(self.single_item(f'/html/body/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[{index}]/div[2]').text.replace("x",''))))
            except:
                time.sleep(0.5)
                continue

            
            ii = (ii+1) % 2
            if flag and _series_que[0]["id"] == _series_que[1]["id"] and _series_que[0]["value"] == _series_que[1]["value"]:
                # print(_series_que[0])
                return _series_que[0].copy()
            flag = True
            time.sleep(0.2)

    def click_bet(self):
        self.click_item( f'/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div/button')
        

    def click_plus(self):
        self.click_item(
            '/html/body/div/ul/li[7]/ul/li[1]/ul/li[1]/div[2]/button[2]')

    def get_balance(self):
        try:
            dollar = self.single_item(
                '/html/body/div/ul/li[3]/div/ul/li[2]/div/p/span[2]').text

        except:
            dollar = "Money 0.00"
        dollar = dollar.replace(',', '')
        return float(re.findall('[0-9.]+', dollar)[0])

    def set_bet_amount(self, dollar):
        bet_fa = self.single_item(
            f'/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/input')
            
        pp = 5
        while pp:
            bet_fa.send_keys(chr(127))
            bet_fa.send_keys(chr(8))
            pp -= 1
        xx = str(round(dollar, 6));
        print(xx)
        bet_fa.send_keys(xx)

    def set_ratio_amount(self, ratio):
        _index = 2
        while _index > 0:
            bet_fa = self.single_item(
                f'/html/body/div/ul/li[7]/ul/li[{_index}]/ul/li[5]/div/input')
            _index -= 1
            pp = 5
            while pp:
                bet_fa.send_keys(chr(127))
                bet_fa.send_keys(chr(8))

                pp -= 1
            bet_fa.send_keys(str(round(ratio, 3)))


# browser = Browser()
# browser.open('https://casino.bet365.com/Play/LiveRoulette')
