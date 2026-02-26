import json
import os

def create_problem(id_name, real_name, desc, code, tests):
    return {
        "id": id_name,
        "name": real_name,
        "description": desc,
        "stub": f"def {id_name}({code}):\n    # TODO: implement\n    pass\n",
        "tests": tests
    }

problems = [
    create_problem("hello_world", "Hello World", "Return the string 'Hello World!'\n\n**Hint:** Use `return 'Hello World!'`", "", [
        {"call": "hello_world()", "expected": "'Hello World!'"}
    ]),
    create_problem("add_two", "Add Two", "Given two numbers a and b, return their sum.\n\n**Hint:** Use the `+` operator, like `return a + b`", "a, b", [
        {"call": "add_two(3, 4)", "expected": "7"},
        {"call": "add_two(-1, 5)", "expected": "4"},
        {"call": "add_two(0, 0)", "expected": "0"}
    ]),
    create_problem("sub_two", "Subtract Two", "Given two numbers a and b, return the result of subtracting b from a.\n\n**Hint:** Use the `-` operator. Order matters: `return a - b`", "a, b", [
        {"call": "sub_two(10, 4)", "expected": "6"},
        {"call": "sub_two(5, 5)", "expected": "0"}
    ]),
    create_problem("mult_two", "Multiply Two", "Given two numbers a and b, return their product.\n\n**Hint:** Use the `*` operator for multiplication.", "a, b", [
        {"call": "mult_two(3, 4)", "expected": "12"},
        {"call": "mult_two(0, 5)", "expected": "0"}
    ]),
    create_problem("div_two", "Divide Two", "Return the true division of a by b. You may assume b is not 0.\n\n**Hint:** Use the `/` operator.", "a, b", [
        {"call": "div_two(10, 2)", "expected": "5.0"},
        {"call": "div_two(5, 2)", "expected": "2.5"}
    ]),
    create_problem("floor_div", "Floor Division", "Return the integer (floor) division of a by b using the // operator. You may assume b is not 0.\n\n**Hint:** Floor division discards the decimal. Use `return a // b`", "a, b", [
        {"call": "floor_div(10, 3)", "expected": "3"},
        {"call": "floor_div(5, 2)", "expected": "2"}
    ]),
    create_problem("mod_two", "Modulo", "Return the remainder of a divided by b using the % operator. You may assume b is not 0.\n\n**Hint:** Modulo gives the remainder. Use `return a % b`", "a, b", [
        {"call": "mod_two(10, 3)", "expected": "1"},
        {"call": "mod_two(14, 5)", "expected": "4"}
    ]),
    create_problem("power_two", "Exponentiation", "Return a raised to the power of b using the ** operator.\n\n**Hint:** Use `return a ** b`", "a, b", [
        {"call": "power_two(2, 3)", "expected": "8"},
        {"call": "power_two(5, 2)", "expected": "25"}
    ]),
    create_problem("string_concat", "String Concatenation", "Given two strings s1 and s2, return them concatenated together.\n\n**Hint:** You can add strings together using the `+` operator.", "s1, s2", [
        {"call": "string_concat('Hello, ', 'world!')", "expected": "'Hello, world!'"},
        {"call": "string_concat('foo', 'bar')", "expected": "'foobar'"}
    ]),
    create_problem("string_len", "String Length", "Return the length of the string s using the len() function.\n\n**Hint:** Use `return len(s)`", "s", [
        {"call": "string_len('hello')", "expected": "5"},
        {"call": "string_len('')", "expected": "0"}
    ]),
    create_problem("string_upper", "Uppercase String", "Return the string s converted entirely to uppercase.\n\n**Hint:** String methods are appended to the string. Use `return s.upper()`", "s", [
        {"call": "string_upper('hello')", "expected": "'HELLO'"},
        {"call": "string_upper('Python')", "expected": "'PYTHON'"}
    ]),
    create_problem("string_lower", "Lowercase String", "Return the string s converted entirely to lowercase.\n\n**Hint:** Use `return s.lower()`", "s", [
        {"call": "string_lower('HELLO')", "expected": "'hello'"},
        {"call": "string_lower('PyThOn')", "expected": "'python'"}
    ]),
    create_problem("string_first_char", "First Character", "Return the first character of the string s. Assume s is not empty.\n\n**Hint:** Python is 0-indexed. Use `return s[0]`", "s", [
        {"call": "string_first_char('hello')", "expected": "'h'"},
        {"call": "string_first_char('Python')", "expected": "'P'"}
    ]),
    create_problem("string_last_char", "Last Character", "Return the last character of the string s. Assume s is not empty.\n\n**Hint:** You can use negative indices starting from the end. Use `return s[-1]`", "s", [
        {"call": "string_last_char('hello')", "expected": "'o'"},
        {"call": "string_last_char('Python')", "expected": "'n'"}
    ]),
    create_problem("string_slicing", "String Slicing", "Return the first 3 characters of the string s. If s is shorter than 3 characters, return s.\n\n**Hint:** Slicing works like `s[start:end]`. Use `return s[:3]`", "s", [
        {"call": "string_slicing('hello')", "expected": "'hel'"},
        {"call": "string_slicing('hi')", "expected": "'hi'"}
    ]),
    create_problem("list_create", "Create List", "Return a list containing the integers 1, 2, and 3 in that order.\n\n**Hint:** Lists are enclosed in square brackets. `return [1, 2, 3]`", "", [
        {"call": "list_create()", "expected": "[1, 2, 3]"}
    ]),
    create_problem("list_append", "Append to List", "Given a list lst and an item, return the list with the item appended to the end.\n\n**Hint:** First use `lst.append(item)`, then `return lst`", "lst, item", [
        {"call": "list_append([1, 2], 3)", "expected": "[1, 2, 3]"},
        {"call": "list_append(['a'], 'b')", "expected": "['a', 'b']"}
    ]),
    create_problem("list_insert", "Insert into List", "Given a list lst, an index i, and an item, insert the item at the given index and return the modified list.\n\n**Hint:** First use `lst.insert(i, item)`, then `return lst`", "lst, i, item", [
        {"call": "list_insert([1, 3], 1, 2)", "expected": "[1, 2, 3]"},
        {"call": "list_insert(['a', 'c'], 1, 'b')", "expected": "['a', 'b', 'c']"}
    ]),
    create_problem("list_len", "List Length", "Return the number of items in the list lst.\n\n**Hint:** The `len()` function works on lists too! `return len(lst)`", "lst", [
        {"call": "list_len([1, 2, 3])", "expected": "3"},
        {"call": "list_len([])", "expected": "0"}
    ]),
    create_problem("list_indexing", "List Indexing", "Return the second element (index 1) of the list lst. Assume lst has at least 2 elements.\n\n**Hint:** 0-indexing means the second item is at index 1. `return lst[1]`", "lst", [
        {"call": "list_indexing([10, 20, 30])", "expected": "20"},
        {"call": "list_indexing(['a', 'b', 'c'])", "expected": "'b'"}
    ]),
    create_problem("list_slicing", "List Slicing", "Return a sublist containing the first two elements of lst. Assume lst has at least 2 elements.\n\n**Hint:** Like string slicing, use `lst[:2]`", "lst", [
        {"call": "list_slicing([10, 20, 30, 40])", "expected": "[10, 20]"},
        {"call": "list_slicing(['a', 'b', 'c'])", "expected": "['a', 'b']"}
    ]),
    create_problem("dict_create", "Create Dictionary", "Return a dictionary mapping the string 'a' to 1 and 'b' to 2.\n\n**Hint:** Dicts use curly braces. `return {'a': 1, 'b': 2}`", "", [
        {"call": "dict_create()", "expected": "{'a': 1, 'b': 2}"}
    ]),
    create_problem("dict_get", "Dictionary Get", "Given a dictionary d and a key k, return the value associated with k. Assume k exists in d.\n\n**Hint:** Access keys using brackets just like lists. `return d[k]`", "d, k", [
        {"call": "dict_get({'a': 1, 'b': 2}, 'a')", "expected": "1"},
        {"call": "dict_get({'name': 'Alice'}, 'name')", "expected": "'Alice'"}
    ]),
    create_problem("tuple_create", "Create Tuple", "Return a tuple containing the strings 'apple' and 'banana'.\n\n**Hint:** Tuples use parentheses. `return ('apple', 'banana')`", "", [
        {"call": "tuple_create()", "expected": "('apple', 'banana')"}
    ]),
    create_problem("set_create", "Create Set", "Given a list of items, return a set containing those items (removing any duplicates).\n\n**Hint:** Convert a list to a set using `return set(items)`", "items", [
        {"call": "set_create([1, 2, 2, 3])", "expected": "{1, 2, 3}"},
        {"call": "set_create([])", "expected": "set()"}
    ]),
    create_problem("bool_and", "Logical AND", "Given two booleans a and b, return True if both are True, otherwise False.\n\n**Hint:** Use the `and` keyword. `return a and b`", "a, b", [
        {"call": "bool_and(True, True)", "expected": "True"},
        {"call": "bool_and(True, False)", "expected": "False"},
        {"call": "bool_and(False, False)", "expected": "False"}
    ]),
    create_problem("bool_or", "Logical OR", "Given two booleans a and b, return True if at least one is True, otherwise False.\n\n**Hint:** Use the `or` keyword. `return a or b`", "a, b", [
        {"call": "bool_or(True, False)", "expected": "True"},
        {"call": "bool_or(False, False)", "expected": "False"}
    ]),
    create_problem("bool_not", "Logical NOT", "Given a boolean a, return its opposite (True becomes False, False becomes True).\n\n**Hint:** Use the `not` keyword. `return not a`", "a", [
        {"call": "bool_not(True)", "expected": "False"},
        {"call": "bool_not(False)", "expected": "True"}
    ]),
    create_problem("is_positive", "Is Positive (If-Else)", "Return True if n is strictly greater than 0, otherwise return False.\n\n**Hint:** You can write an if statement: `if n > 0: return True else: return False` or simply `return n > 0`.", "n", [
        {"call": "is_positive(5)", "expected": "True"},
        {"call": "is_positive(0)", "expected": "False"},
        {"call": "is_positive(-3)", "expected": "False"}
    ]),
    create_problem("is_even", "Is Even", "Return True if n is even, False otherwise.\n\n**Hint:** Check if the remainder when dividing by 2 is zero! `return n % 2 == 0`", "n", [
        {"call": "is_even(4)", "expected": "True"},
        {"call": "is_even(7)", "expected": "False"}
    ]),
    create_problem("max_of_two", "Max of Two", "Return the larger of a and b.\n\n**Hint:** You can use an if statement `if a > b:...` or the built-in `max(a, b)` function.", "a, b", [
        {"call": "max_of_two(5, 10)", "expected": "10"},
        {"call": "max_of_two(7, 3)", "expected": "7"}
    ]),
    create_problem("check_sign", "Check Sign (Elif)", "Return 'positive' if n > 0, 'negative' if n < 0, and 'zero' if n == 0.\n\n**Hint:** Chain conditions with elif. `if n > 0: ... elif n < 0: ... else: ...`", "n", [
        {"call": "check_sign(5)", "expected": "'positive'"},
        {"call": "check_sign(-2)", "expected": "'negative'"},
        {"call": "check_sign(0)", "expected": "'zero'"}
    ]),
    create_problem("sum_list", "Sum a List (For Loop)", "Given a list of numbers, return their total sum.\n\n**Hint:** You can iterate over elements like `for item in lst:` and add them to a total, or just `return sum(lst)`", "lst", [
        {"call": "sum_list([1, 2, 3])", "expected": "6"},
        {"call": "sum_list([])", "expected": "0"}
    ]),
    create_problem("count_evens", "Count Evens (Loop + If)", "Given a list of integers, return how many of them are even.\n\n**Hint:** Set a counter to 0. Loop through `for item in lst:` and if `item % 2 == 0:`, increment the counter. Return the counter.", "lst", [
        {"call": "count_evens([1, 2, 3, 4, 5, 6])", "expected": "3"},
        {"call": "count_evens([1, 3, 5])", "expected": "0"}
    ]),
    create_problem("filter_strings", "Filter Strings", "Given a list of strings, return a new list containing only the strings that have a length greater than 3.\n\n**Hint:** Create an empty list `res = []`. Loop `for s in lst:`. If `len(s) > 3:`, use `res.append(s)`. Return `res`.", "lst", [
        {"call": "filter_strings(['cat', 'dog', 'elephant', 'bird'])", "expected": "['elephant', 'bird']"},
        {"call": "filter_strings(['hi', 'yo'])", "expected": "[]"}
    ]),
    create_problem("sum_while", "Sum using While Loop", "Given an integer n, use a while loop to return the sum of all integers from 1 up to n (inclusive). Assume n >= 1.\n\n**Hint:** Initialize `total = 0` and `i = 1`. `while i <= n:`, add `i` to `total` and do `i += 1`. Return `total`.", "n", [
        {"call": "sum_while(3)", "expected": "6"},
        {"call": "sum_while(5)", "expected": "15"}
    ]),
    create_problem("type_check_int", "Type Check Integer", "Return True if the variable x is an integer, False otherwise.\n\n**Hint:** Use `return type(x) is int` or `return isinstance(x, int)`", "x", [
        {"call": "type_check_int(5)", "expected": "True"},
        {"call": "type_check_int(5.0)", "expected": "False"},
        {"call": "type_check_int('5')", "expected": "False"}
    ]),
    create_problem("type_check_str", "Type Check String", "Return True if the variable x is a string, False otherwise.\n\n**Hint:** Use `return isinstance(x, str)`", "x", [
        {"call": "type_check_str('hello')", "expected": "True"},
        {"call": "type_check_str(123)", "expected": "False"}
    ]),
    create_problem("string_to_int", "String to Integer", "Given a string that contains an integer (like '42'), return it converted to an int.\n\n**Hint:** Cast it using `return int(s)`", "s", [
        {"call": "string_to_int('42')", "expected": "42"},
        {"call": "string_to_int('-10')", "expected": "-10"}
    ]),
    create_problem("int_to_string", "Integer to String", "Given an integer n, return it converted to a string.\n\n**Hint:** Cast it using `return str(n)`", "n", [
        {"call": "int_to_string(42)", "expected": "'42'"},
        {"call": "int_to_string(-10)", "expected": "'-10'"}
    ])
]

# We need to insert this right after "Tutorial", so at index 1 in exercises_data.js
category_obj = {
    "name": "Python Tutorial",
    "problems": problems
}

def update_exercises_data():
    exercises_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "exercises_data.js")
    with open(exercises_data_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We parse the JSON part
    prefix = "// Auto-generated CodingBat exercises data\nconst EXERCISES_DATA = "
    if not content.startswith(prefix):
        print("Could not find expected prefix.")
        return
        
    # The JSON string ends with ";\n"
    json_str = content[len(prefix):-2]
    
    try:
        data = json.loads(json_str)
    except Exception as e:
        print("Error parsing JSON:", e)
        return
        
    # Remove existing 'Python Tutorial' to prevent duplicates
    data["categories"] = [cat for cat in data["categories"] if cat["name"] != "Python Tutorial"]
    
    # Insert at index 1
    data["categories"].insert(1, category_obj)
    
    # Write back
    new_content = prefix + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
    with open(exercises_data_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Successfully updated exercises_data.js with Python Tutorial problems and hints!")

if __name__ == "__main__":
    update_exercises_data()
