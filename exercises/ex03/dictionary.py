"""Practicing with dictionary functions!"""

__author__ = "730658315"


def invert(original_dictionary: dict[str, str]) -> dict[str, str]:
    result_dictionary = {}
    for key in original_dictionary:
        value = original_dictionary[key]
        if value in result_dictionary:
            raise KeyError(f"When inverting {value}, a duplicate key was found")
        result_dictionary[value] = key
    return result_dictionary


def count(my_list: list[str]) -> dict[str, int]:
    result_dictionary = {}
    for item in my_list:
        if item in result_dictionary:
            result_dictionary[item] += 1
        else:
            result_dictionary[item] = 1
    return result_dictionary


def favorite_color(color_dictionary: dict[str, str]) -> str:
    frequent_color: str = ""
    greatest_count: int = 0
    favorites_list = []
    for name in color_dictionary:
        favorites_list.append(color_dictionary[name])
    color_counts = count(favorites_list)
    for color in color_counts:
        color_count = color_counts[color]
        if color_count > greatest_count:
            frequent_color = color
            greatest_count = color_count
    return frequent_color


def bin_len(my_list: list[str]) -> dict[int, set[str]]:
    resulting_dictionary = {}
    for strings in my_list:
        strings_length = len(strings)
        if strings_length not in resulting_dictionary:
            resulting_dictionary[strings_length] = {strings}
        else:
            resulting_dictionary[strings_length].add(strings)
    return resulting_dictionary
