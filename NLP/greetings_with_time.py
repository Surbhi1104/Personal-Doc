import random
from datetime import datetime
h=int(datetime.now().strftime('%H'))
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello"]
if(h<=12):
    s="Good morning"
elif(h<=16):
    s="Good afternoon"
elif(h<=20):
    s="Good evening"
else:
    s="Good night"
print(random.choice(GREETING_RESPONSES),s)
print("It's my pleasure talking you")
