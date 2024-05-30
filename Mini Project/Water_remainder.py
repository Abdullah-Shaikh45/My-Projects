import time
from plyer import notification

if __name__ == '__main__':
    notification.notify(
        title = "Drink Water Please!",
        message = "Water is beneficial for health",
        app_icon = r"C:\Users\Abdullah Shaikh\OneDrive\Desktop\Projects\icon1.ico",
        timeout = 10 
    )