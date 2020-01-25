
import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

import gspread
import json

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

class GoogleItem:
  token = None
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
  spreadsheet_key = os.environ.get("SPREADSHEET_KEY")
  gc = None

  def __init__(self):
    json_file_name = os.environ.get("JSON_FILE_NAME")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, self.scope)
    self.gc = gspread.authorize(credentials)

  def test(self):
    worksheet = self.gc.open_by_key(self.spreadsheet_key).sheet1
    import_value = int(worksheet.acell('A1').value)

    export_value = import_value+1000
    worksheet.update_cell(1,2, export_value)

