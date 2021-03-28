# Python Variables

## Introduction

Like any scripting language, Python supports multiple variable types.

What's super nice about Python is that it is a **dynamically-typed** language. This means you don't have to declare a variable's type when you create it, Python is clever enough to dynamically interpret what a variable is, like so:

```python
my_variable = 1
```

Python just knows this is an `int`. Whereas in a **statically-typed** language like Java, you'd have write something like:

```java
int my_variable = 1;
```

`int` is the type declaration, `my_variable` is the variable name, and `1` is the variable value, and you have to include `;` as a sort of line/instruction delimiter. Java is weird.

## Simple variable types
Python has 4 main variable types, as well as a few more complex ones.

### `string`

Strings can be created using single or double quotes, it doesn't matter which you choose, i.e.

```python
my_string = 'my string'
my_string_2 = "my string"
```
will both print `my string` to the console


### `int`

Easy one, any integer:

```python
my_int = 10
```

### `float`

Another easy one, any decimal number:

```python
my_float = 5.2
```

### `boolean`

`True` or `False` (which also evaluate to `1` and `0`, respectively):

```python
my_bool = True
```

*Note: these must start with a capital letter*
___

## Complex variable types (and how to use them)

### `list`

A list of elements. These elements can differ in type, and are contained in square brackets, `[]`.

You access a list element using `[]`:
```python
my_list = [1, 2, "my string"]
print(my_list[2])
```

would print `my string` to the console

*Note: Lists are zero-indexed, unlike MATLAB, meaning the first element always has position `0`*

Nested lists exist, and can be a pain, but as long as you understand how to access lists you'll be fine, you just use a set of square brackets for each list, for instance:

```python
my_nested_list = [[1, 2], [3, 4]]
print(my_nested_list[0][1])
```
Would print `2` *(remember lists are zero-indexed, so here we're taking the second element of the first list*


### `dict`

Slightly more complicated, dictionaries are key-value structures created using curly brackets, `{}`, like so:

```python
my_simple_dict = {"some_key": "some value"}

my_complex_dict = {
    "my_first_key": 10,
    "my_second_key": "some other value",
    "my_nested_key_1": {
        "my_nested_string_key": "hello"
    },    
    "my_nested_key_2": {
        "my_nested_list_key": [1, 2, 3]
    },
    "my_boolean_key": True
}
```

These look really complicated, but as long as you remember a few key points you'll be able to create, access and manipulate dictionaries in no time. A few key points:

1) All dictionary keys **must** be strings (meaning you can use single or double quotes, either is fine)
2) A `:` must be between the key-value pair
3) Dictionary values can be any of the types we've talked about (`string`, `int`, `float`, `boolean`, `list` or even other `dicts`)
4) Each key-value must be followed by a `,` unless it is the end of the dictionary (or nested dictionary), where it is instead followed by a `}`

You can access dictionaries using square braces, but instead of the element number you provide the key name string, i.e.
```python
print(my_simple_dict["some_key"])
```

Would print `some value`

Sometimes you come across nested dictionaries, and these are handled the same way as nested lists: use a set of square brackets for each layer you want to access, i.e.

```python
print(my_complex_dict["my_nested_key_1"]["my_nested_string_key"])
```

Would give us `hello`

Finally, you can access lists within a dictionary (or nested dictionary) through a combination of the two methods we've covered, i.e.

```python
print(my_complex_dict["my_nested_key_2"]["my_nested_list_key"][2])
```

Would give us `3`

### Other data types

There are also `tuple` and `sets` (and more complex number types), but don't worry about those for now.
`dict`

Also, when you come across `numpy` arrays (which can be multi-dimensional), access these in a similar way to lists or nested lists and you'll be fine.