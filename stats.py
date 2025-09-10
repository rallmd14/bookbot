def word_counting_text(words_text):
    list_words = words_text.split()
    word_count = 0
    for item in list_words:
        word_count += 1
    return word_count

def character_counting_text(list_of_characters):
    character_dictionary = {}
    list_of_characters = list_of_characters.lower()
    for i in range(0,len(list_of_characters)):
        if list_of_characters[i] in character_dictionary:
            character_dictionary[list_of_characters[i]] += 1
        elif list_of_characters[i] != " ":
            character_dictionary[list_of_characters[i]] = 1
    return character_dictionary

def sorting_dictionaries(unsorted_input_dictionary):
    list_of_dictionaries = []
    
    for item in unsorted_input_dictionary:
        temp_dictionary = {}
        temp_dictionary["char"] = item
        temp_dictionary["num"] = unsorted_input_dictionary[item]
        list_of_dictionaries.append(temp_dictionary)
    sorted_dictionary = sorted(list_of_dictionaries, key=lambda d: d['num'], reverse=True)
    return sorted_dictionary



