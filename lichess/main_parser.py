from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep as slp

def start_game_with_player():
    driver = webdriver.Chrome()
    driver.get('https://lichess.org/')

    slp(0.25)
    pick_a_time_control(driver,input())

    input()
    
    driver.quit()
    
def pick_a_difficalty(driver: webdriver.Chrome):
    driver.find_element(By.XPATH, '')

def pick_a_time_control(driver: webdriver.Chrome,difficalty):
    select_varialbe = driver.find_element(By.XPATH, f'//*[@id="main-wrap"]/main/div[2]/div[2]/div[{difficalty}]')
    select_varialbe.click()
