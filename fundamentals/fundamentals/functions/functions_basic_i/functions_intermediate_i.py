############### PART ONE ######################################

###############################################################

# Update Values in Dictionaries and Lists
# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ]

# create a function that takes 3 parameters (list, orignial value, value to be assigned) and returns updated list
def change_list_value(given_list, old_val, new_val):
    # print(l)
# access the list at index 1, access the value at index 0
    for i in range(0, len(given_list)): #access first layer of indexed lists
        # print(i, given_list[i])
        for j in range(0, len(given_list[i])): #access elements in given_list[i]
            # print("value of j", given_list[i][j])
            if given_list[i][j] == old_val: # if value of access element is the same as original value
                given_list[i][j] = new_val # assign new_value as element value
                # print("new list", given_list[i])
    
    # print ("new x", given_list) check output
    return given_list



change_list_value(x, 10, 15)
print(x)

#this function does not account for multiple occurances nor for the original value not being present in the given list 
#################################

# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

# create a function that takes 4 parameters (list, item number, key to be updated, new value)

def change_last_name(l, num, key_name, new_value):
    print("students", l) #check list access
    student_index = num - 1 # access first student. l[num-1]
    # print("student_index", student_index) 
    pupil = l[student_index]
    # print("pupil", pupil)
    pupil[key_name] = new_value #access student's last name, assign new value to last name
    print("pupil", pupil) #check new last name
    print("new roster", l)

    return l

change_last_name(students, 1, 'last_name', 'Bryant')
print(students)
###########################

# 3. In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

def change_dic_list_item(l, old_val, new_val):
    # print(l.keys())
    for k in l.keys():
        # print(k)
        sport = l[k]
        for i in range(0, len(sport)):
            # print(i, sport[i])
            if sport[i] == old_val:
                sport[i] = new_val
                # print(sport)
    print(l)
    return l

change_dic_list_item(sports_directory, 'Messi', 'Andres')
print(sports_directory)
##############################


# 4. Change the value 20 in z to 30

z = [ {'x': 10, 'y': 20} ]

#create a function that takes 3 parameters (list, current_value, new_value)
def replace_dic_list_value(l, current_value, new_value):
# iterate over the list to access the nested dictionary 
    li_len = len(l)
    nested_dic = l[li_len - 1]
    print(nested_dic)
# list out keys
    k_list = list(nested_dic.keys())
    print("keys", k_list)
# list out values
    v_list = list(nested_dic.values())
    print("values", v_list)
#find index of current_value
    position = v_list.index(current_value)
    print("index", position)
# find key of current_value
    curr_key = k_list[position]
    print("curr_key", curr_key)
# asign new value to key
    nested_dic[curr_key] = new_value
    print(nested_dic[curr_key])

    print(l)
    return l

replace_dic_list_value(z, 20, 30)
print(z)



#####################################################################

############ PART TWO ###################################

# Iterate Through a List of Dictionaries

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(some_list):
# loop through list
    for i in range(0, len(some_list)):
        # print(some_list[i])
        l_std = ""
        # temp = ""
# print each key and associated value 
        for j in some_list[i]:
            k = j
            v = some_list[i][j]
            l_std += f"{k} - {v}, " # conditional needed to remove comma from end of string

        print(l_std)

iterateDictionary(students) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;

# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#####################################################################

############ PART THREE ###################################

# Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
# loop through list
    for i in range(0, len(some_list)):
        # print value stored 
        print(some_list[i][key_name])

iterateDictionary2('first_name', students) 
iterateDictionary2('last_name', students) 


#####################################################################

############ PART FOUR ###################################


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    # print(some_dict.keys())
    for k in some_dict.keys():
        # print("key:",k)
        dojo_list = some_dict[k]
        amount = len(dojo_list)
        print(amount, k)

        for i in dojo_list:
            print(i)

printInfo(dojo)
