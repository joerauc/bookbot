def split_string(text_contents):
    return text_contents.strip().split()

def get_word_count(text_contents):
    return len(split_string(text_contents))

def sort_on(vals):
    return vals["num"]

# def sort_char_count(char_list):
#     dict_list = []

#     print(type(char_list))

#     for original_key in char_list.keys():
#         original_val = char_list[original_key]
#         dict_list.append({"name": original_key, "num" : original_val})
    
#     print(dict_list.sort(reverse=True, key=sort_on))

#     return dict_list.sort(reverse=True, key=sort_on)

def beautify_print(char_list):
    for pair in char_list:
        name = pair["name"]
        num = pair["num"]
        print(f"{name}: {num}")

def get_char_count(text_contents):
    char_dict = {}
    sorted_list = []
    
    split_string_arr = split_string(text_contents)
    for word in split_string_arr:
        for char in word:
            lowercase = char.lower()
            if lowercase in char_dict:
                char_dict[lowercase] += 1
            else:
                char_dict[lowercase] = 1

    for original_key in char_dict.keys():
        original_val = char_dict[original_key]
        sorted_list.append({"name": original_key, "num" : original_val})

    sorted_list.sort(reverse=True, key=sort_on)

    beautify_print(sorted_list)