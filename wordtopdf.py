import os
from docx2pdf import convert

def convertir_docx_a_pdf(ruta_carpeta):
    # Verifica que la carpeta exista
    if not os.path.isdir(ruta_carpeta):
        print(f"La ruta '{ruta_carpeta}' no existe o no es un directorio.")
        return
    
    # Recorre todos los archivos de la carpeta
    for archivo in os.listdir(ruta_carpeta):
        # Verifica que el archivo tenga extensión .docx
        if archivo.lower().endswith(".docx"):
            ruta_docx = os.path.join(ruta_carpeta, archivo)
            
            # La salida deseada en PDF: mismo nombre, diferente extensión
            nombre_base = os.path.splitext(archivo)[0]
            ruta_pdf = os.path.join(ruta_carpeta, f"{nombre_base}.pdf")
            
            # Convierte el archivo docx a pdf
            print(f"Convirtiendo: {ruta_docx} -> {ruta_pdf}")
            convert(ruta_docx, ruta_pdf)

if __name__ == "__main__":
    # Reemplaza 'C:\\ruta\\de\\carpeta' con la ruta en tu sistema Windows
    ruta_de_ejemplo = r"C:\Users\DeepCool\OneDrive - umascustom.com\QTS PLACAS QR"
    
    convertir_docx_a_pdf(ruta_de_ejemplo)
    print("¡Conversión completada!")
