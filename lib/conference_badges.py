def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    badge_list = []
    for name in names:
        badge_list.append(f"Hello, my name is {name}.")
    return badge_list


def assign_rooms(names):
    room_assignment = []
    for index, name in enumerate(names):
        room_assignment.append(
            f"Hello, {name}! You'll be assigned to room {index + 1}!")
    return room_assignment


def printer(names):
    badges = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in badges:
        print(badge)
    for room in rooms:
        print(room)
