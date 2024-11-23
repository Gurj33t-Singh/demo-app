from ._anvil_designer import AddDataTemplate
from anvil import *
import anvil.server
import stripe.checkout


class AddData(AddDataTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Collect data from all the UI fields (adjust field names as necessary)
    data = {
        "phone_number": self.phone_number.text,
        "field1": self.field_1.text,  # Assuming field1 is a TextBox
        "field2": self.field_2.text,  # Assuming field2 is a TextBox
        "field3": self.field_3.text,  # Assuming field3 is a TextBox
        "field4": self.field_4.text,  # Assuming field4 is a TextBox
        "field5": self.field_5.text,  # Assuming field5 is a TextBox
        "field6": self.field_6.text,  # Assuming field6 is a TextBox
        "field7": self.field_7.text,  # Assuming field7 is a TextBox
        "field8": self.field_8.text,  # Assuming field8 is a TextBox
        "field9": self.field_9.selected_value,  # Assuming field9 is a TextBox
        "field10": self.check_box_1.checked # Assuming field10 is a TextBox
    }
    
    # Send the data via POST request to the FastAPI backend
    url = "http://127.0.0.1:8082/create"  # Replace with your actual FastAPI endpoint URL
    
    response = anvil.http.request(url, method="POST", json=data)
    
    # Check the response and handle accordingly
    if response.status_code == 200:
        # Handle successful response
        print("Data sent successfully")
    else:
        # Handle error response
        print(f"Error: {response.status_code}, {response.text}")

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("ViewData")
