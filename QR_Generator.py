import qrcode
from PIL import Image

def generar_qr_con_logo(
    texto_qr,
    logo_path=None,
    nombre_archivo_salida="qr_con_logo.png"
):
    """
    Genera un código QR con el contenido de 'texto_qr' e inserta un logo opcional en el centro.
    Se utiliza todo el espacio para el QR, sin añadir títulos ni margenes extra.

    :param texto_qr:       Texto o URL para codificar en el QR
    :param logo_path:      Ruta opcional a una imagen para insertar en el centro del QR
    :param nombre_archivo_salida: Nombre del archivo PNG que se generará
    """

    # 1) Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección
        box_size=10,
        border=4
    )
    qr.add_data(texto_qr)
    qr.make(fit=True)
    
    # Crear la imagen QR (convertir a RGB)
    img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    ancho_qr, alto_qr = img_qr.size

    # 2) Insertar un logo en el centro (opcional)
    if logo_path is not None:
        logo = Image.open(logo_path).convert("RGBA")
        # Ajusta la proporción del logo para que no ocupe demasiado espacio
        factor_porcentaje = 0.2  # 20% del ancho del QR
        nuevo_ancho = int(ancho_qr * factor_porcentaje)
        # Redimensionar manteniendo la relación de aspecto
        logo.thumbnail((nuevo_ancho, nuevo_ancho), Image.Resampling.LANCZOS)

        # Calcular posición para centrar el logo en el QR
        logo_ancho, logo_alto = logo.size
        pos_x = (ancho_qr - logo_ancho) // 2
        pos_y = (alto_qr - logo_alto) // 2

        # Pegar el logo usando su canal alpha como máscara
        img_qr.paste(logo, (pos_x, pos_y), logo)

    # 3) Guardar la imagen sin margen extra, usando todo el espacio del QR
    img_qr.save(nombre_archivo_salida)
    print(f"Imagen guardada: {nombre_archivo_salida}")

if __name__ == "__main__":
    # Bucle para generar códigos QR de acuerdo a un patrón
    # for i in range(151, 300):
        # for position in ["BOTTOM", "TOP"]:
            titulo = f"IOM_FCW"
            generar_qr_con_logo(
                texto_qr=f"https://qr.umascustom.com/VANTAGE/{titulo}",
                logo_path=None,
                nombre_archivo_salida=f"imagenes\VANTAGE\qr_{titulo}.PNG"
            )
