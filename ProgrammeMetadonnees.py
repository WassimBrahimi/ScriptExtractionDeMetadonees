from pathlib import Path
import os.path, time
import csv
from PIL import Image
from PIL.ExifTags import TAGS
import sys
from tinytag import TinyTag
from PyPDF2 import PdfFileReader



path_of_the_directory = '*CHEMIN DU FICHER*'


#Fichier XLSX

paths = Path(path_of_the_directory).glob('**/*.xlsx')
for path in paths:
   print("\n")
   #afficher le path
   print("Path : ",path)
   # Date de creation et date de modification
   creation = time.ctime(os.path.getmtime(path))
   modif = time.ctime(os.path.getctime(path))
   print("Derniere modification: ", modif)
   print("Creation : ", creation)

   # Nom et extention du document
   split_tup = os.path.splitext(path)

   file_name = split_tup[0]
   file_extension = split_tup[1]
   nomfichier=os.path.basename(file_name)
   print("Nom du fichier: ", nomfichier)
   print("Extention du fichier: ", file_extension)
   
   # taille du document
   file_size = os.path.getsize(path)
   print("taille du fichier :", file_size, "octets")
   print("\n")

#Fichier XML

paths = Path(path_of_the_directory).glob('**/*.xml')
for path in paths:
   print("\n")
   #afficher le path
   print("Path : ",path)
   # Date de creation et date de modification
   creation = time.ctime(os.path.getmtime(path))
   modif = time.ctime(os.path.getctime(path))
   print("Derniere modification: ", modif)
   print("Creation : ", creation)

   # Nom et extention du document
   split_tup = os.path.splitext(path)

   file_name = split_tup[0]
   file_extension = split_tup[1]
   nomfichier=os.path.basename(file_name)
   print("Nom du fichier: ", nomfichier)
   print("Extention du fichier: ", file_extension)
   
   # taille du document
   file_size = os.path.getsize(path)
   print("taille du fichier :", file_size, "octets")
   print("\n")

#Fichier JSON

paths = Path(path_of_the_directory).glob('**/*.json')
for path in paths:
   print("\n")
   #afficher le path
   print("Path : ",path)
   # Date de creation et date de modification
   creation = time.ctime(os.path.getmtime(path))
   modif = time.ctime(os.path.getctime(path))
   print("Derniere modification: ", modif)
   print("Creation : ", creation)

   # Nom et extention du document
   split_tup = os.path.splitext(path)

   file_name = split_tup[0]
   file_extension = split_tup[1]
   nomfichier=os.path.basename(file_name)
   print("Nom du fichier: ", nomfichier)
   print("Extention du fichier: ", file_extension)
   
   # taille du document
   file_size = os.path.getsize(path)
   print("taille du fichier :", file_size, "octets")
   print("\n")



#CSV


paths = Path(path_of_the_directory).glob('**/*.csv')
for path in paths:
 #afficher le path
   print("Path : ",path)
   # Date de creation et date de modification
   creation = time.ctime(os.path.getmtime(path))
   modif = time.ctime(os.path.getctime(path))
   print("Derniere modification: ", modif)
   print("Creation : ", creation)

   # Nom et extention du document
   split_tup = os.path.splitext(path)

   file_name = split_tup[0]
   file_extension = split_tup[1]

   nomfichier=os.path.basename(file_name)
   print("Nom du fichier: ", nomfichier)
   print("Extention du fichier: ", file_extension)
   
   # taille du document
   file_size = os.path.getsize(path)
   print("taille du fichier :", file_size, "octets")

   with open(path)as fp:
     reader = csv.reader(fp)
     headers = next(reader)        
     ncol = len(headers)
     nrow = sum(1 for _ in reader) 
   print("En-têtes :",headers)
   print("Nombre de colonnes :",ncol)
   print("Nombre de lignes :",nrow)
   print("\n")


#IMAGES

paths = Path(path_of_the_directory).glob('**/*.jpeg ')
for path in paths:
   print("\n")
 #afficher le path
   imagename = path

   image = Image.open(imagename)


   info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
    }

   for label,value in info_dict.items():
     print(f"{label:25}: {value}")
    


   print("\n")
 

#Videos


paths = Path(path_of_the_directory).glob('**/*.mp4')
for path in paths:
   print("\n")
   video = TinyTag.get(path) 
   print("title: " , video.title)
   print("artist: ", video.artist)
   print("genre: " ,video.genre)
   print("year: " ,video.year)
   print( "bitrate: "+str(video.bitrate) + " kBits/s")
   print("composer: ", video.composer)
   print("Filesize: " + str(video.filesize) + " Octets")
   print("AlbumArtist: " , str(video.albumartist))
   print("Duration: " + str(video.duration) + " secondes")
   print("TrackTotal: " + str(video.track_total))
   print("\n")
  



#PDF

paths = Path(path_of_the_directory).glob('**/*.pdf')
for path in paths:
 print("\n")
 def get_info(pathpdf):
    with open(pathpdf, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
    
    print("Auteur : ",info.author)
    print("Createur : ",info.creator)
    print("Realisateur : ",info.producer)
    print("Titre : ",info.title)

 if __name__ == '__main__':
  pathpdf = path
  get_info(pathpdf)
 
  print("Path : ",path)
  # Date de creation et date de modification
  creation = time.ctime(os.path.getmtime(path))
  modif = time.ctime(os.path.getctime(path))
  print("Derniere modification: ", modif)
  print("Creation : ", creation)
   # Nom et extention du document
  split_tup = os.path.splitext(path)

  file_name = split_tup[0]
  file_extension = split_tup[1]

  nomfichier = os.path.basename(file_name)
  print("Nom du fichier: ", nomfichier)
  print("Extention du fichier: ", file_extension)
   
   # taille du document
  file_size = os.path.getsize(path)
  print("taille du fichier :", file_size, "octets")
  print("\n")
