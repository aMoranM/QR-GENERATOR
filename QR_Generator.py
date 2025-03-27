import qrcode
import textwrap
from PIL import Image, ImageDraw, ImageFont

def generar_qr_con_logo_y_titulo_multilinea(
    texto_qr,
    titulo,
    logo_path=None,
    nombre_archivo_salida="qr_con_logo_y_multilinea.png",
    line_width=20,                # Ancho máximo en caracteres por línea
    fuente="C:/Windows/Fonts/arial.ttf",  # Ruta a la fuente TrueType
    font_size=30                  # Tamaño de la fuente
):
    """
    Genera un QR con el contenido de 'texto_qr', inserta un logo opcional en el centro,
    y dibuja el 'titulo' en múltiples líneas debajo del QR.
    
    :param texto_qr:       Texto o URL para codificar en el QR
    :param titulo:         Texto a dibujar debajo del QR (se hará multilinea si es largo)
    :param logo_path:      Ruta opcional a una imagen para insertar en el centro del QR
    :param nombre_archivo_salida: Nombre del archivo PNG que se generará
    :param line_width:     Número máximo de caracteres antes de partir la línea
    :param fuente:         Ruta a la fuente TrueType para dibujar el texto
    :param font_size:      Tamaño de la fuente en puntos
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
        # Ajusta la proporción del logo para que no sea muy grande
        factor_porcentaje = 0.2  # 20% del ancho del QR
        nuevo_ancho = int(ancho_qr * factor_porcentaje)
        # Redimensionar manteniendo relación de aspecto
        logo.thumbnail((nuevo_ancho, nuevo_ancho), Image.Resampling.LANCZOS)

        # Calcular posición para centrar el logo en el QR
        logo_ancho, logo_alto = logo.size
        pos_x = (ancho_qr - logo_ancho) // 2
        pos_y = (alto_qr - logo_alto) // 2

        # Pegar el logo usando su propio canal alpha como máscara
        img_qr.paste(logo, (pos_x, pos_y), logo)

    # 3) Preparar la fuente y el "wrapped text" (texto con saltos de línea)
    font = ImageFont.truetype(fuente, font_size)
    # Usa 'textwrap.fill' para partir el texto en líneas con un ancho máximo
    titulo_multilinea = textwrap.fill(titulo, width=line_width)

    # 4) Medir el texto en multilinea
    temp_img = Image.new("RGB", (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    bbox = temp_draw.multiline_textbbox((0, 0), titulo_multilinea, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 5) Crear imagen final (QR + el texto debajo)
    espacio_titulo = text_height + 20  # Deja un margen extra
    nueva_imagen = Image.new("RGB", (ancho_qr, alto_qr + espacio_titulo), "white")

    # Pegar el QR en la parte superior
    nueva_imagen.paste(img_qr, (0, 0))

    # 6) Dibujar el texto multilinea
    draw = ImageDraw.Draw(nueva_imagen)
    # Centrarlo horizontalmente
    x_texto = (ancho_qr - text_width) // 2
    # Ponerlo debajo del QR
    y_texto = alto_qr + (espacio_titulo - text_height) // 2

    draw.multiline_text((x_texto, y_texto), titulo_multilinea, font=font, fill="black", align="center")

    # 7) Guardar la imagen
    nueva_imagen.save(nombre_archivo_salida)
    print(f"Imagen guardada: {nombre_archivo_salida}")


if __name__ == "__main__":
    # Bucle para generar el QR de 1 a 20, en versiones BOTTOM y TOP
    for i in range(20, 21):
        for position in ["BOTTOM", "TOP"]:
            titulo = f"WIRING_DIAGRAM"
            
            # Versión SIN logo
            generar_qr_con_logo_y_titulo_multilinea(
                texto_qr=f"https://qr.umascustom.com/{titulo}",
                titulo = titulo.replace("_", " "),
                logo_path=None,
                nombre_archivo_salida=f"qr_{titulo}.png",
                line_width=15,
                fuente="C:/Windows/Fonts/arial.ttf",  # Ajusta la ruta de la fuente según tu sistema
                font_size=48
            )