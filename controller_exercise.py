import random
import time

class Controller():
    def __init__(self,tv_status="close",tv_sound=5, channels = ["CNN"], channel="CNN"):
        self.tv_status = tv_status
        self.tv_sound = tv_sound
        self.channels = channels
        self.channel = channel


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
            answer = input("Please press '<' button to decrease sound or press '>' button to increase sound: ")

            if(answer == "<"):
                if(self.tv_sound != 0):
                    self.tv_sound -= 1
                    print("Sound: {}".format(self.tv_sound))
                else:
                    print("Sound cannot decrease anymore")
            elif (answer == ">"):
                if(self.tv_sound != 25):
                    self.tv_sound += 1
                    print("Sound: {}".format(self.tv_sound))
                else:
                    print("Sound cannot increase anymore")
            elif (answer == "q" or answer == "Q"):
                break

    def add_channel(self,channel_name):

        print("Channel is adding right now")

        time.sleep(1)
        self.channels.append(channel_name)

    def random_channel(self):

        random1 = random.randint(0, len(self.channels)-1)

        self.channel = self.channels[random1]

        print("Current Channel: {}".format(self.channel))

    def __len__(self):
        return len(self.channels)

    def __str__(self):

        return "TV status: {}\nTV Sound: {}\nCurrent Channel: {}\nChannels: {}".format(self.tv_status,self.tv_sound,self.channel,self.channels)




    print("""
    WELCOME TO TV PROGRAM
    
    1- OPEN TV
    
    2- CLOSE TV

    3- SOUND
    
    4- ADD CHANNEL
    
    5- RANDOM CHANNEL
    
    6- NUMBER OF CHANNELS
    
    7- TV INFORMATIONS
    
    """)

controller = Controller()

while True:

    operation = input("Choose the operation: ")

    if (operation == "q"):
        print("Goodbye")
        time.sleep(2)
        break
    elif (operation == "1"):
        controller.open_tv()

    elif (operation == "2"):
        controller.close_tv()

    elif (operation == "3"):
        controller.sound_settings()

    elif (operation == "4"):

        answer = input("enter channel names separated by ',': ")

        channel_list = answer.split(",")
        for i in channel_list:
            controller.add_channel(i)

    elif (operation == "5"):
        controller.random_channel()

    elif (operation == "6"):
        print("Number of channel: {} ".format(controller.__len__()))

    elif (operation == "7"):
        print(controller)




