from person import Person
    people = []
    people.append(Person("Shawn", "Thomas", 25))
    people.append(Person("Blake", "Stelter", 28))
    people.append(Person("Brianna", "Murphy", 27))

for person in people:
    print("{} {} is {}".format(person.first_name, person.last_name,  person.age))