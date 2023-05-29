from moviepy.editor import VideoFileClip, concatenate_videoclips
import os


# TODO: Cambiar las rutas de los videos
intro_path = "intro/lectura rfid.mp4" 
videos_path = "input/"
output_path = "output/"


"""
unir_videos: Función que permite unir dos videos en uno solo.
Parámetros:
    intro_path: Ruta del primer video.
    video2_path: Ruta del segundo video.
    output_path: Ruta donde se guardarán los videos unidos.
"""

def unir_videos(intro_path:str, video2_path:str, output_path:str):
    # Cargar los videos
    video1 = VideoFileClip(intro_path)
    video2 = VideoFileClip(video2_path)

    # Concatenar los videos
    videos_concatenados = concatenate_videoclips([video1, video2])

    # Guardar el video resultante
    videos_concatenados.write_videofile(output_path)




def main():
    #listar los videos que hay dentro de la carpeta de videos_path
    videos = os.listdir(videos_path)
    for video, index in zip(videos, range(len(videos))):
        
        print(f"Uniendo video {index+1} de {len(videos)}")
        # Unir los videos
        unir_videos(intro_path, videos_path+video, output_path+video)

if __name__ == "__main__":
    main()