#!/usr/bin/env python3
import random 
import string
import dropbox





def main():
    input_password =  input("inputyournamepassword:   " )
    

    password_first  = ['XyQVBy?2i','+sUD2fdF','6UX?Dd38','D+H?fd7w','Tq+6ky&K','6Vfs#y!&']
    password_sec    = ['jH4a$hfZz7LB','B^gZ%t~+d45J','?^AMymb3z2HB','8!D^nAmHwWsp','3zxWu9e@sj6W','3zxWu9e@sj6Wi']
    password_first = random.choice(password_first)
    password_sec   = random.choice(password_sec)
    number = random.randrange(0,100)
    sp     = random.choice(string.punctuation)
    password = password_first + password_sec + str(number) + sp
    #print(password,input_password)

    

        
    
    
    f = open("safepassword.txt","a+")
    f.write("yourpassword: %s : %s\n"%(password,input_password))



dbx = dropbox.Dropbox('51G33pH_seAAAAAAAAAAEGKbvgte5WcJlV51MeqmJfme7j8XjmOXn6TYCL0p5jp1')
localfile = 'safepassword.txt'
backuppath  = '/safepassword-backup.txt'

def backup():

    with open(localfile,'rb') as f:
        dbx.files_upload(f.read(),backuppath + localfile,mute = True )
        print(" uploading" + localfile + " to dropbox as " + backuppath + "...")


    #dbx.files_download_to_file('coppy' + localfile,backuppath+localfile)

   
    

main()    
backup()



        
