#dict lookup is O(1)

#so if we have a dict of mapping first_names->last_names
# then we can look up the first names and return the last names for just O(1)

def find_last_name(names_dict, first_name):

    return names_dict.get(first_name)
    #this will directly return None if firstname doest exist in the dict

    #or 
    return names_dict[first_name]
    # this one will not return a None if there is no first name in the names_dict


    

