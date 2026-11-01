def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)


messages = ["Hi!", "On my way.", "See you soon."]
sent_messages = []

send_messages(messages[:], sent_messages)   # kirim salinan

print(messages)         # list asli tetap berisi
print(sent_messages)    # ['Hi!', 'On my way.', 'See you soon.']