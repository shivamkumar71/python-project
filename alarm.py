import datetime
import time
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)


def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting....")
    alarm_trigered = False
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        
        if current_time == alarm_time:
            print("Wake up! it's time!")
            end_time = time.time()+60 # 60 second from now
            alarm_trigered = True
            
            while time.time() < end_time:
                engine.say("Wake up! it's time!")
                
            engine.runAndWait()
            
            break
        time.sleep(1)


alarm_time = "21:38"
alarm_clock(alarm_time)