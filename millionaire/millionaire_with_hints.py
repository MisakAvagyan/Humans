import random
import os.path


def get_random_5_questions(questions):
    tmp = []
    while len(tmp) < 5:
        num = random.randint(0, len(questions) - 1)
        if questions[num] not in tmp:
            tmp.append(questions[num])
    return tmp


def structure_questions(tmp):
    gquestions = {}

    for el in tmp:
        q, a = el.split("?")
        gquestions[q] = a.split(",")
    return gquestions





def get_random_5_questions(questions):
    tmp = []
    while len(tmp) < 5:
        num = random.randint(0, len(questions) - 1)
        if questions[num] not in tmp:
            tmp.append(questions[num])
    return tmp


def structure_questions(tmp):
    gquestions = {}

    for el in tmp:
        q, a = el.split("?")
        gquestions[q] = a.split(",")
    return gquestions




def game(gquestions):
    cnt = 0
    used_hints = {
        "50/50": False,
        "phone_a_friend": False,
        "audience_help": False
    }

    for q, a in gquestions.items():
        print(q)
        options = a[:]

        random.shuffle(options)
        print_options(options)

        print_hints(used_hints)

        while True:
            choice = input("Enter your answer or hint choice (1/2/3): ")
            if choice == "1" and not used_hints["50/50"]:
                used_hints["50/50"] = True
                print("Two wrong answers have been removed." + a[0] + ', ' + random.choice(options[1:4]))
            elif choice == "2" and not used_hints["phone_a_friend"]:
                used_hints["phone_a_friend"] = True
                print("Your friend says: The answer is '" + a[0] + "'")
            elif choice == "3" and not used_hints["audience_help"]:
                used_hints["audience_help"] = True
                audience_choice = random.choice(options)
                print("The audience thinks the answer is '" + audience_choice + "'")
            elif choice in ("1", "2", "3"):
                print("You have already used that hint.")
            else:
                if choice == a[0]:
                    print("Correct")
                    cnt += 1
                else:
                    print("Incorrect. The correct answer was", a[0])
                break

    print("You got %d/5" % cnt)
    return cnt



def print_options(options):
    for idx, opt in enumerate(options, start=1):
        print(f"{idx}. {opt}")


def print_hints(used_hints):
    if not used_hints["50/50"]:
        print("\n1. Use hint: 50/50")
    if not used_hints["phone_a_friend"]:
        print("\n2. Use hint: Phone a friend")
    if not used_hints["audience_help"]:
        print("\n3. Use hint: Ask the audience")





def get_questions_from_file(fname):
    with open(fname) as f:
        return f.readlines()


def sanitize_data(ml):
    return [el.strip() for el in ml]


def check_file_existence(fname):
    if not os.path.isfile(fname):
        print("Your files does not exists: %s. Please check" % fname)
        return False
    return True


def get_top_players_from_file(fname):
    with open(fname) as f:
        return f.readlines()


def create_file(fname):
    f = open(fname, "w")
    f.close()


def create_players_dict(data):
    # should be written "username: XP"
    md = {}
    for el in data:
        p, x = el.split(": ")
        md[p] = int(x)
    return md


def confirm_username(username, players):
    if username in players:
        ans = input("Would you like to rewrite your XP? ")
        if ans.lower() == "y":
            pass
        else:
            username = input("Enter your username: ")
            while username in players:
                username = input("Enter your username: ")
    return username


def sort_players_by_xp(players):
    ml = list(players.items())
    ml.sort(key=lambda x: x[1], reverse=True)
    return ml


def write_player_xp(fname, ml):
    with open(fname, "w") as f:
        for pl, xp in ml:
            f.write(pl + ": " + str(xp) + "\n")


def main():
    username = input("Enter your username: ")
    question_file = "questions.txt"
    fl = check_file_existence(question_file)
    if not fl:
        exit()
    top_file = "top_players.txt"
    fl = check_file_existence(top_file)
    if not fl:
        create_file(top_file)
    players_data = get_top_players_from_file(top_file)
    players = sanitize_data(players_data)
    players_dict = create_players_dict(players)
    username = confirm_username(username, players_dict)
    questions = get_questions_from_file(question_file)
    questions = sanitize_data(questions)
    random5 = get_random_5_questions(questions)
    game_questions = structure_questions(random5)
    xp = game(game_questions)
    players_dict[username] = xp
    players = sort_players_by_xp(players_dict)
    write_player_xp(top_file, players)


main()
