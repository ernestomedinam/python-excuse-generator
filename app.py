from random import randint, seed

who = ["my dog", "my mom", "my brother", "my dad"]
did = ["ate", "pissed on", "crushed", "broke"]
what = ["my homework", "car's engine", "my uniform", "grandma's food"]
when = ["right before class", "at night", "at lunch", "during breakfast"]

def choose_random(items_list):
    """ receives a list and returns a randomly selected item """
    seed()
    return items_list[randint(0, len(items_list) - 1)]

print(f"{choose_random(who)} {choose_random(did)} {choose_random(what)} {choose_random(when)}")

# excuse = f"{choose_random(who)} {choose_random(did)} {choose_random(what)} {choose_random(when)}"

# who_index = randint(0, 3)
# seed()
# did_index = randint(0, 3)
# seed()
# what_index = randint(0, 3)
# seed()
# when_index = randint(0, 3)
# excuse = f"{who[who_index]} {did[did_index]} {what[what_index]} {when[when_index]}" 

#print(excuse)