initial = ["at_home"]
goal = ["at_college"]

actions = {
    "go_college": {
        "pre": ["at_home"],
        "add": ["at_college"],
        "del": ["at_home"]
    }
}

state = initial.copy()

for action in actions:
    if all(p in state for p in actions[action]["pre"]):
        state += actions[action]["add"]
        for d in actions[action]["del"]:
            state.remove(d)

print(state)
