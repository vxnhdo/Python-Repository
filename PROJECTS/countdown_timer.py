import time # to use time.sleep()

my_time = int(input("Enter the time in seconds: "))

for i in range(my_time, 0, -1): # creates a countdown loop that starts from my_time and goes down to 1, decreasing by 1 each time.

    seconds = i % 60 # 'i' modulus 60 = counts the extra seconds after minutes has been taken out

    mins = int(i/60) % 60 # convert seconds into minutes then modulus 60 (hours) = remaining minutes

    hours = int(i/3600) # divide by 3600 seconds bc its equal to 1 hr

    print(f"{hours}:02:{mins:02}:{seconds:02}")
    
    time.sleep(1) # Pauses program for 1 second before continuing

print("Time is up!")
