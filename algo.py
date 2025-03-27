import os

def crear_carpetas_y_archivos(base_path):
    # Asegúrate de que base_path existe o créalo si no existe
    os.makedirs(base_path, exist_ok=True)
    
    for i in range(2, 21):
        for posicion in ["BOTTOM", "TOP"]:
            # Arma el nombre de la carpeta
            nombre_carpeta = f"CRAH-{i}-{posicion}"
            ruta_carpeta = os.path.join(base_path, nombre_carpeta)
            
            # Crea la carpeta (si no existe)
            os.makedirs(ruta_carpeta, exist_ok=True)
            
            # Contenido del index.html con la redirección
            html_content = f"""<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url=https://qr.umascustom.com/CRAH-{i}-{posicion}">
  </head>
  <body>
    Redirecting to PDF...
  </body>
</html>"""
            
            # Crea (o sobreescribe) el archivo index.html
            with open(os.path.join(ruta_carpeta, "index.html"), "w", encoding="utf-8") as archivo:
                archivo.write(html_content)


if __name__ == "__main__":
    # Reemplaza esta ruta con la ruta que desees en tu sistema Windows
    ruta_base = r"C:\Users\DeepCool\Developments\QR REDIRECTION HTML\qr-redirects"
    crear_carpetas_y_archivos(ruta_base)
    print("¡Carpetas e index.html creados exitosamente!")
