import subprocess
import os
from get_Answer import Fetcher

class Commander:
    def __init__(self):
        self.comfirm = ["yes", "sure", "do it", "confirm"]
        self.cancel = ["no", "wait", "don't", "cancel"]

    def discover(self, text):
        if "what" in text or "your name" in text:
            self.respond("My name is Commander. How are you")
        elif "launch" or "open" in text:
            app = text.split(" ", 1)[-1]
            self.respond("Openning "+app)
            os.system("open -a " + app +".app")
    
    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)
