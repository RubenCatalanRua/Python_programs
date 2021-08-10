import os, shutil, time

dir_folder = r"C:\Users\catalan\Desktop\PythonDestFolder/"

def moving_files():
    
    src_folder = r"C:\Users\catalan\Desktop\PythonOriginFolder/"
    for file in os.listdir(src_folder):
       if file == "desktop.ini":
           continue
       ext = os.path.splitext(file)[1]
       extPath = ext[1:]
       dir_folder_1 = dir_folder + extPath.upper()
       src_doc = src_folder + file
       
       if not os.path.exists(dir_folder_1):
           os.makedirs(dir_folder_1)

       if os.path.exists(dir_folder_1):
           try:
               shutil.copy(src_doc, dir_folder_1)
           except Exception:
               continue
               
               
while True:
  
    moving_files()
    time.sleep(10)
           
           





