"""Practicing with unit tests!"""

__author__ = "730658315"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len


def test_invert_edge1() -> None:
    """Test edge case for invert with no input"""
    original_dictionary = {}
    assert invert(original_dictionary) == {}


def test_invert_use1() -> None:
    """Test use case for invert with dictionary of letter pairs"""
    original_dictionary = {"a": "z", "b": "y", "c": "x"}
    result_dictionary = {"z": "a", "y": "b", "x": "c"}
    assert invert(original_dictionary) == result_dictionary


def test_invert_use2() -> None:
    """Test second use case for invert with dictionary of subjects and colors"""
    original_dictionary = {"math": "blue", "science": "green", "english": "red"}
    result_dictionary = {"blue": "math", "green": "science", "red": "english"}
    assert invert(original_dictionary) == result_dictionary


def test_count_edge1() -> None:
    """Test edge case for count with an Empty list"""
    my_list = []
    result_dictionary = {}
    assert count(my_list) == result_dictionary


def test_count_use1() -> None:
    """Test use case for count with list of pets"""
    my_list = ["dog", "cat", "bird", "cat", "snake"]
    result_dictionary = {"dog": 1, "cat": 2, "bird": 1, "snake": 1}
    assert count(my_list) == result_dictionary


def test_count_use2() -> None:
    """Test second use case for count with lists of letters"""
    my_list = ["a", "b", "c", "c", "b", "a"]
    result_dictionary = {"a": 2, "b": 2, "c": 2}
    assert count(my_list) == result_dictionary


def test_favorite_color_edge1() -> None:
    """Test edge case for favorite color"""
    color_dictionary = {}
    assert favorite_color(color_dictionary)


def test_favorite_color_use1() -> None:
    """Test use case for favorite color using fewer colors"""
    color_dictionary = {"student1": "green", "student2": "blue", "student3": "green"}
    assert favorite_color(color_dictionary) == "green"


def test_favorite_color_use2() -> None:
    """Test second use case for favorite color using many colors"""
    color_dictionary = {
        "student1": "purple",
        "student2": "orange",
        "student3": "white",
        "student4": "pink",
    }
    assert favorite_color(color_dictionary) == "purple"


def test_bin_len_edge1() -> None:
    """Test edge case for bin len with an empty list"""
    my_list = [""]
    assert bin_len(my_list) == {0: {""}}


def test_bin_len_use1() -> None:
    """Test use case for bin len with different words"""
    my_list = ["the", "brown", "egg"]
    assert bin_len(my_list) == {3: {"the", "egg"}, 5: {"brown"}}


def test_bin_len_use2() -> None:
    """Test second use case for bin len with words of same length"""
    my_list = ["the", "big", "egg"]
    assert bin_len(my_list) == {3: {"the", "big", "egg"}}
