import qrcode
from PIL import ImageDraw, ImageFont

if __name__ == '__main__':
    FONT_SIZE = 100
    FILL_COLOR='black'
    BACK_COLOR='#ffffff'

    target_url = input('What is the URL?: ')
    output_file_name = input('What is the output file name?: ')

    qr = qrcode.QRCode(
        version=1,
        box_size=100,
        border=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    qr.add_data(target_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Avenir.ttc", FONT_SIZE)
    draw.text((530, 160), target_url, fill='rgb(0, 0, 0)', font=font)
    img.save(output_file_name)