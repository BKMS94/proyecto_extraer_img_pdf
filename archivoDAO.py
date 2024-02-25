# import module
from pdf2image import convert_from_path
import os, shutil


class ArchivoDAO:
    saving_folder = os.getcwd() + '\imgs' #donde se guarda la imagen
    saving_folder = saving_folder.replace('\\','\\\\')
    poppler_path = r'C:\Program Files\poppler-23.08.0\Library\bin' #donde se encuentra el archivo de la libreria


    
    @classmethod
    def existe_carpeta(cls):    
        if os.path.exists('imgs'):
            shutil.rmtree('imgs')

        os.mkdir('imgs')

    # recorrer y extraer imagen de la pagina completa hoja por hoja 
    @classmethod
    def extraer(cls,archivo):
        cls.pages = convert_from_path(pdf_path=archivo.pdf_path, poppler_path=ArchivoDAO.poppler_path)
        c = 1
        for page in cls.pages:
            img_name = f'img-{c}.jpeg'
            page.save(os.path.join(ArchivoDAO.saving_folder, img_name), 'JPEG')
            c += 1

# prueba
if __name__ == '__main__':
    # archivo = Archivo('C:/Users/BRAYA/Videos/catalogo gorda/catalogo.pdf')
    print(ArchivoDAO.saving_folder)