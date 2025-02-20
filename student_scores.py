people_scores = {
    "html": "80%",
    "CPP": "50%"
}

def get_people_scores(Name, **subjects):
    print(f"Hello {Name}, This is your score table:")
    for sub, value in subjects.items():
        print(f"{sub} => {value}")

get_people_scores("Ahmed", **people_scores)
