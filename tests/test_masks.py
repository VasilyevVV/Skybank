import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [(2200792289607341, "2200 79** **** 7341"),
                                                   ("2200792289607341", "2200 79** **** 7341"),
                                                   ("2200 7922 8960 7341", "2200 79** **** 7341"),
                                                   ("0054752989607340", "0054 75** **** 7340"),
                                                   ("0054 752989607341", "0054 75** **** 7341"),
                                                   ("105 47 5 2989 6 07 342", "1054 75** **** 7342")])
def test_correct_card_mask(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_empty_card_mask():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
        assert str(exc_info.value) == "Пустой номер карты"