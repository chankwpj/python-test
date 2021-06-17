def test_list_length():
    int_set = {1, 2, 3, 4}
    assert len(int_set) == 4


def test_set_contains():
    int_set = {1, 2, 3, 4}
    assert 4 in int_set


def test_set_contains_multiple():
    int_set = {1, 2, 3}
    assert {1, 3} in int_set


def test_list_order():
    int_list = [5, 4, 3]
    assert [3, 4, 5] == int_list

