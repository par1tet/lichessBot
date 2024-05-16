from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep as slp
import lxml
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://lichess.org/')

def start_game_with_player(id):
    slp(0.4)
    pick_a_time_control(driver,id)
def pick_a_difficalty(driver: webdriver.Chrome):
    driver.find_element(By.XPATH, '')

def pick_a_time_control(driver: webdriver.Chrome,difficalty):
    select_varialbe = driver.find_element(By.XPATH, f'//*[@id="main-wrap"]/main/div[2]/div[2]/div[{difficalty}]')
    select_varialbe.click()

def return_board():
    while 'https://lichess.org/' == driver.current_url:
        slp(0.01)
    request = requests.get(driver.current_url)

    soup = BeautifulSoup(request.text,'lxml')

    board = soup.find_all('piece')
    board_arr = [[f'{i["class"][0]} {i["class"][1]}', int(float(((((i["style"]).split(";"))[0]).split(":")[1]).replace("%","")) / 12.5), int(float(((((i["style"]).split(";"))[1]).split(":")[1]).replace("%","")) / 12.5)] for i in board]


    board_map = []
    for i in range(8):
        board_map.append([])
        for k in range(8):
            board_map[-1].append('empty area')
            
    for i in range(8):
        for k in range(8):
            for p in board_arr:
                if p[1] == i and p[2] == k:
                    board_map[i][k] = p[0]
            
    for i in board_map:
        for k in i:
            print(k, end='\t')
        print('')
    pass
    return board_map