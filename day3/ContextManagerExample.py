# -*- coding: UTF-8 -*-
# 
# Name: wolke
# Date: 2024-09-10
# macOS: 14.2.1  Python: 3.12


class ManagedFile:

    def __init__(self, name):
        self.name = name
        self.file = None

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


if __name__ == "__main__":
    # usage of try/except/finally
    try:
        file = open("myfile.txt", "r")
    except FileNotFoundError as e:
        print(str(e))
    except Exception as e:
        print(str(e))
    # do something
    finally:
        if file:
            file.close()


    # usage of ContextManger
    with open("myfile.txt", "r") as file:
        # do something
        pass

    # usage of own ContextManager
    with ManagedFile('hello.txt') as file:
        file.write('hello, world!\n')
        file.write('bye now\n')
