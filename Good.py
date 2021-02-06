import datetime

d = datetime.datetime.now()

for attr in ['hour']:
    (attr, ':', getattr(d, attr))

timenow = getattr(d, attr)

timemid = 12

morn = "Morning"
eve = "Evening"
mid = "Middle"

if timenow > timemid:
    timenow = eve
elif timenow < timemid:
    timenow = morn

print("please enter your name")
print("Good " + timenow + ", " + input())