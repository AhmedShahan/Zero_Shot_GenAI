from typing import TypedDict

class person(TypedDict):
    name: str
    cgpa: float

new_person1=person(name="Shahan",cgpa=3.5)
new_person2=person(name="Ahmed",cgpa=3.7)

print(new_person2)