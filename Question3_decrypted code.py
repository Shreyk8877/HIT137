# QUESTION 3
# Correct the errors and provide the comments, encryped code.

# Correct the errors code
# Global variable initialisation
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} 

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove (local_variable)
        local_variable -= 1
    
    return numbers

# Set initialisation
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()  # this method takes no argument but 1 was provided

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

# Dictionary initialisation
modify_dict() # this method takes no argument but 1 was provided

def update_global():
    global global_variable 
    global_variable += 10

# Loop for demonstration
for i in range(5):
    print(i)
    i += 1

# Conditional checks
if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

# Printing results
print(global_variable)
print (my_dict)
print (my_set)
