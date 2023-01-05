import pywhatkit
import numpy

israel = "+972"
iteration = int(input("how many numbers you want to add?"))
message = input("enter your message \n")
print("the message you entered is " + message)
time = input("enter time when you want the message to be sent (08:33)")
time = time.split(":")
hour = (int)(time[0])  # getting only the hour
min = (int)(time[1])  # getting only the hour

a = [0 for x in range(iteration)]
arrLength = len(a)
print(len(a))
# send to multiple people
if (iteration > 1):
    for i in a:
        a[i] = str(input("enter number\n"))

    for i in a:
        pywhatkit.sendwhatmsg(israel + a[i], message, hour, min, 8, False, 3)

    # print("the number you entered is " + number[1:10])
# send to only one people
else:
    number = input("enter number\n")
    # print("the number you entered is "+number[1:10])
    pywhatkit.sendwhatmsg(israel + number, message, hour, min, 8, False, 3)
