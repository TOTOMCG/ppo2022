#! /usr/bin/env python3
import sys
import json
from uuid import uuid4
from random import randint
from faker import Faker

domain_names = ["email.ru", "yandex.ru", "google.com", "rambler.ru"]

fake = Faker(["ru_RU"])


def get_rdi():
    return randint(0, len(domain_names) - 1)


def email():
    e = fake.email()
    return f"{e.split('@')[0]}@{domain_names[get_rdi()]}"


def main(count=10):
    acc = []
    for _ in range(count):
        names = fake.name().split(" ")
        acc.append({
            "uuid": str(uuid4()),
            "username": fake.user_name(),
            "password": None,
            "email": email(),
            "first_name": names[0],
            "middle_name": names[1],
            "last_name": names[2],
        })
    print(json.dumps(acc, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    count = 10
    if len(sys.argv) > 2:
        try:
            count = int(sys.argv[1])
        except Exception:
            pass
    main(count)
