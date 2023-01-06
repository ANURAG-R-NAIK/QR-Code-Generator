import qrcode as qr
img = qr.make(input('Enter The Url Here'))
img.save(input("Enter The File Name"))