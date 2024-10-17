import time
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as gp

# Setup GPIO
gp.setmode(gp.BOARD)
led = 7
gp.setup(led, gp.OUT)

# Telegram bot token and chat ID
token = 'your_token_here'
id = 'your_chat_id_here'

# Initialize the bot
bot = telepot.Bot(token)
print(bot.getMe())

# Function to handle Telegram messages
def tel(msg):
    chat_id = msg['chat']['id']
    cmnd = msg['text'].lower()  # Make command case-insensitive
    
    if 'on' in cmnd:
        msgg = 'on'
        gp.output(led, True)
        time.sleep(2)
        msgg = 'LED is ' + msgg
        bot.sendMessage(chat_id, msgg)
        
    elif 'off' in cmnd:
        msgg = 'off'
        gp.output(led, False)
        msgg = 'LED is ' + msgg
        bot.sendMessage(chat_id, msgg)

# Start the message loop in the main thread
MessageLoop(bot, tel).run_as_thread()
print("Bot is listening...")

try:
    while True:
        time.sleep(10)  # Main loop sleep to prevent excessive CPU usage
except KeyboardInterrupt:
    print("Exiting...")
finally:
    gp.cleanup()  # Cleanup GPIO when exiting
