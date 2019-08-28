"""
Make a GIF.

GIF MAKER takes all the .PNG files out of a path,
sorts them by name to make a gif.
There is an option to delete the used PNGs.
"""

import os
import imageio


def gif_maker(f_path: str, gif_name: str = 'result007',
              fps: float = 3.0, kill: bool = False) -> None:
    """
    Use the GIF MAKER.

    It needs the PATH of the PNGs and will save a the GIF in that Directory.
    """
    # List of images for imageio
    images = []
    # List of files with an PNG-ending
    file_names = []
    # Getting the PNG-filenames
    for f_name in os.listdir(f_path):
        if f_name.endswith(".png"):
            file_names.append(f_name)
    # Sort the filenames to get the right GIF
    file_names.sort()

    # Check if there are files
    if len(file_names) <= 1:
        print(f'Not enough PNG-FILES in {f_path}')
        return

    for name in file_names:
        image = imageio.imread(f_path+name)
        images.append(image)

    imageio.mimsave(f'{f_path}{gif_name}.gif', images, fps=fps)
    if kill:
        os.system('rm *.png')


if __name__ == "__main__":

    FILEPATH = 'pics/'
    gif_maker(FILEPATH)
