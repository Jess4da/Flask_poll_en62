import gspread
from datetime import date, datetime
from oauth2client.service_account import ServiceAccountCredentials
from os import path

ROOT = path.dirname(path.realpath(__file__))


today = datetime.now()
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(path.join(ROOT, 'secret_key.json'), scope)
client = gspread.authorize(creds)

def getData():
    global today, scope, creds, client, sheet, sn
    today = datetime.now()
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(path.join(ROOT, 'secret_key.json'), scope)
    client = gspread.authorize(creds)

    sheet = client.open('เช็คชื่อ 62').worksheet('เช็คชื่อ')
    sn = sheet.col_count

def getData_illigal():
    global today, scope, creds, client, sheet, sn
    today = datetime.now()
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(path.join(ROOT, 'secret_key.json'), scope)
    client = gspread.authorize(creds)

    sheet = client.open('เช็คชื่อ 62').worksheet('แต่งกายผิดระเบียบ')
    sn = sheet.col_count

def colnum(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def checkDate():
    return sheet.cell(1,sn).value == today.strftime("%d/%m/%Y")

def oldcheck(id):
    cell = sheet.find(str(id))
    sheet.update_cell(cell.row, sn, 1)
    return sheet.cell(cell.row, 2).value + " " + sheet.cell(cell.row, 3).value + " " + sheet.cell(cell.row, 4).value

def newCheck(id):
    sheet.add_cols(1)
    sheet.update_cell(1, sn + 1, today.strftime("%d/%m/%Y"))
    cell = sheet.find(str(id))
    sheet.update_cell(cell.row, sn + 1, 1)
    sheet.update_cell(710, sn + 1, "=SUM("+colnum(sn+1)+"2:"+colnum(sn+1)+"707)")
    return sheet.cell(cell.row, 2).value + " " + sheet.cell(cell.row, 3).value + " " + sheet.cell(cell.row, 4).value

def checkDT(id):
    if checkDate():
        return oldcheck(id)
    else:
        return newCheck(id)

def sumtoday():
    try:
        cell = sheet.find(today.strftime("%d/%m/%Y"))
        return sheet.cell(710, cell.col).value
    except:
        return 0

def oldcheckil(id, comment):
    cell = sheet.find(str(id))
    sheet.update_cell(cell.row, sn, comment)
    return sheet.cell(cell.row, 2).value + " " + sheet.cell(cell.row, 3).value + " " + sheet.cell(cell.row, 4).value

def newCheckil(id, comment):
    sheet.add_cols(1)
    sheet.update_cell(1, sn + 1, today.strftime("%d/%m/%Y"))
    cell = sheet.find(str(id))
    sheet.update_cell(cell.row, sn + 1, comment)
    return sheet.cell(cell.row, 2).value + " " + sheet.cell(cell.row, 3).value + " " + sheet.cell(cell.row, 4).value


def checkDTil(id, comment):
    if checkDate():
        return oldcheckil(id, comment)
    else:
        return newCheckil(id, comment)