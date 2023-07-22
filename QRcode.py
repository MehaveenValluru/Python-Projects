
import qrcode
company=input("Enter Company Name : ")
projname=input("Enter the Name of Project : ")
data={"company":company,"projname":projname,}
qr=qrcode.QRCode(version=1,box_size=12,border=5)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color='purple',back_color="white")
img.save("text.png")








