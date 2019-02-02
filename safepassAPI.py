#!/usr/bin/env python3
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import string




def main():
    input_password =  input("inputyournamepassword:   " )


    password_first  = ['XyQVBy?2i','+sUD2fdF','6UX?Dd38','D+H?fd7w','Tq+6ky&K','6Vfs#y!&']
    password_sec    = ['jH4a$hfZz7LB','B^gZ%t~+d45J','?^AMymb3z2HB','8!D^nAmHwWsp','3zxWu9e@sj6W','3zxWu9e@sj6Wi']
    password_first = random.choice(password_first)
    password_sec   = random.choice(password_sec)
    number = random.randrange(0,100)
    sp     = random.choice(string.punctuation)
    password = password_first + password_sec + str(number) + sp
    name_password = password,input_password
    
























    SCOPE = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


    creadentials = ServiceAccountCredentials.from_json_keyfile_name('safePasswordV1-eb6d43424c74.json',SCOPE)

    gc = gspread.authorize(creadentials)

    wks = gc.open('safepassword').sheet1

    #print(wks.get_all_records())

    wks.append_row(name_password)








main()
