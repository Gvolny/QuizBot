from PIL import Image, ImageSequence

background = Image.open('back2.jpg')#.convert('RGBA')
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


