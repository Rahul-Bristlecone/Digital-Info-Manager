import webbrowser
hi_intent=["Hi","Hello","Whats up","Howdy"]

msg=input("Start Chatting")
search=msg.split()

chat=True
while chat:
    if msg in hi_intent:
        print("Hello")
    elif msg=="bye":
        print("See You Soon")
    elif search[0]=="open":
        webbrowser.open(search[-1]+'.com')
    else:
        print("I did not get you, Please Try Again")
    chat=False