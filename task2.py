import random

admn_min = 1
admn_max = 1000

def get_numbers_ticket(min, max, quantity):
    selected_nums = []
    if min >= admn_min and max <= admn_max and 0 < quantity <= max:
        while len(selected_nums) <= quantity:
            r_num = random.randrange(min,max)
            if r_num not in selected_nums:
                selected_nums.append(r_num)
            else:
                continue
        return sorted(selected_nums)
    else:
        print(f"Args must be within min {admn_min} and max {admn_max}")        



lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)