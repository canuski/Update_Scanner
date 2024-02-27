# Update_Scanner
This app get info from windows about the latest updates and sends a message on boot with any newly realsed updates to telegram.

I was tired of pressing the windows update checker multiple time a day and waiting for it to load, so I built this small app to do it for me. Add the .bat file into C:\Users\<your-username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup and it'll run every time windows gets booted.

You also need to make a telegram bot and add the chat-id into a secrets.py file.
