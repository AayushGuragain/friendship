import random
if __name__ == '__main__':
    initial_database = open('names.txt', 'r')
    saved_secondary_database = open('names_chosen_already.txt', 'r')
    next_save = open('names_chosen_already.txt', 'a')
    original_contents = initial_database.read()
    saved_contents = saved_secondary_database.read()
    original_lines = original_contents.split('\n')
    saved_lines = saved_contents.split('\n')
    random_choice = random.choice(original_lines)

    while random_choice in saved_lines:
        random_choice = random.choice(original_lines)
        if len(original_lines) == len(saved_lines) - 1:
            random_choice = 'NO MORE CHOICES'

    print(f"How about calling {random_choice} today?")
    if random_choice != 'NO MORE CHOICES':
        next_save.write(random_choice)
        next_save.write('\n')

    initial_database.close()
    saved_secondary_database.close()
    next_save.close()
