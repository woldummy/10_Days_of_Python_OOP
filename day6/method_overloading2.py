# -*- coding: UTF-8 -*-
# usage of *args and **kwargs in a function
# Name: wolke
# Date: 2024-10-22
# macOS: 14.2.1  Python: 3.12



def create_profile(name, email, *args, **kwargs):
    profile = {
        'name': name,
        'email': email,
        'skills': args, 'details': kwargs}
    return profile


if __name__ == "__main__":
    # Example usage
    profile = create_profile(
        "Jane Doe", "jane@example.com", "Python", "Data Science", location="New York", status="Active")
    print(profile)
