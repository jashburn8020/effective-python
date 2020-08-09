# Effective Python

Summary and examples from the book Effective Python, 2nd edition

- [Effective Python](#effective-python)
  - [1. Pythonic Thinking](#1-pythonic-thinking)
    - [Item 1: Know Which Version of Python You're Using](#item-1-know-which-version-of-python-youre-using)
    - [Item 2: Follow the PEP 8 Style Guide](#item-2-follow-the-pep-8-style-guide)
    - [Item 3: Know the Differences Between `bytes` and `str`](#item-3-know-the-differences-between-bytes-and-str)
    - [Item 4: Prefer Interpolated F-Strings Over C-style Format Strings and `str.format`](#item-4-prefer-interpolated-f-strings-over-c-style-format-strings-and-strformat)
    - [Item 5: Write Helper Functions Instead of Complex Expressions](#item-5-write-helper-functions-instead-of-complex-expressions)
    - [Item 6: Prefer Multiple Assignment Unpacking Over Indexing](#item-6-prefer-multiple-assignment-unpacking-over-indexing)
    - [Item 7: Prefer `enumerate` Over `range`](#item-7-prefer-enumerate-over-range)
    - [Item 8: Use `zip` to Process Iterators in Parallel](#item-8-use-zip-to-process-iterators-in-parallel)
    - [Item 9: Avoid `else` Blocks After `for` and `while` Loops](#item-9-avoid-else-blocks-after-for-and-while-loops)
    - [Item 10: Prevent Repetition with Assignment Expressions](#item-10-prevent-repetition-with-assignment-expressions)
  - [2. Lists and Dictionaries](#2-lists-and-dictionaries)
    - [Item 11: Know How to Slice Sequences](#item-11-know-how-to-slice-sequences)
    - [Item 12: Avoid Striding and Slicing in a Single Expression](#item-12-avoid-striding-and-slicing-in-a-single-expression)
    - [Item 13: Prefer Catch-All Unpacking Over Slicing](#item-13-prefer-catch-all-unpacking-over-slicing)
    - [Item 14: Sort by Complex Criteria Using the `key` Parameter](#item-14-sort-by-complex-criteria-using-the-key-parameter)
    - [Item 15: Be Cautious When Relying on `dict` Insertion Ordering](#item-15-be-cautious-when-relying-on-dict-insertion-ordering)
    - [Item 16: Prefer `get` Over `in` and `KeyError` to Handle Missing Dictionary Keys](#item-16-prefer-get-over-in-and-keyerror-to-handle-missing-dictionary-keys)
    - [Item 17: Prefer `defaultdict` Over `setdefault` to Handle Missing Items in Internal State](#item-17-prefer-defaultdict-over-setdefault-to-handle-missing-items-in-internal-state)
    - [Item 18: Know How to Construct Key-Dependent Default Values with `__missing__`](#item-18-know-how-to-construct-key-dependent-default-values-with-__missing__)
  - [Source](#source)

## 1. Pythonic Thinking

### Item 1: Know Which Version of Python You're Using

- Be sure that the command-line executable for running Python on your system is the version you expect it to be
- Avoid Python 2 because it will no longer be maintained after January 1, 2020

### Item 2: Follow the PEP 8 Style Guide

- Using a consistent style makes your code more approachable and easier to read
- [PEP 8](https://www.python.org/dev/peps/pep-0008/) is the style guide for how to format Python code

### Item 3: Know the Differences Between `bytes` and `str`

- `bytes` contains sequences of 8-bit values, and `str` contains sequences of Unicode code points
- Do encoding and decoding of Unicode data at the furthest boundary of your interfaces
  - the _Unicode sandwich_
- The core of your program should use the `str` type containing Unicode data and should not assume anything about character encodings
  - allows you to be very accepting of alternative text encodings (such as Latin-1, Shift JIS, and Big5) while being strict about your output text encoding (ideally, UTF-8)

### Item 4: Prefer Interpolated F-Strings Over C-style Format Strings and `str.format`

- See [`interpolated_f_strings_test.py`](src/ch01/interpolated_f_strings_test.py)
- Python has four different ways of formatting strings that are built into the language and standard library
  - all but one of them have serious shortcomings
- The `%` formatting operator
  - `formatted = '%-10s = %.2f' % (key, value)`
  - if you change the type or order of data values in the tuple on the right side of a formatting expression, you can get errors due to type conversion incompatibility
    - similarly so if you change the format string
    - you need to constantly check that the two sides of the `%` operator are in sync - error prone
    - see `test_c_printf_style_change_order()`
  - they become difficult to read when you need to make small modifications to values before formatting them into a string
    - can cause the tuple in the formatting expression to become so long that it needs to be split across multiple lines
    - see `test_c_printf_style_small_modifications()`
  - if you want to use the same value in a format string multiple times, you have to repeat it in the right side tuple
    - error prone if you have to repeat small modifications to the values being formatted
  - using a dictionary instead of a tuple
    - causes formatting expressions to become longer and ore visually noisy because of the presence of the dictionary key and colon operator on the right side
    - increases verbosity - each key must be specified at least twice
      - once in the format specifier
      - once in the dictionary as a key
      - potentially once more for the variable name that contains the dictionary value
    - see `test_c_printf_style_dictionary()`
- `format` built-in and `str.format`
  - `#{}: {} (£{:.2f}): {}".format(item_number + 1, fruit.title(), price, round(count))`
  - leaves your code difficult to read when you need to make small modifications to values before formatting them
    - see `test_format_small_modifications()`
  - doesn't help reduce the redundancy of repeated keys
- Interpolated format strings
  - `f"#{item_number + 1}: {fruit.title()} (£{price:.2f}): {round(count)}"`
  - shorter than using C-style format strings with the `%` operator and the `str.format` method in all cases
  - enable you to put a full Python expression within the placeholder braces
  - see `test_f_string_small_modifications()`

### Item 5: Write Helper Functions Instead of Complex Expressions

- See [`helper_functions.py`](src/ch01/helper_functions.py)
- Python's syntax makes it easy to write single-line expressions that implement a lot of logic
  - this can make expressions difficult to read due to visual noise
  - see `test_parse_query_string_complex()`
- As soon as expressions get complicated, consider splitting them into smaller pieces and moving logic into helper functions to ease reading
  - see `test_parse_query_string_helper()`

### Item 6: Prefer Multiple Assignment Unpacking Over Indexing

- See [`assignment_unpacking_test.py`](src/ch01/assignment_unpacking_test.py)
- Python has a built-in tuple type that can be used to create immutable, ordered sequences of values
  - in the simplest case, a tuple is a pair of two values
- Python also has syntax for unpacking, which allows for assigning multiple values in a single statement
  - has less visual noise than accessing the tuple's indexes, and it often requires fewer lines
- Unpacking can even be used to swap values in place without the need to create temporary variables
  - `a[i-1], a[i] = a[i], a[i-1]`
  - the right side of the assignment (`a[i], a[i-1]`) is evaluated first, and its values are put into a new temporary, unnamed tuple
  - the unpacking pattern from the left side of the assignment (`a[i-1], a[i]`) is used to receive that tuple value
  - the temporary unnamed tuple silently goes away
- Another valuable application of unpacking is in the target list of `for` loops and similar constructs, such as comprehensions and generator expressions
  - `for rank, (name, calories) in enumerate(snacks, 1)`
  - see `test_unpack_for_loop()`

### Item 7: Prefer `enumerate` Over `range`

- See [`assignment_unpacking_test.py`](src/ch01/assignment_unpacking_test.py)
- Often, you'll want to iterate over a list and also know the index of the current item in the list
- One way to do it is by using `range`
  - harder to read
    - `for i in range(len(snacks))`
    - `item = snacks[i]`
- Python provides the `enumerate` built-in function
  - wraps any iterator with a lazy generator
  - yields pairs of the loop index and the next value from the given iterator
  - each pair can be succinctly unpacked in a `for` statement
  - see `test_unpack_for_loop()`

### Item 8: Use `zip` to Process Iterators in Parallel

- See [`zip_iterators_test.py`](src/ch01/zip_iterators_test.py)
- Often in Python you find yourself with many lists of related objects
  - related by their indexes
  - to iterate over the lists parallel, you can iterate over the length of one of the lists
    - index into the lists by the loop index
    - see `test_longest_name()`
- Python provides the `zip` built-in function
  - wraps two or more iterators with a lazy generator
  - generator yields tuples containing the next value from each iterator
  - tuples can be unpacked directly within a `for` statement
  - `for name, count in zip(names, counts)`
  - see `test_longest_name_zip()`
- `zip` consumes the iterators it wraps one item at a time
  - can be used with infinitely long inputs
- When the input iterators are of different lengths
  - `zip` keeps yielding tuples until any one of the wrapped iterators is exhausted
  - output is as long as its shortest input
  - use the `zip_longest` function from the `itertools` built-in module if you don't expect the lengths of the lists to be equal
    - replaces missing values with whatever `fillvalue` is passed to it, which defaults to `None`

### Item 9: Avoid `else` Blocks After `for` and `while` Loops

- See [`else_after_for_while_test.py`](src/ch01/else_after_for_while_test.py)
- You can put an `else` block immediately after a loop's repeated interior block
  - means "do this if the loop was (not wasn't) completed"
    - the loop breaking out using a `break` statement skips the `else` block
    - see `test_coprime_else()`
  - also runs if:
    - loop over an empty sequence
    - `while` loop is initially `False`
- `else` with other types of statements works differently:
  - `if`/`else`: "do this if the block before doesn't happen"
  - `try`/`except`/`else`: "do this if there was no exception to handle"
- Behaviour isn't intuitive and can be confusing
  - expressivity you gain from the `else` block doesn't outweigh the burden you put on people who want to understand your code in the future
- Use a helper function
  - see `test_coprime_helper()`

### Item 10: Prevent Repetition with Assignment Expressions

- See [`assignment_expression_test.py`](src/ch01/assignment_expression_test.py)
- An assignment expression (the walrus operator) is a new syntax introduced in Python 3.8
  - enables you to assign variables in places where assignment statements are disallowed
    - such as in the conditional expression of an `if` or `while` statement
  - its value evaluates to whatever was assigned to the identifier on the left side of the walrus operator
  - assign and evaluate variable names in a single expression - reduces repetition
- In general, when you find yourself repeating the same expression or assignment multiple times within a grouping of lines, consider using assignment expressions in order to improve readability
  - see `test_walrus()`

## 2. Lists and Dictionaries

### Item 11: Know How to Slice Sequences

- Slicing allows you to access a subset of a sequence's items with minimal effort
- The simplest uses for slicing are the built-in types `list`, `str`, and `bytes`
- Slicing can be extended to any Python class that implements the `__getitem__` and `__setitem__` special methods
- When slicing from the start of a list, you should leave out the zero index to reduce visual noise
- When slicing to the end of a list, you should leave out the final index because it's redundant
- Using negative numbers for slicing is helpful for doing offsets relative to the end of a list
- The result of slicing a list is a whole new list
  - if you leave out both the start and the end indexes when slicing, you end up with a copy of the original list
- When used in assignments, slices replace the specified range in the original list
  - `a[2:7] = [99, 22, 14]`
  - the list grows or shrinks depending on the length of the replacement list relative to the slice
  - if you assign to a slice with no start or end indexes, you replace the entire contents of the list with a copy of what's referenced (instead of allocating a new list)

### Item 12: Avoid Striding and Slicing in a Single Expression

- See [`striding_slicing_test.py`](src/ch02/striding_slicing_test.py)
- Python has special syntax for the stride of a slice in the form `somelist[start:end:stride]`
  - take every nth item when slicing a sequence
- A common Python trick for reversing a string is to slice the string with a stride of -1
  - works correctly for Unicode strings
  - breaks when Unicode data is encoded as a UTF-8 byte string
  - see `test_reverse_stride_unicode()`
- The stride part of the slicing syntax can be confusing, especially when the stride is negative
  - hard to read because of its density
- Avoid using a stride along with start and end indexes
- If you must use a stride, prefer making it a positive value and omit start and end indexes
- If you must use a stride with start or end indexes, consider using one assignment for striding
  and another for slicing
  - first operation to reduce the size of the resulting slice
- Consider using `itertools` built-in module's `islice` method

### Item 13: Prefer Catch-All Unpacking Over Slicing

- See [`catch_all_unpacking_test.py`](src/ch02/catch_all_unpacking_test.py)
- One limitation of basic unpacking is that you must know the length of the sequences you're unpacking in advance
- Example: extracting the rest of the elements in a list through slicing
  - indexing and slicing is visually noisy
  - error prone to divide the members of a sequence into various subsets
    - you're more likely to make off-by-one errors
    - you might change boundaries on one line and forget to update the others
  - see `test_catch_all_slicing()`
- Python supports catch-all unpacking through a _starred expression_
  - allows one part of the unpacking assignment to receive all values that didn't match any other part of the unpacking pattern
    - `oldest, older, *others = [20, 19, 15, 9, 8]`
    - `oldest, *others, youngest = [20, 19, 15, 9, 8]`
    - see `test_catch_all_starred_expression()`
  - you can also unpack arbitrary iterators with the unpacking syntax along with a starred expression

### Item 14: Sort by Complex Criteria Using the `key` Parameter

- See [`sort_using_key_test.py`](src/ch02/sort_using_key_test.py)
- The `list` built-in type provides a `sort` method for ordering items in a list based on a variety of criteria
- By default, `sort` will order a `list`'s contents by the natural ascending order of the items
  - sorting objects by their natural order doesn't work if the objects' class does not define comparison special methods, which are called by the `sort` method
  - your objects may also need to support multiple orderings, in which case defining a natural order doesn't help
- The `sort` method accepts a `key` parameter that's expected to be a function
  - the `key` function is passed a single argument, which is an item from the list that is being sorted
  - the return value of the `key` function should be a comparable value (i.e., with a natural ordering) to use in place of an item for sorting purposes
  - `tools.sort(key=lambda tool: tool.name)`
  - see `test_sort_attribute()`
- Sometimes you may need to use multiple criteria for sorting
  - the simplest solution is to use the tuple type
  - comparable by default and have a natural ordering
  - they implement all of the special methods, such as `__lt__`, that are required by the `sort` method
    - iterating over each position in the tuple and comparing the corresponding values one index at a time
    - if the first position in the tuples being compared are equal, then the tuple comparison will move on to the second position, and so on
  - limitation: sorting for all criteria must be in the same order
    - `power_tools.sort(key=lambda tool: (tool.weight, tool.name))`
    - see `test_sort_multiple_criteria()`
  - for numerical values, it's possible to mix sorting directions by using the unary minus operator in the `key` function
    - `power_tools.sort(key=lambda tool: (-tool.weight, tool.name))`
    - see `test_sort_multiple_criteria_rev_numerical()`
  - for non-numerical values, make use of `sort`'s stable sorting (the order of two equal elements is maintained)
    - call `sort` multiple times on the same list to combine different criteria together
    - execute the sorts in the opposite sequence of what you want the final list to contain
    - see `test_sort_multiple_criteria_rev_non_numerical()`

### Item 15: Be Cautious When Relying on `dict` Insertion Ordering

- In Python 3.5 and before, iterating over a `dict` would return keys in arbitrary order
- Starting with Python 3.6, and officially part of the Python specification in version 3.7, dictionaries preserve insertion order
- Note: The `collections` built-in module has had an `OrderedDict` class that preserves insertion ordering
  - if you need to handle a high rate of key insertions and `popitem` calls (e.g., to implement a least-recently-used cache), `OrderedDict` may be a better fit than the standard `dict` type
- You shouldn't always assume that insertion ordering behaviour will be present when you're handling dictionaries
  - Python makes it easy for programmers to define their own custom container types that emulate the standard protocols matching `list`, `dict`, and other types
  - Python is not statically typed, so most code relies on duck typing
  - you may have code that assumes that the dictionary's iteration is in insertion order
    - the assumption will not be true if a dictionary that is ordered differently (e.g., sorted by keys) is used instead
- Mitigation:
  - write code that does not assume the dictionary has a specific iteration order
    - most conservative and robust solution
  - add explicit check to ensure the type of dictionary matches expectation, and raise an exception if not
    - `if not isinstance(some_dictionary, dict):`
    - likely to have better runtime performance than the more conservative approach
  - use type annotations to enforce that the dictionary is a `dict` instance
    - provides the best mix of static type safety and runtime performance

### Item 16: Prefer `get` Over `in` and `KeyError` to Handle Missing Dictionary Keys

- See [`handle_missing_dict_keys_test.py`](src/ch02/handle_missing_dict_keys_test.py)
- The contents of dictionaries are dynamic, and so it's entirely possible that when you try to access or delete a key, it won't already be present
- 4 common ways to detect and handle missing keys in dictionaries:
  - use an `if` statement with an `in` expression to check if the key is present
    - see `increment_if_in()`
  - rely on dictionaries raising `KeyError` when accessing a key that doesn't exist
    - see `increment_keyerror()`
  - use `dict`'s `get` method along with a default value
    - for a dictionary with simple value types, this is the shortest and clearest option
      - `count = counter_mapping.get(key, 0)`
      - see `increment_get_default()`
    - use assignment expression to create dictionary values that have a high cost or may raise exceptions
      - `if (names := bread_voters.get(key)) is None:`
      - see `test_get_complex_value()`
  - use `dict`'s `setdefault` method
    - if the key isn't present, `setdefault` assigns that key to the default value provided
      - returns the value for that key - either the originally present value or the newly inserted default value
      - note: when the key is missing, the default value is assigned directly into the dictionary instead of being copied
    - this is the shortest way to handle missing dictionary keys when the default values are cheap to construct, mutable, and there's no potential for raising exceptions.
    - `names = bread_voters.setdefault(key, [])`
    - see `test_setdefault()`
    - the method name is quite confusing
      - consider using `defaultdict` (Item 17) instead

### Item 17: Prefer `defaultdict` Over `setdefault` to Handle Missing Items in Internal State

- See [`defaultdict_for_internal_state_test.py`](src/ch02/defaultdict_for_internal_state_test.py)
- If a dictionary of arbitrary keys is passed to you, and you don't control its creation
  - prefer the `get` method to access its items
    - `if (cities := visits.get(country)) is None:`
    - see `access_get()`
  - it's worth considering using the `setdefault` method in situations where it leads to shorter code
    - `visits.setdefault(country, set()).add(city)`
    - see `access_setdefault()`
- Problems with `setdefault`:
  - method is confusingly named
  - not efficient - constructs a new object (in the above example, `set`) on every call regardless whether the key is already present in the dictionary
- If you're creating a dictionary to manage an arbitrary set of potential keys, then you should consider using a [`defaultdict`](https://docs.python.org/3/library/collections.html#defaultdict-objects) instance from the `collections` built-in module
  - automatically stores a default value when a key doesn't exist
  - uses a function that will return the default value to use each time a key is missing
  - see `test_default_dict()`

### Item 18: Know How to Construct Key-Dependent Default Values with `__missing__`

- See [`key_dependent_default_values_test.py`](src/ch02/key_dependent_default_values_test.py)
- There are times when neither `setdefault` nor `defaultdict` is the right fit to handle missing keys in a dictionary
  - the `setdefault` method of `dict` is a bad fit when creating the default value has high computational cost or may raise exceptions
  - the function passed to `defaultdict` must not require any arguments, which makes it impossible to have the default value depend on the key being accessed
- You can define your own `dict` subclass with a `__missing__` method in order to construct default values that must know which key was being accessed
  - the `__missing__` method is called only when the key is not present in the dictionary
  - see `test_missing()`

## Source

Slatkin, Brett. _Effective Python: 90 Specific Ways to Write Better Python_. USA: Addison-Wesley, 2020.
