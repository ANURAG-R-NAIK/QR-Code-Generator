import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border = 4,)

qr.add_data(input("Enter The Url"))
qr.make(fit=True)
img = qr.make_image(fill_color = "Red", back_color = "Blue")
img.save(input("Enter The File Name with.png"))
