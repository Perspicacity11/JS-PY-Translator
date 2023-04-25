import openai
openai.api_key = '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' # GET A NEW KEY AS THIS ONE WAS DEACTIVATED (CAN'T BE PUBLIC IN COMMITS)
messages = [ {"role": "system", "content":
              "You are an intelligent assistant."} ]
while True:
    message = input("User : ")
    # I need to configure this message variable to receive form input from the view
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    # I need to output the reply variable into the view
    messages.append({"role": "assistant", "content": reply})