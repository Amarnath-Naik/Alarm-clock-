from datetime import datetime
from playsound import playsound
alram_time = input("enter the time of alarm to be set:HH:MM:SS\n") # here take input as HH:MM:SS

alram_hour = alram_time[0:2]     # here asign the 1st two index(0 and 1) values of the input - HH
alram_minute = alram_time[3:5]   # here asign the 2nd two index(3 and 4) values of the input - MM
alram_seconds = alram_time[6:8]  # here asign the 3rd two index(6 and 7) values of the input - SS

print("setting up alarm..")
while True:            #this loop for check the time value match or not for every second 

    now = datetime.now()
    
    current_hour = now.strftime("%H")    # here asign the current time 
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S")
    
    if alram_hour == current_hour:
        if alram_minute == current_minutes:
            if alram_seconds == current_seconds:
                print("⏲️  playing alarm...")
                playsound('C:\\Users\\amarn\\Music\\sound effect pack\\Phone Ringing.mp3')
                break    #for break the loop after match the time values# project
                #done
