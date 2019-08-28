"""Test for GIF MAKER."""

import os
from gif_maker import gif_maker


def test_making_a_gif_out_of_png():
    """Just reads in PNGs and makes a GIF out of it."""
    FILEPATH = 'pics/'
    gif_maker(FILEPATH, gif_name='test')
    # created?
    assert os.path.isfile(FILEPATH + 'test.gif')
    os.remove(FILEPATH + 'test.gif')
    # deleted?
    assert not os.path.isfile(FILEPATH + 'test.gif')
