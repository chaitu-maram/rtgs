from django.conf import settings
import gspread
from google.oauth2.service_account import Credentials

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(settings.GSHEETS_CREDS_FILE, scopes=scope)
client = gspread.authorize(creds)
sh = client.open_by_key(settings.GSHEETS_SHEET_ID)


def append_row_to_sheet(tab_name, row_data):
    """
    Append a row to the given tab (worksheet) by name.
    :param tab_name: str, the worksheet/tab name (e.g., "Axis Bank" or "Union Bank")
    :param row_data: list, the row values in the right order
    """
    try:
        ws = sh.worksheet(tab_name)   # Open specific tab
        ws.append_row(row_data)
        return True
    except Exception as e:
        print("Error appending row:", e)
        return False
