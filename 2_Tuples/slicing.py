prime_numbers = (1, 2, 3, 5, 7, 11, 13, 17, 19)

# from idx 2 to 7 but 7 is not included
num = prime_numbers[2:7]
print(f"idx 2 to 7: {num}")

first_4num = prime_numbers[:4]
print(f"first 4 num: {first_4num}")

last_5num = prime_numbers[-5:]
print(f"last 5 num: {last_5num}")

#with step => optional, step=1
odd_idx = prime_numbers[::2]
print(f"items of odd idx: {odd_idx}")