class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    instances = []
    for data in people_data:
        person = Person(data["name"], data["age"])
        instances.append(person)

    for data in people_data:
        current_person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            wife_name = data["wife"]
            current_person.wife = Person.people[wife_name]

        if "husband" in data and data["husband"] is not None:
            husband_name = data["husband"]
            current_person.husband = Person.people[husband_name]

    return instances
