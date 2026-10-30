from textovy_nastroj import najcastejsie_slovo, pocet_slov, skratit
import pytest

def test_text_viac_medzier():
    assert pocet_slov("ahoj svet ") == 2

def test_prazdny_text():
    assert pocet_slov("") == 0

def test_jedno_slovo():
    assert pocet_slov("ahoj") == 1

def test_dlhsi_text_skratit():
    assert skratit("Dobrý deň", 5) == "Dobr…"

def test_kratsi_text_ako_n():
    assert skratit("Ahoj", 10) == "Ahoj"

def test_rovnaky_text_ako_n():
    assert skratit("Ahoj", 4) == "Ahoj"

def test_najcastejsie_slovo_normalne():
    assert najcastejsie_slovo("Ahoj svet ahoj") == "ahoj"

def test_najcastejsie_slovo_remiza():
    assert najcastejsie_slovo("b a b a") == "b"

def test_najcastejsie_slovo_prazdne():
    with pytest.raises(ValueError):
        najcastejsie_slovo("")