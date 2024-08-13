import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
import random
import time
import pyautogui

# Сайт с телеканалами
url = "https://www.tvonline.ru/channels/"

# Получение списка телеканалов
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
channels = soup.find_all('a', class_='channel-link')

# Список ссылок на телеканалы
channel_urls = []
for channel in channels:
    channel_urls.append(channel.get('href'))

# Открытие браузера
pyautogui.press('win')
pyautogui.typewrite('https://www.tvonline.ru')
pyautogui.press('enter')

# Ожидание загрузки страницы
time.sleep(5)

while True:
    # Случайный выбор телеканала
    channel_url = random.choice(channel_urls)
    pyautogui.typewrite(channel_url)
    pyautogui.press('enter')

    # Ожидание загрузки телеканала
    time.sleep(1)

    # Переключение на полноэкранный режим
    pyautogui.press('f11')

    # Ожидание 1 секунды
    time.sleep(1)

    # Закрытие полноэкранного режима
    pyautogui.press('esc')
