import qrcode

# Paste Hpyerlink Here
hyperlink = " "
# File Name
fName = "test"+".jpeg"
def generateQR(loc,fName):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(loc)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(fName)

    print("QR Code has been generated and Saved as:", fName)

generateQR(hyperlink, fName)