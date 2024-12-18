from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    # Überprüfen, ob die Textbox leer ist
    if not self.text_box_1.text.strip():  # strip() entfernt Leerzeichen
        # Fehlermeldung anzeigen, wenn die Textbox leer ist
        alert("Bitte füllen Sie das Textfeld aus!", title="Fehler")
    else:
        # Weiter mit der Anmeldung
        username = self.text_box_1.text
        # Hier kannst du die Anmelde-Logik hinzufügen
        print(f"Benutzername eingegeben: {username}")


