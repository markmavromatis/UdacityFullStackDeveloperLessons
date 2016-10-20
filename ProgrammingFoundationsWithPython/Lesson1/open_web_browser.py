import webbrowser
import time

url = 'http://www.python.org/'

# Open URL in a new tab, if a browser window is already open.
# webbrowser.open_new_tab(url + 'doc/')

# Open URL in new window, raising the window if possible.
for x in range(3):
    time.sleep(3)
    webbrowser.open_new(url)
