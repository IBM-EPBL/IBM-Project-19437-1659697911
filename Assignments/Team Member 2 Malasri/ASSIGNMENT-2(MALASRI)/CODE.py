import random


temp=random.randint(1,10)
humidity=random.randint(1,10)

print("temperature:",temp)
if temp > 5 and temp < 7:
    print("temperature is normal")
elif temp < 5:
    print("temperature is low")
else:
    print("temperature is  high")

print("Humidity:",humidity)
if humidity> 3 and humidity < 6:
    print("humidity is normal")
elif humidity < 3:
    print("humidity is low")
else:
    print("humidity is  high")


    
