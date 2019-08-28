"""Test for GIF MAKER."""

import os
from gif_maker import gif_maker


def test_making_a_gif_out_of_png():
    """Just reads in PNGs and makes a GIF out of it."""
    file_path = 'pics/'
    gif_maker(file_path, gif_name='test')
    # created?
    assert os.path.isfile(file_path + 'test.gif')
    os.remove(file_path + 'test.gif')
    # deleted?
    assert not os.path.isfile(file_path + 'test.gif')
