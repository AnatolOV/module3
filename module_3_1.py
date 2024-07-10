calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    lenghOfString = len(string)
    upperString = string.upper()
    lowString = string.lower()
    count_calls()

    return (lenghOfString, upperString, lowString)

def is_contains(string, list_to_search):
    count_calls()
    count = 0
    for i in list_to_search:
        if string.upper() == i or string.lower() == i:
            count += 1
        else:
            count += 0
    if count > 0:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

