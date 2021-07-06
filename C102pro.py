import dropbox
import time
import random
start_time = time.time()


    

def upload_file():
    access_token ='sl.A0FrGk65-h0AELd93uQUg1mT5k4m70eptLUi5U5o7ZfEJ5tHnbsotJzs_gfPw7uRh7GZ9lIOj0wpR5-LJCPqD4ib3rJ_7tSnQlpJtguwt4QpzRAgA4tK9xqOl9l3muLxoJ67Uywo'
    #file = task_name
    file_from = 'tasks.txt'
    file_to = '/test/tasks.txt' 
    dbx = dropbox.Dropbox(access_token)
    with open (file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

     

def main():
    
    while(True):
        if((time.time()-start_time)>=5):
          
            upload_file()
            #upload_file.release()

    
main()




