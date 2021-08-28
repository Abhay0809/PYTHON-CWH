import qrcode

print("CONVERT YOUR LINK TO QR CODE instantly!")
link = input("Enter your link here: ")
name = input("Enter name of saved image: ")

img = qrcode.make(link)
type(img)

img.save(f"./QRCodes_img/{name}.png")
img.show()

print("Thanks for using the program!")
