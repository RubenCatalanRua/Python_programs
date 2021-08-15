import os, shutil

def storing_files(save_folder):


    for file in os.listdir(save_folder):
        if file == "desktop.ini":
            continue
            
        ext = os.path.splitext(file)[1]
        extPath = ext[1:]
        end_folder = save_folder + extPath.upper()
        src_doc = save_folder + file
           
        if not os.path.exists(end_folder):
            os.makedirs(end_folder)

        if os.path.exists(end_folder):
            try:
                shutil.move(src_doc, end_folder)
            except Exception:
                continue
               
           

# Usar como ejemplo C:\Users\catalan\Desktop\PythonOriginFolder\





