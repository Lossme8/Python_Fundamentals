prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active_flag = True
# message = ""
# while message != 'quit':
while active_flag:
    message = input(prompt)

    # message = input(prompt)
    if message == 'quit':
        active_flag = False
    else:
        print(message)
