calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(text):
    count_calls()
    list_ = [len(text), text.upper(), text.lower()]
    return tuple(list_)


def is_contains(string_="", list_to_search=None):
    count_calls()
    if list_to_search is None:
        list_to_search = []
    list_to_search = [x.upper() for x in list_to_search]
    return string_.upper() in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
