import os
import sys

def crear_carpetas_y_archivos(base_path):
    # Asegurarse de que la ruta base exista o crearla
    os.makedirs(base_path, exist_ok=True)
    
    # Recorrer el rango y los distintos valores de "posicion"
    # for i in range(1, 25):
    # Armar el nombre y ruta de la carpeta
    nombre_carpeta = f"ASSEMBLY_HANDLING_AND_POSITIONING_OF_THE_UNIT"
    ruta_carpeta = os.path.join(base_path, nombre_carpeta)
    
    # Si la carpeta ya existe, se detiene el proceso
    if os.path.exists(ruta_carpeta):
        print(f"La carpeta '{ruta_carpeta}' ya existe. Deteniendo el proceso.")
        sys.exit(1)
    
    # Crear la carpeta (sin usar exist_ok=True)
    os.makedirs(ruta_carpeta)
    
    # Contenido del index.html con la redirección
    html_content = f"""<!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="refresh" content="0; url=https://qr.umascustom.com/VANTAGE/{nombre_carpeta}">
      </head>
      <body>
        Redirecting to PDF...
      </body>
    </html>"""
    
    # Crear el archivo index.html en la carpeta recién creada
    index_path = os.path.join(ruta_carpeta, "index.html")
    with open(index_path, "w", encoding="utf-8") as archivo:
        archivo.write(html_content)
    print(f"Carpeta creada: '{ruta_carpeta}' y se generó '{index_path}'.")

if __name__ == "__main__":
    # Reemplaza esta ruta con la que desees en tu sistema Windows
    ruta_base = r"C:\Users\DeepCool\Developments\QR REDIRECTION HTML\qr-redirects\VANTAGE"
    crear_carpetas_y_archivos(ruta_base)
    print("¡Carpetas e index.html creados exitosamente!")
