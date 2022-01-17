import random

name = "Bot 8765"
responses = {
    "what's your name?": [
        "They call me{}".format(name),
        "i am {}".format(name),
        "i go by {}".format(name),
        "you can call me {}".format(name),
        f"it's okay if you call me {name}"
    ],
    "default": "This is the default message"
}
weather = "sunny"
mood = "happy"
resp = {
    "what is your name": [
        "They call me{}".format(name),
        "i am {}".format(name),
        "i go by {}".format(name),
        "you can call me {}".format(name),
        f"it's okay if you call me {name}",
    ],
    "what is today's weather?": [
        "The weather is {}".format(weather),
        "it is {} today".format(weather)
    ],
    "how are you?": [
        "i am {}".format(mood),
        "it's lovely today so i am {}".format(name),
        "{}".format(mood)
    ],
    "": [
        "hi, Are you there?",
        "what do you mean by these."
    ],
    "stop": [
        "alright",
        "okay",
        "bye"
    ],
    "exit": [
        "alright",
        "okay",
        "bye"
    ],
    "end": [
        "alright",
        "okay",
        "bye"
    ],
    "default": [
        "i'm not programmed to answer this question"
    ]
}


def res(message):
    if message in resp:
        bot_message = random.choice(resp[message])
    else:
        bot_message = random.choice(resp["default"])
    return bot_message


def real_text(user_text):
    if "name" in user_text:
        expected_text = "what is your name"
    elif "weather" in user_text:
        expected_text = "what is today's weather"
    elif "how are" in user_text:
        expected_text = "how are you?"
    elif "end" in user_text:
        expected_text = "end"
    elif "stop" in user_text:
        expected_text = "stop"
    elif "exit" in user_text:
        expected_text = "exit"
    else:
        expected_text = ""
    return expected_text


def send_message(message):
    response = res(message)
    print(response)


while True:
    my_input = input("Enter question for bot: ")
    my_input = my_input.lower()
    related_text = real_text(my_input)
    send_message(related_text)
    if my_input == "exit" or my_input == "end" or my_input == "stop":
        break
