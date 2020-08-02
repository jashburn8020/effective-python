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

## Source

Slatkin, Brett. _Effective Python: 90 Specific Ways to Write Better Python_. USA: Addison-Wesley, 2020.
