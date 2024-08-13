# Random-switch-of-TV-channels

This program uses the requests library to get a list of TV channels from the site, the BeautifulSoup library for parsing an HTML page, and the pyautogui library to simulate user actions in the browser. The program randomly selects a TV channel from the list, opens it in the browser, switches to full-screen mode, waits 1 second and closes full-screen mode.

Please note that this program may not work correctly on all websites and browsers. In addition, it may violate the rules of use of the site, so use it at your own risk.

Also, in order for the program to work correctly, you need to install the pyautogui library and configure the browser so that it opens links in a new tab.

To add the function of switching TV channels every second, you can use the schedule library to schedule tasks.
