import os
from dotenv import load_dotenv

from skpy import SkypeEventLoop, SkypeNewMessageEvent

load_dotenv()

username = os.environ.get('SKYPE_USERNAME')
password = os.environ.get('SKYPE_PASSWORD')
skype_id = os.environ.get('SKYPE_ID')

class SkypePing(SkypeEventLoop):
    def onEvent(self, event):
        # return if it is not an MessageEvent
        if not isinstance(event, SkypeNewMessageEvent):
            return
        
        # return if it is my own message
        if event.msg.userId == self.userId:
            return

        if "ping" in event.msg.plain.lower():
            event.msg.chat.sendMsg("Pong!")
        if '@'+skype_id in event.msg.plain:
            event.msg.chat.sendMsg("At your service!")

if __name__ == "__main__":
    sk = SkypePing(username, password, autoAck=True)

    # sk.subscribePresence() # Only if you need contact presence events.
    
    sk.loop()
