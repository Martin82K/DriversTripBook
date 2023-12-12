import random
import string

from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=5))


@dataclass(kw_only=True)
class Driver:
    name: str
    surname: str
    phone: int
    email: str
    _person_id: int = field(init=True, repr=True, default_factory=generate_id)


def main() -> None:
    person1 = Driver(name="Petr", surname="Svetr", phone=123456789, email="petr.svetr@nevim.cz")
    print(person1)


if __name__ == "__main__":
    main()
