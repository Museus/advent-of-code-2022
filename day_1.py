import pathlib

CALORIES_FILE = "input.txt"

def load_calories_file(calories_file_path: pathlib.Path):
    with open(calories_file_path, "r") as input_file:
        return input_file.readlines()

def split_food_by_elf(food_items):
    results = {}
    current_elf = 1

    results[current_elf] = 0
    for food in food_items:
        calories = food.strip()
        if calories:
            results[current_elf] += int(calories)

        if not calories:
            current_elf += 1
            results[current_elf] = 0

    return results

def get_elf_with_most_calories(calories_file_path: pathlib.Path):
    food_items = load_calories_file(calories_file_path)
    elf_calories = split_food_by_elf(food_items)

    return sorted(elf_calories.items(), key=lambda x: x[1], reverse=True)[0]

calories_file_path = pathlib.Path(CALORIES_FILE)
result = get_elf_with_most_calories(calories_file_path)

print(f"Elf {result[0]} with {result[1]} calories.")
