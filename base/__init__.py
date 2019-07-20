import sys

def bot_runner(bot_action_function):
    """
    Our chatbot is a cmd line interface hence, we use this method as base
    :param bot_action_function:
    :return:
    """
    while True:
        user_text = input("User :: ")
        if user_text == "exit":
            sys.exit(0)
        bot_text = bot_action_function(user_text)
        print("Bot :: " + bot_text)