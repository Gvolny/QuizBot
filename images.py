from PIL import Image, ImageDraw, ImageFont, ImageSequence


def get_image(text):
    back = Image.open("back1.jpg")
    width, height = back.size

    idraw = ImageDraw.Draw(back)

    fontsize = 144
    font = ImageFont.truetype("NimbusSanL-Regu.ttf", size=fontsize)

    while font.getbbox(text)[-2] > 800:
        font = ImageFont.truetype("NimbusSanL-Regu.ttf", size=font.size - 2)

    font_width, font_height = font.getbbox(text)[-2:]

    n_width = (width - font_width) / 2
    n_height = (height - font_height) / 2

    idraw.text((n_width, n_height), text, font=font, fill='black')

    back.save('texted_back.png')

    get_gif()


def get_gif():
    background = Image.open('texted_back.png')  # .convert('RGBA')
    animated_gif = Image.open("snowfalling.gif")

    all_frames = []

    for gif_frame in ImageSequence.Iterator(animated_gif):
        # duplicate background image because we will change it (we will paste
        new_frame = background.copy()

        # convert to `RGBA` to use `Alpha` in `paste` as transparency mask
        gif_frame = gif_frame.convert('RGBA')

        # paste on background with transparency mask (channel ALPHA in gif_frame)
        new_frame.paste(gif_frame, mask=gif_frame)

        all_frames.append(new_frame)

    # save first frame and append other frames with duration 100ms
    all_frames[0].save("image2.gif", save_all=True, append_images=all_frames[1:], duration=100, loop=0)