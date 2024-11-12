# Creating Primitive data types
data_int: int = 20
data_float: float = 10.3
data_str: str = 'Suraj Kumar Mahato'
data_bool: bool = True

# Operations on each primitive data type
print(data_int + 1)  # Arithmetic operation on int
print(data_float + 0.3)  # Arithmetic operation on float
print(data_str + ' is learning Python')  # String concatenation
print(data_bool and False)  # Logical operation

# Creating dictionary to store and display these variables by their types as keys
data_dict = {'int': data_int, 'float': data_float, 'str': data_str, 'bool': data_bool}
print(data_dict)  # Displaying the dictionary
