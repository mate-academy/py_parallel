import parallel


def test_sides():
    b = parallel.Box(5, 4, 3)
    assert b.get_length() == 5
    assert b.get_width() == 4
    assert b.get_height() == 3


def test_volume():
    b = parallel.Box(5, 4, 3)
    assert b.get_volume() == 60