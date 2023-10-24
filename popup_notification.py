from tkinter import messagebox


class MessageBox:
    def __init__(self):
        pass

    def pop_ups(self, mod_id, difference, ours, other_price):
        choice = messagebox.askyesno(title="Price Alert!",
                                     message=f"Price difference for Model ID {mod_id} is ₹{difference}\n"
                                             f"Our Price: ₹{ours}\n"
                                             f"Other's Price: ₹{other_price}\n"
                                             f"Do you want to make our price decrease by ₹1 than other's? \n"
                                             f" Choose 'yes' or 'no' ")
        return choice
