import qrcode
import image

qr = input("ENTER HERE: ")
img=qrcode.make(qr)
print()
fn = input("ENTER FILE NAME HERE: ")
fnfl = fn+".png"
img.save(fnfl)
print()
print("QR CODE SAVED AS: "+fnfl)
