import re

# def normalize_phone(phone_number):
#     normal_chars = ['+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#     new_number = []

#     for char in phone_number:
#         if char in normal_chars:
#             new_number.append(char)

#     new_number = "".join(new_number)

#     if new_number.startswith("+38"):
#         return new_number
#     else:
#         return "+38" + new_number

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)

    if not cleaned_number.startswith("38"):
        cleaned_number = "38" + cleaned_number

    return "+" + cleaned_number


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)



