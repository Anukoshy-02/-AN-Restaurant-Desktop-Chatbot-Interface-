import customtkinter as ctk
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
app=ctk.CTk()
app.geometry("600*400")
app.title("welcome to AN restaurant")
entry = ctk.CTkEntry(app, width=500, font=("Arial", 14))
entry.pack(pady=20)
# Label for bot response
label = ctk.CTkLabel(app, text="Hello! Ask me anything about the restaurant ", font=("Arial", 16), wraplength=500, justify="left")
label.pack(pady=20)
def onclick():
    queries=entry.get()
    if("hi" in queries or "hello" in queries ):
        label.configure(text="welcome to our restaurant! How can i assist you today?")
    elif("menu" in queries):
        label.configure(text="we serve biriyani,noodles,pasta,desserts")
    elif("what are your timings" in queries):
        label.configure(text="we are open from 12pm to 11 pm,all days of the week")
    elif("home delivery "in queries):
        label.configure(text="yes,we deliver through zomato and swiggy")
    elif("thanks " in queries or "exit" in queries or "bye" in queries):
        label.configure(text="Thanks for visting!Have a great day")
    else:
        label.configure(text="I'm sorry,i didn't understand that,can you ask something else")
send_button = ctk.CTkButton(app, text="Send", command=onclick)
send_button.pack(pady=10)
app.mainloop()