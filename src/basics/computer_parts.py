available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                  ]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

current_choice = "-"
computer_parts = []
while current_choice != "0":
    if current_choice in valid_choices:
        # if available_parts[int(current_choice) - 1] in computer_parts:
        #     computer_parts.remove(available_parts[int(current_choice) - 1])
        #     print(computer_parts)
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)

    else:
        print("Please choose an option from below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)