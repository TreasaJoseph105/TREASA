user=input("you:").lower()
bot="" #response variable
if user=="hi":
    bot="hello"
elif user=="hello":
    bot="hello"
elif user=="name":
    bot="i am simple chatbot"
elif user=="bye":
    bot="goodbye have a great day"
else:
    bot="i dont understand"
print("Bot:",bot)