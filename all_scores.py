people_scores = {
    "html": "80%",
    "CPP": "50%"
}

def get_people_scores(Name, subjects):  # استلام القاموس ككائن واحد
    print(f"Hello {Name}, This is your score table:")
    for sub, value in subjects.items():
        print(f"{sub} => {value}")

get_people_scores("Ahmed", people_scores)  # تمرير القاموس كما هو بدون تفكيك
