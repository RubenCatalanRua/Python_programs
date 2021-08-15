import pytube, os, shutil

from FileStoringProgram import storing_files

while True:
    save_folder = input("¿Dónde quieres guardar tus archivos? Escribe la ruta de la carpeta(utiliza un \ al final para que el programa funcione correctamente): ")

    if not os.path.exists(save_folder):
        print("Esta carpeta no existe")
    else:
        break

while True:
    
    link = input("Escribe el link del vídeo o escribe ALMACENAR para ordenar todas las descargas. ")
    if link == "ALMACENAR":

        storing_files(save_folder)
        print("Archivos almacenados")
        continue
    else:
        try:
            Vd = pytube.YouTube(link)

            print("Título:" , Vd.title)
            print("Número de visitas:" , Vd.views)

        except:
            print("No se ha encontrado el vídeo.")
            continue
    
    while True:
        Answer = input("Pulsa 1 para descargar en formato MP3 o pulsa 2 para MP4 ")

        if Answer == "1":

            try:
                video = Vd.streams.get_audio_only()
                print("Descargando...")
                
                Mp4Format = video.download(save_folder)
                Base = os.path.splitext(Mp4Format)[0]
                Mp3Format = Base + ".mp3"
                os.rename(Mp4Format, Mp3Format)
            
                print("¡Descarga completa!")
                break
            
            except Exception:
                print("Esta canción ya ha sido descargada en esta carpeta.")
                break
        elif Answer == "2":

            try:
                video = Vd.streams.get_highest_resolution()
                print("Descargando...")
                video.download(save_folder)
                print("¡Descarga completa!")
                break
            
            except Exception:
                print("Este vídeo ya ha sido descargado en esta carpeta.")
                break
        

