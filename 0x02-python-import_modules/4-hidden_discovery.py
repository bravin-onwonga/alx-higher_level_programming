#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defined_modules = [name for name in dir(hidden_4)]
    for s in defined_modules:
        if s[0] != '_' and s[1] != '_':
            print("{}".format(s))
