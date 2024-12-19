from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
    
    def button_login_click(self, **event_args):
        # Nimmt Eingaben des Benutzers
        username = self.text_box_1.text
        password = self.text_box_2.text

        # Senden der Daten an das Server-Modul
        result = anvil.server.call('check_login', username, password)

        # Anzeigen der Rückgabe
        if result:
            self.label_result.text = f"Willkommen! Dein Kontostand beträgt: {result['balance']}€"
        else:
            self.label_result.text = "Login fehlgeschlagen!"
