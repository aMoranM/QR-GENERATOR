import qrcode
from PIL import Image, ImageDraw, ImageFont

def generar_qr_con_titulo(texto_qr, titulo, nombre_archivo_salida='qr_con_titulo.png'):
    # Generar el objeto QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(texto_qr)
    qr.make(fit=True)

    # Crear imagen a partir del QR y convertirla a RGB
    img_qr = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Crear imagen de fondo (RGB) con espacio adicional para el texto
    ancho_qr, alto_qr = img_qr.size
    espacio_titulo = 50
    nueva_imagen = Image.new("RGB", (ancho_qr, alto_qr + espacio_titulo), "white")
    
    # Pegar el QR en la parte superior
    nueva_imagen.paste(img_qr, (0, 0))
    
    # Dibujamos el texto
    draw = ImageDraw.Draw(nueva_imagen)
    font = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 40)

    # Medir el texto con font.getsize()
    bbox = draw.textbbox((0, 0), titulo, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calcular coordenadas para centrar el texto en el espacio inferior
    x_texto = (ancho_qr - text_width) // 2
    y_texto = alto_qr + (espacio_titulo - text_height) // 2

    # Dibujar el texto
    draw.text((x_texto, y_texto), titulo, font=font, fill="black")
    
    # Guardar
    nueva_imagen.save(nombre_archivo_salida)
    print(f"Imagen guardada: {nombre_archivo_salida}")

if __name__ == "__main__":
    # Ejemplo de uso
    generar_qr_con_titulo(
        texto_qr="https://qr.umascustom.com/IOM QTS",
        titulo="IOM QTS",
        nombre_archivo_salida="qr_IOM QTS.png"
    )
