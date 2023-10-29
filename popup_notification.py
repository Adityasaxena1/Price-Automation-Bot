from PyQt5.QtWidgets import QApplication, QMessageBox

app = QApplication([])


def pop_ups(mod_id, difference, ours, other_price):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setWindowTitle("Price Alert!")
    msg_box.setText(f"Price difference for Model ID {mod_id} is ₹{difference}\n"
                    f"Our Price: ₹{ours}\n"
                    f"Offer Price: ₹{other_price}\n"
                    f"Do you want to make our price equal to Offer Price? \n"
                    f"Choose 'yes' or 'no' ")
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    result = msg_box.exec_()

    if result == QMessageBox.Yes:
        return True
    else:
        return False
