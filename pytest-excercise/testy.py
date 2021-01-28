import pytest
import homework
import json

@pytest.mark.parametrize("list, indices, expected_result", [([], [], []),
                                                            (['test'], [2], ['s']),
                                                            ([1, 2, 3], [0, 2], [1, 3])])
def test_take_from_list(list, indices, expected_result):
    assert homework.take_from_list(list, indices) == expected_result


@pytest.mark.xfail(reason="Index Error")
def test_index_error_take_from_list():
    assert homework.take_from_list([], [1])
    assert homework.take_from_list([1, 2, 3], [3])

@pytest.mark.xfail(reason="Value Error")
def test_value_error_take_from_list():
    assert homework.take_from_list([1, 2, 3], [1.01])
    assert homework.take_from_list([1, 2, 3], ['a'])
    assert homework.take_from_list([1, 2, 3], [None])


def test_calculate(tmpdir):
    input_file = tmpdir.join('input.json')
    data = {"list": [13, 21, 96], "indices": [1, 2, 5]}
    output_file = tmpdir.join('output.json')

    with open(input_file, 'w') as file:
        json.dump(data, file)

    with pytest.raises(IndexError):
        homework.calculate(input_file, output_file)
