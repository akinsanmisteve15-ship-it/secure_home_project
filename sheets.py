import gspread
from datetime import datetime

class SheetsService:
    def __init__(self):
        try:
            self.gc = gspread.service_account(filename="creds.json")
            self.sh = self.gc.open("SHV_User_Data")
            self.wks = self.sh.sheet1
        except Exception as e:
            print(f"⚠️ Google Service Unavailable: {e}")
            self.wks = None

    def sync(self, data_list):
        if not self.wks:
            return False
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.wks.append_row([timestamp] + data_list)
            return True
        except Exception as e:
            print(f"⚠️ Sheets Sync Failed: {e}")
            return False

google_cloud = SheetsService()