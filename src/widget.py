from .masks import get_mask_card_number, get_mask_account


def mask_account_card(account_info: str) -> str:
    """Функция обрабатки информацию о картах и счетах. Возвращает строку с с замаскированным номером"""
    account_list = account_info.split(" ")
    masked_info = ""
    account_info_mask = ""
    if len(account_list[-1]) == 16:
        masked_info = get_mask_card_number(int(account_list[-1]))
    elif len(account_list[-1]) == 20:
        masked_info = get_mask_account(int(account_list[-1]))
    account_info_mask = f"{" ".join(account_list[:-1])} {masked_info}"
    return account_info_mask


info = "Maestro 1596837868705199"
print(mask_account_card(info))
