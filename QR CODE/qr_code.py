import qrcode
# from PIL import Image


data = 'https://netflix-clone-react-shabab.netlify.app/'
img = qrcode.make(data)
img.save('qr.jpeg')


data = 'https://netflix-clone-react-shabab.netlify.app/'
img = qrcode.make(data)
img.save('olx-clone.jpeg')


# img.save('netflix-qr.png')


# qr = qrcode.QRCode(version=1,
#                    error_correction=qrcode.constants.ERROR_CORRECT_H,
#                    box_size=10,
#                    border=4,)
# qr.add_data('https://netflix-clone-react-shabab.netlify.app/')
# qr.make(fit=True)
# img = qr.make_image(fillcolor='red', bgcolor='blue')
# img.save('netflix-clone.png')
