import os
import gspread
from gspread.models import Cell
from oauth2client.service_account import ServiceAccountCredentials
from GoogleSheets.tools import config_parser


# use creds to create a client to interact with the Google Drive API
scope = ['https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/spreadsheets']
module_name = config_parser.get("config", "module_name")
client_secret_json = config_parser.get("config", "client_secret_json")
path_to_secret_json = os.path.join(module_name, client_secret_json)
creds = ServiceAccountCredentials.from_json_keyfile_name(
    path_to_secret_json, scope)
client = gspread.authorize(creds)

# Create sheet object
sheet = client.open_by_key(config_parser.get("config", "spreadsheet_id"))

sheet_1 = sheet.get_worksheet(0)
sheet_2 = sheet.get_worksheet(1)
sheet_3 = sheet.get_worksheet(2)


def update_status_cell():
    value = config_parser.get("config", "status_cell_value")
    label = config_parser.get("config", "status_cell_label")
    sheet_1.update_acell(label, value)
