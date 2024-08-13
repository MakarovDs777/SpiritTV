import schedule
import time

def switch_channel():
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

schedule.every(1).seconds.do(switch_channel)  # переключать телеканал каждую секунду

while True:
    schedule.run_pending()
    time.sleep(1)
