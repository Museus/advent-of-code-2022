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

def get_three_elves_with_most_calories(calories_file_path: pathlib.Path):
    food_items = load_calories_file(calories_file_path)
    elf_calories = split_food_by_elf(food_items)

    return sorted(elf_calories.items(), key=lambda x: x[1], reverse=True)[:3]

calories_file_path = pathlib.Path(CALORIES_FILE)

print("Top elf:")

elf_with_most_calories = get_elf_with_most_calories(calories_file_path)
print(f"  Elf {elf_with_most_calories[0]} with {elf_with_most_calories[1]} calories.")

print("\nTop three elves:")
three_elves_with_most_calories = get_three_elves_with_most_calories(CALORIES_FILE)
for elf in three_elves_with_most_calories:
    print(f"  Elf {elf[0]} with {elf[1]} calories.")

print(f"\nTotal calories in top 3: {sum(calories for _, calories in three_elves_with_most_calories)}")
