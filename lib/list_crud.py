def create_an_empty_list():
    return []

def create_a_list():
     return [3,5,9,14]

def add_element_to_end_of_list(new_list, element):
    new_list.append(element)
    return new_list

def add_element_to_start_of_list(new_list, element):
    new_list.insert(0, element)
    return new_list

def remove_element_from_end_of_list(new_list):
    new_list.pop()
    return new_list

def remove_element_from_start_of_list(new_list):
    del new_list[0]
    return new_list

def retrieve_first_element_from_list(new_list):
    return new_list[0]

def retrieve_element_from_index(new_list, index):
    return new_list[index]

def retrieve_last_element_from_list(new_list):
    return new_list[-1]
