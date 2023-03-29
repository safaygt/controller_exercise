import random
import time

class Controller():
    def __init__(self,tv_status="close",tv_sound=5,channels=["CNN,NTV,BLOOMBERG,FOX"]):
        self.tv_status = tv_status
        self.tv_sound = tv_sound
        self.channels = channels

    def open_tv(self):
        if(self.tv_status == "close"):
            print("TV is opening now")
            time.sleep(2)
            self.tv_status = "open"
        else:
            print("TV is already open")

    def close_tv(self):
        if (self.tv_status == "open"):
            print("TV is closing now")
            time.sleep(2)
            self.tv_status = "close"
        else:
            print("TV is already close")
    def sound_settings(self):
        while True:
            answer = input("Please press '<' button to decrease sound or press '>' button to increase sound.")

            if(answer == "<"):
                if(self.tv_sound != 0):
                    self.tv_sound -= 1
                    print("Sound: {}".format(self.tv_sound))
            elif (answer == ">"):
                if(self.tv_sound != 25):
                    self.tv_sound += 1
                    print("Sound: {}".format(self.tv_sound))
            elif (answer == "q" or answer == "Q"):
                break

