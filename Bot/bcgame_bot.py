from glob import glob
from my_browser import Browser
import time
from time import gmtime, strftime
import xml.etree.ElementTree as ET
import random
import keyboard


global browser
global glist
global gameMode
global type_cnt
global my_threshold
global start_pos
global auto_ratio
global inc_rate
global max_betno
global pri_amount
global outputMode

glist = []

my_threshold = []
auto_ratio = []
start_pos = []
inc_rate  = []
max_betno = []
pri_amount = []




##################################################
###########  Temorary input Function #############
global ppp
ppp = 0




#######     Generate the Ouptput File ##############
filename =  strftime("%Y_%m_%d_%H_%M_%S", gmtime())
filename = f"./data/series_{filename}.csv"

with open(filename, 'w+') as f:
    f.close()
####################################################




prev_id = None
def appeared_new_number():
    global prev_id
    while True:
        pp = browser.get_history_numbers()
        if prev_id!=pp["id"]:
            prev_id = pp["id"]
            print(pp)
            return pp["value"]
            
def read_parameters_from_file():
    global type_cnt
    global gameMode
    global my_threshold
    global start_pos
    global auto_ratio
    global inc_rate 
    global max_betno
    global pri_amount
    global outputMode
    
    my_threshold = []
    start_pos = []
    auto_ratio = []
    inc_rate  = []
    max_betno = []
    pri_amount = []

    myXMLtree = ET.parse('params_config.xml')
    
    
    _gameMode = myXMLtree.find('gameMode').text
    if 'BACKTEST' in _gameMode:
        gameMode = 'BACKTEST'
    elif 'REALGAME' in _gameMode:
        gameMode = 'REALGAME'
    else:
        gameMode = 'READONLY'
        
    # <outputMode> TELEGRAM </outputMode>
    
    _outputMode = myXMLtree.find('outputMode').text
    if 'TELEGRAM' in _outputMode:
        outputMode = 'TELEGRAM'
    else:
        outputMode = 'CONSOLE'
    
    
    type_cnt = int(myXMLtree.find('Count').text)
    
    for _index in range(type_cnt):
        x = myXMLtree.find(f'Type{_index}')
        start_pos.append( int(x.find('startPoint').text))
        max_betno.append( int(x.find('maxBetNumber').text))
        pri_amount.append( float(x.find('primaryPrice').text))
        auto_ratio.append( float(x.find('profitRatio').text))
        my_threshold.append( int(x.find('threshold').text))
        inc_rate.append( float(x.find('incBetRate').text))
        
    


def save_new_number_to_file(_num):
    global filename
    
    with open(filename, 'a') as f: ##   save first input of series
        f.write(str(_num) + '\n')
        f.close()


def startProcess():
    global browser
    global glist
    global start_pos
    global gameMode
    global my_threshold
    global auto_ratio
    global inc_rate
    global outputMode
    
    
    
    if gameMode!='BACKTEST':
        browser = Browser()
        browser.open()
    
    bet_amount=100
    
    while True:
        read_parameters_from_file()
        new_value = appeared_new_number()
        # save_new_number_to_file( )
        print("new number is " , new_value)



        bet_amount += 1
        browser.set_bet_amount(bet_amount)
        time.sleep(1)
        browser.click_bet()  ##################  click the bet button.


if __name__ == "__main__":
    read_parameters_from_file()
    startProcess()
