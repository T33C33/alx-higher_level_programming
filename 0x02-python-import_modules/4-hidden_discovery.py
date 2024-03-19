#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    f_names = [
            current_name for current_name in names
            if not current_name.startswith('__')
    ]
    f_names.sort()
    for current_name in f_names:
        print(current_name)
