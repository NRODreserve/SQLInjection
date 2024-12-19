from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
    def __init__(self, **properties):
        self.init_components(**properties)
        # Initialisiere die Ergebnisse
        self.label_result.text = ""

    def button_login_click(self, **event_args):
        # Eingaben sammeln
        username = self.text_box_1.text
        password = self.text_box_2.text

        # Anfrage an das Backend senden
        results = anvil.server.call('check_login', username, password)

        # Ergebnisse in der Label-Komponente anzeigen
        if results:
            # Liste der Konten und Beträge erstellen
            konten_texte = [f"Account {r['account_id']}: {r['balance']}€" for r in results]
            self.label_result.text = "\n".join(konten_texte)
        else:
            # Fehlermeldung anzeigen
            self.label_result.text = "Login fehlgeschlagen!"
