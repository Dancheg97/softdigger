"""file to test dangerous funciton"""
from func import double_capitalize


def test_double_capitalize():
    assert double_capitalize("avatar") == "AVATARAVATAR"
    assert double_capitalize("cocaCola") == "COCACOLACOCACOLA"
