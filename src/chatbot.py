from tokinzation import tokenizer

while True:
    user_input = input("YOU:")

    if user_input.lower() == "exit" or user_input.lower() == "bye":
        print("Byeeeeeee")
        break

    tokenized_word = tokenizer(user_input)

    print(tokenized_word)

