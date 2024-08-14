import pyautogui
import time
import random
import webbrowser
 
# Список каналов
channel_urls = [
    "https://hd.kinopoisk.ru/channels?openedChannelId=4aecd6b37658480180d30b43d03ce502&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=49915b0d1520da79aa53f455c2cfa952&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=49d78328c2da6e63b7f3a16c8626862c&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=4e9950d2d2407a1387a532bdef4b3ebd&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=4bc29e0e11e8e43d967a080efa7aa1cc&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=405a75b4bf01b6d3a6e0a3aa29a12c70&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=44bacd2c139817b0802741d0e7e1f755&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=485e19b7beaf04a399e1990c9fcaa315&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=430beb8d7156a3e0b992546ef1dfba4a&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=49d798897233a2beacf95f9420c510cc&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=41a0f81e79c523d4a8e280aacc8b0e16&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=4984e085bc8e71ed8693d1071d5f5d3c&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=4eb40c4c15b3f1288f4fb53b20557fe0&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=4e4aa9676018adecb1dad8f3f8bda29f&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=49b5e09fcc46b6fbbf4ff72811a50239&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=4d95ed1fcbde66eda02d5262102b4c4d&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=44a6c897f0765abfa9257926b9dddddd&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=4d1d6979385d28ebab8faae66cd97d72&page=tv",
    "https://hd.kinopoisk.ru/channels?openedChannelId=4c5507619976c5fba5afa33c04583f0b&page=tv",
]
 
# Открываем браузер
for url in channel_urls:
    webbrowser.open(url)
    time.sleep(0.5)
 
# Ждем пока браузер откроется и все вкладки прогрузятся
time.sleep(10)
 
# Выключаем звук во всех вкладках
for _ in range(len(channel_urls)):
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(0.1)
    pyautogui.hotkey('m')
 
# Делаем случайное переключение между вкладками
while True:
    # Выбираем случайную вкладку
    tabs_count = len(channel_urls)
    tab_index = random.randint(0, tabs_count - 1)
 
    # Переключаемся на первую вкладку
    for _ in range(tabs_count):
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.1)
 
    # Переключаемся на случайную вкладку
    for _ in range(tab_index):
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.1)
 
    # Включаем звук в текущей вкладке
    pyautogui.hotkey('m')
 
    # Ждем 1 секунду
    time.sleep(1)
 
    # Выключаем звук в текущей вкладке
    pyautogui.hotkey('m')
