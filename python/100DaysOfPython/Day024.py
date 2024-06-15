# Day 24
# File Operations

with open("Day024_Names.txt") as names:
    for i in names.readlines():
        with open(f"letter_for_{i.strip()}.txt", "w") as letter:
            message = f"Dear {i.strip()},\n\nYou are invited to my birthday this Saturday. \n\nHope you can make it!\n\nTheBirthdayGuy"
            letter.write(message)
