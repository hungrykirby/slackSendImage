
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

  def __init__(self, dev):
    json_file_name = os.environ.get("JSON_FILE_NAME")
    if dev == False:
      self.spreadsheet_key = os.environ.get("SPREADSHEET_KEY_DEV")
    credentials = ServiceAccountCredentials.from_json_keyfile_name(join(os.getcwd(), json_file_name), self.scope)
    self.gc = gspread.authorize(credentials)

  def test(self):
    worksheet = self.gc.open_by_key(self.spreadsheet_key).sheet1
    import_value = int(worksheet.acell('A1').value)

    # export_value = import_value+1000
    # worksheet.update_cell(1,2, export_value)
    print(len(worksheet.get_all_values()[0]))
    last_line = len(worksheet.get_all_values()) + 1
    worksheet.update_cell(last_line, 2, 3)
  
  def write_pressure_spreadsheet(self, place, year, month, date, time, pressure):
    worksheet = self.gc.open_by_key(self.spreadsheet_key).sheet1
    last_line = len(worksheet.get_all_values()) + 1
    worksheet.update_cell(last_line, 1, place)
    worksheet.update_cell(last_line, 2, year)
    worksheet.update_cell(last_line, 3, month)
    worksheet.update_cell(last_line, 4, date)
    worksheet.update_cell(last_line, 5, time)
    worksheet.update_cell(last_line, 6, pressure)
    

