import segno
import ezdxf

def qr_to_r12_dxf(data: str, out_dxf: str, module_size: float = 1.0, border: int = 4):
    """
    Create a true R12 (AC1009) DXF containing a QR code for `data`.

    - module_size: the side length (in drawing units) of each QR “pixel”.
    - border: number of “quiet‐zone” modules around the code (ISO minimum = 4).
    """
    # 1) Generate the Segno QR object (error level H for max redundancy)
    qr = segno.make(data, error="H")

    # 2) Extract its boolean matrix (True = dark, False = light)
    matrix = qr.matrix    # e.g. a tuple of tuples, size = N×N
    size = len(matrix)    # N modules per side

    # 3) Create a new DXF document at R12 (AC1009)
    doc = ezdxf.new(dxfversion="AC1009")
    msp = doc.modelspace()

    # 4) For each “dark” module, draw a filled SOLID (4-vertex quad)
    for row_idx, row in enumerate(matrix):
        for col_idx, bit in enumerate(row):
            if not bit:
                continue  # skip “light” modules

            # Compute lower-left corner for this module in DXF units:
            x0 = (col_idx + border) * module_size
            y0 = ((size - 1 - row_idx) + border) * module_size

            # Define the four corners of this square (clockwise or CCW):
            p0 = (x0,             y0)                          # lower-left
            p1 = (x0 + module_size, y0)                        # lower-right
            p2 = (x0 + module_size, y0 + module_size)          # upper-right
            p3 = (x0,             y0 + module_size)            # upper-left

            # Add a filled SOLID in black (color=0) 
            msp.add_solid([p0, p1, p2, p3], dxfattribs={"color": 0})

    # 5) Save out as an R12 DXF
    doc.saveas(out_dxf)
    print(f"R12 DXF saved as: {out_dxf}")

if __name__ == "__main__":
    # Example: generate “qr_CRAH-151-BOTTOM.dxf” at 2 units/module + 4-module border
    for i in range(222, 262):
        for position in ["BOTTOM", "TOP"]:
            titulo = f"CRAH-{i}-{position}"
            qr_to_r12_dxf(
                data=f"https://qr.umascustom.com/{titulo}",
                out_dxf=f"imagenes\DXF\qr_{titulo}.dxf",
                module_size=1.0,
                border=4
            )
