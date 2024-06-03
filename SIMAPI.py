import time
from whatsapp_api import WhatsAppAPI  # Assuming you have a WhatsApp API wrapper

class SIMCard:
    def __init__(self, credit):
        self.credit = credit
    
    def deduct_credit(self, amount):
        if self.credit >= amount:
            self.credit -= amount
            return True
        else:
            return False

class WhatsAppWithSIM:
    def __init__(self, sim_card):
        self.sim_card = sim_card
        self.whatsapp_api = WhatsAppAPI()  # Initialize WhatsApp API
    
    def send_message(self, contact, message):
        # Simulating sending message via WhatsApp
        self.whatsapp_api.send_message(contact, message)
        time.sleep(2)  # Simulating network delay
    
    def send_message_without_internet(self, contact, message):
        if self.sim_card.deduct_credit(1):  # Assuming 1 credit is deducted for each message
            self.send_message(contact, message)
        else:
            print("Insufficient credit. Cannot send message.")

# Usage
sim_card = SIMCard(10)  # Assume starting credit is 10
whatsapp_with_sim = WhatsAppWithSIM(sim_card)

# Sending message with internet
whatsapp_with_sim.send_message("Osama", "Hello Osama, how are you?")

# Sending message without internet
whatsapp_with_sim.send_message_without_internet("Osama", "Hello Osama, how are you?")
