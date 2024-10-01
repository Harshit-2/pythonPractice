# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

import time
from plyer import notification

while (True):
    notification_title = 'DRINK WATER!'
    notification_message = "Stay hydrated and healthy! It's time to take a break and have a refreshing glass of water."

    notification.notify(
        title=notification_title,
        message=notification_message,
        app_icon=None,
        timeout=10,
        toast=False
    )
    
    time.sleep(3600)
