from ._anvil_designer import ViewDataTemplate
from anvil import *
import anvil.server
import stripe.checkout


class ViewData(ViewDataTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the search button is clicked"""
    
    # Get the phone number input from the UI
    phone_number = self.phone_number_1.text if self.phone_number_1.text else None
    
    # Define the page size for pagination
    page_size = 10  # or you can fetch this from UI (e.g., a dropdown)

    def call_api_search(phone_number=None, size=10):
        """
        Calls the FastAPI search endpoint and returns the data.
        """
        url = "http://127.0.0.1:8082/search"  # Replace with your FastAPI server URL
        params = {"phone_number": phone_number, "size": size}
        
        # Use requests or anvil.http to make the API call
        response = anvil.http.request(url, method="POST", params=params)
        
        if response.status_code == 200:
            return response.json()  # Return the data as a list of records
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
    
    # Call the search API and get data
    try:
        data = call_api_search(phone_number=phone_number, size=page_size)
        
        # Display data in the data grid
        self.data_grid_1.items = data  # Set the grid's items to the result

    except Exception as e:
        # Show an error message if something goes wrong
        print(f"Error: {str(e)}")

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("AddData")
