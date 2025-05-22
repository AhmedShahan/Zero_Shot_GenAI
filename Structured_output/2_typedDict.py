from typing import TypedDict

class person(TypedDict):
    name: str
    cgpa: float

new_person1=person(name="Shahan",cgpa=3.5)
new_person2=person(name="Ahmed",cgpa=3.7)

new_person4=person(name="Sinthiya")
new_person3= person(name="Shahan", cgpa="3.9")
print(new_person4)
### There is no error after passing cgpa as string