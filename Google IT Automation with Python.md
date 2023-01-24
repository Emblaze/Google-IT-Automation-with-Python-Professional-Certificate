# Google IT Automation with Python Professional Certificate

## 1. Crash Course on Python

### Python Resources

#### More About Python

##### Using Python on your own

The best way to learn any programming language is to practice it on your own as much as you can. If you have Python installed on your computer, you can execute the interpreter by running the python3 command (or just python on Windows), and you can close it by typing exit() or Ctrl-D.

If you don't already have Python installed on your machine, that's alright. We'll explain how to install it in an upcoming course.

##### Python practice resources

In the meantime, you can still practice by using one of the many online Python interpreters or codepads available online. There's not much difference between an interpreter and a codepad. An interpreter is more interactive than a codepad, but they both let you execute code and see the results.

Below, you'll find links to some of the most popular online interpreters and codepads. Give them a go to find your favorite.

[](https://www.python.org/shell/)

[](https://www.onlinegdb.com/online_python_interpreter)

[](https://repl.it/languages/python3)

[](https://www.tutorialspoint.com/execute_python3_online.php)

[](https://rextester.com/l/python3_online_compiler)

[](https://trinket.io/python3)

##### Additional Python resources

While this course will give you information about how Python works and how to write scripts in Python, you'll likely want to find out more about specific parts of the language. Here are some great ways to help you find additional info:

Read the [official Python documentation](https://docs.python.org/3/).

Search for answers or ask a question on [Stack Overflow](https://stackoverflow.com/).

Subscribe to the Python [tutor](https://mail.python.org/mailman/listinfo/tutor) mailing list, where you can ask questions and collaborate with other Python learners.

Subscribe to the [Python-announce](https://mail.python.org/mailman/listinfo/python-announce-list) mailing list to read about the latest updates in the language.

##### Python history and current status

Python was released almost 30 years ago and has a rich history. You can read more about it on the [History of Python](https://en.wikipedia.org/wiki/History_of_Python) Wikipedia page or in the section on the [history of the software](https://docs.python.org/3.0/license.html) from the official Python documentation.

Python has recently been called the fastest growing programming language. If you're interested in why this is and how it's measured, you can find out more in these articles:

[The Incredible Growth of Python](https://stackoverflow.blog/2017/09/06/incredible-growth-python/) (Stack Overflow)

[Why is Python Growing So Quickly - Future Trends](https://www.netguru.com/blog/why-python-is-growing-so-quickly-future-trends) (Netguru)

[By the numbers: Python community trends in 2017/2018](https://opensource.com/article/18/5/numbers-python-community-trends) (Opensource.com)

[Developer Survey Results 2018](https://insights.stackoverflow.com/survey/2018#technology) (Stack Overflow)

### First Programming Concepts Cheat Sheet

First Programming Concepts Cheat Sheet Functions and Keywords

Functions and keywords are the building blocks of a language's syntax.

Functions are pieces of code that perform a unit of work. In the examples we've seen so far, we've only encountered the print() function, which prints a message to the screen. We'll learn about a lot of other functions in later lessons but, if you're too curious to wait until then, you can discover all the functions available [here](https://docs.python.org/3/library/functions.html).

Keywords are reserved words that are used to construct instructions. We briefly encountered for and in in our first Python example, and we'll use a bunch of other keywords as we go through the course. For reference, these are all the reserved keywords:

|      |          |         |          |        |
------ | -------- | ------- | -------- | ------ |
False  | class    | finally | is       | return |
None   | continue | for     | lambda   | try    |
True   | def      | from    | nonlocal | while  |
and    | del      | global  | not      | with   |
as     | elif     | if      | or       | yield  |
assert | else     | import  | pass     | break  |
except | in       | raise   |          |        |

You don't need to learn this list; we'll dive into each keyword as we encounter them. In the meantime, you can see examples of keyword usage [here](https://www.programiz.com/python-programming/keyword-list).

#### Arithmetic operators

Python can operate with numbers using the usual mathematical operators, and some special operators, too. These are all of them (we'll explore the last two in later videos).

```python
a + b = Adds a and b

a - b = Subtracts b from a

a * b = Multiplies a and b

a / b = Divides a by b

a ** b = Elevates a to the power of b. For non integer values of b,\
   this becomes a root (i.e. a ** (1/2) is the square root of a)

a // b = The integer part of the integer division of a by b

a % b = The remainder part of the integer division of a by b
```

### Expressions & Variables

#### Data Types Recap

In Python, text in between quotes -- either single or double quotes -- is a string data type. An integer is a whole number, without a fraction, while a float is a real number that can contain a fractional part. For example, 1, 7, 342 are all integers, while 5.3, 3.14159 and 6.0 are all floats. When attempting to mix incompatible data types, you may encounter a **TypeError**. You can always check the data type of something using the **_type()_** function.

#### Implicit vs Explicit Conversion

Some data types can be mixed and matched due to implicit conversion. Implicit conversion is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so.

By contrast, explicit conversion is where we manually convert from one data type to another by calling the relevant function for the data type we want to convert to. We used this in our video example when we wanted to print a number alongside some text. Before we could do that, we needed to call the _str()_ function to convert the number into a string. Once the number was explicitly converted to a string, we could join it with the rest of our textual string and print the result.

### Functions

#### Defining Functions Recap

We looked at a few examples of built-in functions in Python, but being able to define your own functions is incredibly powerful. We start a function definition with the def keyword, followed by the name we want to give our function. After the name, we have the parameters, also called arguments, for the function enclosed in parentheses. A function can have no parameters, or it can have multiple parameters. Parameters allow us to call a function and pass it data, with the data being available inside the function as variables with the same name as the parameters. Lastly, we put a colon at the end of the line.

After the colon, the function body starts. It's important to note that in Python the function body is delimited by indentation. This means that all code indented to the right following a function definition is part of the function body. The first line that's no longer indented is the boundary of the function body. It's up to you how many spaces you use when indenting -- just make sure to be consistent. So if you choose to indent with four spaces, you need to use four spaces everywhere in your code.

#### Returning Values Using Functions

Sometimes we don't want a function to simply run and finish. We may want a function to manipulate data we passed it and then return the result to us. This is where the concept of return values comes in handy. We use the return keyword in a function, which tells the function to pass data back. When we call the function, we can store the returned value in a variable. Return values allow our functions to be more flexible and powerful, so they can be reused and called multiple times.

Functions can even return multiple values. Just don't forget to store all returned values in variables! You could also have a function return nothing, in which case the function simply exits

### Conditionals

#### Comparison Operators

In Python, we can use comparison operators to compare values. When a comparison is made, Python returns a boolean result, or simply a True or False.

To check if two values are the same, we can use the equality operator: **==**

To check if two values are not the same, we can use the not equals operator: **!=**

We can also check if values are greater than or lesser than each other using > and <. If you try to compare data types that aren't compatible, like checking if a string is greater than an integer, Python will throw a **TypeError**.

We can make very complex comparisons by joining statements together using logical operators with our comparison operators. These logical operators are **and**, **or**, and **not**.

- When using the **and** operator, _both sides of the statement being evaluated must be true for the whole statement to be true_.

- When using the **or** operator, _if either side of the comparison is true, then the whole statement is true_.

Lastly, the **not** operator simply inverts the value of the statement immediately following it. So _if a statement evaluates to True, and we put the not operator in front of it, it would become False_.

#### Branching with if Statements Recap

We can use the concept of **branching** to have our code alter its execution sequence depending on the values of variables. We can use an if statement to evaluate a comparison. We start with the if keyword, followed by our comparison. We end the line with a colon. The body of the if statement is then indented to the right. If the comparison is **_True_**, the code inside the if body is executed. If the comparison evaluates to **_False_**, then the code block is skipped and will not be run.

_The body of the if block will only execute when the condition evaluates to true; otherwise, it skipped._

#### else Statements and the Modulo Operator

We just covered the if statement, which executes code if an evaluation is true and skips the code if it's false. But what if we wanted the code to do something different if the evaluation is false? We can do this using the else statement. The else statement follows an if block, and is composed of the keyword else followed by a colon. The body of the else statement is indented to the right, and will be executed if the above if statement doesn't execute.

We also touched on the modulo operator, which is represented by the percent sign: %. This operator performs integer division, but only returns the remainder of this division operation. If we're dividing 5 by 2, the quotient is 2, and the remainder is 1\. Two 2s can go into 5, leaving 1 left over. So 5%2 would return 1\. Dividing 10 by 5 would give us a quotient of 2 with no remainder, since 5 can go into 10 twice with nothing left over. In this case, 10%2 would return 0, as there is no remainder.

#### More Complex Branching with elif Statements

Building off of the _if_ and _else_ blocks, which allow us to branch our code depending on the evaluation of one statement, the _elif_ statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an _elif_ statement starts with the _elif_ keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An _elif_ statement **must follow** an _if_ statement, and will only be evaluated if the _if_ statement was evaluated as false. You can include multiple _elif_ statements to build complex branching in your code to do all kinds of powerful things!

#### Conditionals Cheat Sheet

In earlier videos, we took a look at some of the built-in Python operators that allow us to compare values, and some logical operators we can use to combine values. We also learned how to use operators in if-else-elif blocks.

It's a lot to learn but, with practice, it gets easier to remember it all. In the meantime, this handy cheat sheet gives you all the information you need at a glance.

##### Comparison operators

```python
a == b: a is equal to b
a != b: a is different than b
a < b: a is smaller than b
a <= b: a is smaller or equal to b
a > b: a is bigger than b
a >= b: a is bigger or equal to b
```

##### Logical operators

```python
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True.\
 False if both are False.
not a: True if a is False, False if a is True.
```

##### Branching blocks

In Python, we branch our code using if, else and elif. This is the branching syntax:

```python
if condition1:
  if-block
elif condition2:
  elif-block
else:
  else-block
```

### Introduction to loops

#### Anatomy of a While Loop

A _while loop will continuously execute code depending on the value of a condition_. It begins with the keyword while, followed by a comparison to be evaluated, then a colon. On the next line is the code block to be executed, indented to the right. Similar to an if statement, the code in the body will only be executed if the comparison is evaluated to be true. What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.

#### Why Initializing Variables Matters

When we forget to initialize the variable two different things can happen. The first possible outcome and the easiest to catch is that Python might raise an error telling us that we're using a variable we haven't defined.

Now, there's a second issue we might face if we forget to initialize variables with the right value. We might have already used the variable in our program. In this case, if we reuse the variable without setting the correct value from the start, it will still have the value from before. This can lead to some pretty unexpected behavior.

**Whenever you're writing a loop check that you're initializing all the variables you want to use before you use them.**

##### Common Pitfalls With Variable Initialization

You'll want to watch out for a common mistake: forgetting to initialize variables. If you try to use a variable without first initializing it, you'll run into a **NameError**. This is the Python interpreter catching the mistake and telling you that you're using an undefined variable. The fix is pretty simple: initialize the variable by assigning the variable a value before you use it.

Another common mistake to watch out for that can be a little trickier to spot is forgetting to initialize variables with the correct value. If you use a variable earlier in your code and then reuse it later in a loop without first setting the value to something you want, your code may wind up doing something you didn't expect. Don't forget to initialize your variables before using them!

#### Infinite Loops and How to Break Them

Example of an infinite loop:

```python
while x % 2 == 0:
  x = x / 2
```

Fix:

```python
  while x != 0 and x % 2 == 0:
    x = x / 2
```

Another example:

```python
def print_range(start, end):
"""Loop through the numbers from start to end"""
n = start
while n <= end:
  print(n)
```

Fix:

```python
def print_range(start, end):
n = start
while n <= end:
  print(n)
  n += 1
```

##### Infinite loops and Code Blocks

Another easy mistake that can happen when using loops is introducing an infinite loop. An infinite loop means the code block in the loop will continue to execute and never stop. This can happen when the condition being evaluated in a while loop doesn't change. Pay close attention to your variables and what possible values they can take. Think about unexpected values, like zero.

### What is a for loop?

A loop iterates over a sequence of values.

- Use for loops when there's a sequence of elements that you want to iterate.

- Use while loops when you want to repeat an action until a condition changes.

And if whatever you're trying to do can be done with either for or while loops, just use whichever one's your favorite.

#### For Loops Recap

_For_ loops allow you to iterate over a sequence of values. Let's take the example from the beginning of the video:

```python
for x in range(5):
  print(x)
```

Similar to _if_ statements and _while_ loops, _for_ loops begin with the keyword **_for_** with a colon at the end of the line. Just like in function definitions, _while_ loops and _if_ statements, the body of the _for_ loop begins on the next line and is indented to the right. But what about the stuff in between the for keyword and the colon? In our example, we're using the _range()_ function to create a sequence of numbers that our _for_ loop can iterate over. In this case, our variable **x** points to the current element in the sequence as the _for_ loop iterates over the sequence of numbers. Keep in mind that in Python and many programming languages, a range of numbers will start at 0, and the list of numbers generated will be one less than the provided value. So _range(5)_ will generate a sequence of numbers from 0 to 4, for a total of 5 numbers.

Bringing this all together, the range(5) function will create a sequence of numbers from 0 to 4\. Our _for_ loop will iterate over this sequence of numbers, one at a time, making the numbers accessible via the variable **x** and the code within our loop body will execute for each iteration through the sequence. So for the first loop, **x** will contain 0, the next loop, 1, and so on until it reaches 4\. Once the end of the sequence comes up, the loop will exit and the code will continue.

The power of _for_ loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers. You can use _for_ loops to iterate over a list of strings, such as usernames or lines in a file.

Not sure whether to use a for loop or a _while_ loop? Remember that a _while_ loop is great for performing an action over and over until a condition has changed. A _for_ loop works well when you want to iterate over a sequence of elements.

#### More for loops examples

```python
def factorial(n):
  result = 1
  for i in ___:
      __
  return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
```

The **_range_** function can receive one, two or three parameters.

- If it receives one parameter, it will create a sequence one by one from zero until one less than the parameter received.

- If it receives two parameters, it will create a sequence one by one from the first parameter until one less than the second parameter.

- Finally, if it receives three parameters, it will create a sequence starting from the first number and moving towards the second number. But this time, the jumps between the numbers will be the size of the third number, and again, it will stop before the second number.

#### Nested for Loops

```python
"""Domino tiles examples"""
for left in range(0, 7):
  for right in range(left,7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print() #note the identation difference with the previous line ;-)

"""Output:
[0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6]
[1|1] [1|2] [1|3] [1|4] [1|5] [1|6]
[2|2] [2|3] [2|4] [2|5] [2|6]
[3|3] [3|4] [3|5] [3|6]
[4|4] [4|5] [4|6]
[5|5] [5|6]
[6|6]
"""
```

Another example:

```python
"""Local girl's basketball league"""
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team
      print(home_team + " vs " + away_team)

"""Output:
Dragons vs Wolves
Dragons vs Pandas
Dragons vs Unicorns
Wolves vs Dragons
Wolves vs Pandas
Wolves vs Unicorns
Pandas vs Dragons
Pandas vs Wolves
Pandas vs Unicorns
Unicorns vs Dragons
Unicorns vs Wolves
Unicorns vs Pandas
"""
```

#### Common Errors in for Loops

- Forgetting that the upper limit of a range() isn't included.

- Iterating over non-sequences. Integer numbers aren't iterable. Strings are iterable letter by letter, but that might not be what you want.

[Python wiki page on for loops](https://wiki.python.org/moin/ForLoop)

### Recursion (optional)

#### What is recursion?

**Recursion** is the repeated application of the same procedure to a smaller problem. Recursion lets us tackle complex problems by reducing the problem to a simpler one.

In programming, recursion is a way of doing a repetitve task by having function call itself. Notions of base case and recursive case.

Example: Recursive factorial function

```python
def factorial (n):
  if n < 2:
    return 1
  else:
    return n * factorial (n - 1)
```

Other example:

```python
"""The function sum_positive_numbers should return the sum of all\
 positive numbers between the number n received and 1.\
For example, when n is 3 it should return 1+2+3=6, and when\
 n is 5 it should return 1+2+3+4+5=15.\
Fill in the gaps to make this work:
"""

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
      return ___

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return ___ + sum_positive_numbers(___)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
```

And another:

```python
def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return __

  # Recursive case: keep dividing number by base.
  return is_power_of(__, ___)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
```

#### Recursion in Action in the IT Context

Think automations tasks around files and directories, groups (Active Directory/LDAP)...

#### Additional Recursion Sources

In the past videos, we visited the basic concepts of recursive functions.

A recursive function must include a recursive case and base case. The recursive case calls the function again, with a different value. The base case returns a value without calling the same function.

A recursive function will usually have this structure:

```python
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
```

For more information on recursion, check out these resources:

- [Wikipedia Recursion page](https://en.wikipedia.org/wiki/Recursion)

- See what happens when you [Search Google for Recursion](https://www.google.com/search?q=recursion)

### Strings, Lists and Dictionaries

**Strings in Python are immutable.**

#### Parts of a String: Indexing and Slicing

String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the character you want to access. It's important to **remember that Python starts indexes at 0**. So to access the first character in a string, you would use the index[0]. If you try to access an index that's larger than the length of your string, you'll get an **IndexError**. This is because you're trying to access something that doesn't exist! You can also access indexes from the end of the string going towards the start of the string by using negative values. The index[-1] would access the last character of the string, and the index[-2] would access the second-to-last character.

You can also access a portion of a string, called a slice or a substring. This allows you to access multiple characters of a string. You can do this by creating a range, using a colon as a separator between the start and end of the range, like [2:5].

This range is similar to the range() function we saw previously. It includes the first number, but goes to one less than the last number. For example:

```python
fruit = "Mangosteen"
fruit[1:4]
'ang'
```

The slice _includes_ the character at index 1, and _excludes_ the character at index 4\. You can also easily reference a substring at the start or end of the string by only specifying one end of the range. For example, only giving the end of the range:

```python
fruit[:5]
'Mango'
```

This gave us the characters from the start of the string through index 4, excluding index 5\. On the other hand this example gives is the characters including index 5, through the end of the string:

```python
fruit[5:]
'steen'
```

You might have noticed that if you put both of those results together, you get the original string back!

```python
fruit[:5] + fruit[5:]
'Mangosteen'
```

#### Creating new strings

```python
message = "A kong string with a silly typo"
message[2] = "l"
TypeError: 'str' object does not support item assignment
```

```python
new_message = message[:2] + "l" + message[3:]
```

```python
message = "This is a new message"
```

**Remember: Strings in Python are immutable**.

Notion of **method**: a _method_ is a function associated with a specific class.

```python
pets = "Cat & Dogs"
pets.index(&)
5
```

"Real world" application:

```python
def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@") + old_domain
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email
```

#### Basic String Methods

In Python, strings are immutable. This means that they can't be modified. So if we wanted to fix a typo in a string, we can't simply modify the wrong character. We would have to create a new string with the typo corrected. We can also assign a new value to the variable holding our string.

If we aren't sure what the index of our typo is, we can use the string method index to locate it and return the index. Let's imagine we have the string **"lions tigers and bears"** in the variable **animals**. We can locate the index that contains the letter g using _animals.index("**g**")_, which will return the index; in this case 8. We can also use substrings to locate the index where the substring begins. animals.index("bears") would return 17, since that's the start of the substring. If there's more than one match for a substring, the index method will return the first match. If we try to locate a substring that doesn't exist in the string, we'll receive a **ValueError** explaining that the substring was not found.

We can avoid a ValueError by first checking if the substring exists in the string. This can be done using the **_in_** keyword. We saw this keyword earlier when we covered _for_ loops. In this case, it's a conditional that will be either True or False. If the substring is found in the string, it will be True. If the substring is not found in the string, it will be False. Using our previous variable **animals**, we can do **"horses" in animals** to check if the substring "horses" is found in our variable. In this case, it would evaluate to False, since horses aren't included in our example string. If we did **"tigers" in animals**, we'd get True, since this substring is contained in our string.

#### Some More Strings Methods

|          |             |              |           |           |
|----------|-------------|--------------|-----------|-----------|
| .upper() | .lower()    | .strip()     | .lstrip() | .rstrip() |
| .count() | .endswith() | .isnumeric() | .join()   | .split()  |

#### Advanced String Methods

We've covered a bunch of String class methods already, so let's keep building on those and run down some more advanced methods.

The string method **lower** will return the string with all characters changed to lowercase. The inverse of this is the _**upper** method_, which will return the string all in uppercase. Just like with previous methods, we call these on a string using dot notation, like **"this is a string".upper()**. This would return the string **"THIS IS A STRING"**. This can be super handy when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases.

You can use the _**strip** method_ to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters. You can also use the methods lstrip and rstrip to remove whitespace only from the left or the right side of the string, respectively.

The _method **count**_ can be used to return the number of times a substring appears in a string. This can be handy for finding out how many characters appear in a string, or counting the number of times a certain word appears in a sentence or paragraph.

If you wanted to check if a string ends with a given substring, you can use the method endswith. This will return True if the substring is found at the end of the string, and False if not.

The **isnumeric** method can check if a string is composed of only numbers. If the string contains only numbers, this method will return True. We can use this to check if a string contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error. Useful! Try:

```python
int("12345") + int("54321")
```

We took a look at string concatenation using the plus sign, earlier. We can also use the _**join** method_ to concatenate strings. This method is called on a string that will be used to join a list of strings. The method takes a list of strings to be joined as a parameter, and returns a new string composed of each of the strings from our list joined using the initial string. For example,

```python
" ".join(["This","is","a","sentence"])
```

would return the string "This is a sentence".

The inverse of the join method is the _**split** method_. This allows us to split a string into a list of strings. By default, it splits by any whitespace characters. You can also split by any other characters by passing a parameter.

#### Formating Strings: the .format() method

Concatenation with _+_ and explicit conversion with _str()_ are helpful, but not always ideal.

##### String Formatting

You can use the _**format** method_ on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, **{}**, as a placeholder, to be replaced. Then call the format method on the string using _.format()_ and pass variables as parameters. The variables passed to the method will then be used to replace the curly bracket placeholders. This method automatically handles any conversion between data types for us.

If the curly brackets are empty, they'll be populated with the variables passed in the order in which they're passed. However, you can put certain expressions inside the curly brackets to do even more powerful string formatting operations. You can put the name of a variable into the curly brackets, then use the names in the parameters. This allows for more easily readable code, and for more flexibility with the order of variables.

You can also put a formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression **{:.2f}** means that you'd format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. You can also specify text alignment using the greater than operator: >. For example, the expression **{:>3.2f}** would align the text three spaces to the right, as well as specify a float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.

An example:

```python
name = "user"
number = len(name) * 3
print("Hello {}! Your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}".format(name=name,\
 number=number))
```

Another example, with a _formating expression_:

```python
price = 7.5
with_tax = price * 1.21
print("Base price: {:.2f} €. With VAT: {:.2f} €".format(price,\
 with_tax))
```

Yet another example:

```python
def to_celsius(t):
  return (t - 31)*5/9

for x in range(0, 101, 10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
```

#### String Formatting Recap

You can use the format method on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, {}, as a placeholder, to be replaced. Then call the format method on the string using .format() and pass variables as parameters. The variables passed to the method will then be used to replace the curly bracket placeholders. This method automatically handles any conversion between data types for us.

If the curly brackets are empty, they'll be populated with the variables passed in the order in which they're passed. However, you can put certain expressions inside the curly brackets to do even more powerful string formatting operations. You can put the name of a variable into the curly brackets, then use the names in the parameters. This allows for more easily readable code, and for more flexibility with the order of variables.

You can also put a formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression {:.2f} means that you'd format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.

Check out the official documentation for [all available String methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

### Lists

#### Lists Defined

Lists in Python are defined using square brackets, with the elements stored in the list separated by commas: **list = ["This", "is", "a", "list"]**. You can use the **len()** function to return the number of elements in a list: **len(list)** would return . You can also use the in keyword to check if a list contains a certain element. If the element is present, it will return a True boolean. If the element is not found in the list, it will return False. For example, **"This" in list** would return True in our example. Similar to strings, lists can also use indexing to access specific elements in a list based on their position. You can access the first element in a list by doing **list[0]**, which would allow you to access the string **"This"**.

```python
def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = ___
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return(___)
    return("")

print(get_word("This is a lesson about lists", 4)) # Should print:\
 lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing
```

In Python, lists and strings are quite similar. They're both examples of sequences of data. Sequences have similar properties, like (1) being able to iterate over them using **for loops**; (2) support indexing; (3) using the **len** function to find the length of the sequence; (4) using the plus operator + in order to concatenate; and (5) using the **in** keyword to check if the sequence contains a value. Understanding these concepts allows you to apply them to other sequence types as well.

#### Modifying the Contents of a List

Lists are sequences of elements of any type are mutable.

While lists and strings are both sequences, a big difference between them is that lists are mutable. This means that the contents of the list can be changed, unlike strings, which are immutable. You can add, remove, or modify elements in a list.

You can add elements to the end of a list using the _**append** method_. You call this method on a list using dot notation, and pass in the element to be added as a parameter. For example, _**list.append("New data")**_ would add the string "New data" to the end of the list called list.

If you want to add an element to a list in a specific position, you can use the _method **insert**_. The method takes two parameters: the first specifies the index in the list, and the second is the element to be added to the list. So _**list.insert(0, "New data")**_ would add the string "New data" to the front of the list. This wouldn't overwrite the existing element at the start of the list. It would just shift all the other elements by one. If you specify an index that's larger than the length of the list, the element will simply be added to the end of the list.

You can remove elements from the list using the _**remove** method_. This method takes an element as a parameter, and removes the first occurrence of the element. If the element isn't found in the list, you'll get a **ValueError** error explaining that the element was not found in the list.

You can also remove elements from a list using the **pop** method. This method differs from the remove method in that it takes an index as a parameter, and returns the element that was removed. This can be useful if you don't know what the value is, but you know where it's located. This can also be useful when you need to access the data and also want to remove it from the list.

Finally, you can change an element in a list by using indexing to overwrite the value stored at the specified index. For example, you can enter **list[0] = "Old data"** to overwrite the first element in a list with the new string "Old data".

#### Lists and Tuples

Tuples are sequences of elements of any type that are **immutable**.

```python
fullname = ("Grace", "M", "Hopper")
```

The position of the elements inside the tuple have meaning.

Tuples are used for lots of different things in Python. One common example is the return value of functions. When a function returns more than one value, it's actually returning a tuple.

This means that we can turn a tuple of three elements into three separate variables.

```python
def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print\
 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
```

#### Tuples

As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable. Lists are sequences of elements of any data type, and are mutable. The third sequence type is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. They're specified using parentheses instead of square brackets.

You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful when we need to ensure that an element is in a certain position and will not change. Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn't going to change. Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.

#### Iterating Over Lists Using Enumerate

When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element in the list, exposing the element to the for loop as a variable. But what if you want to access the elements in a list, along with the index of the element in question? You can do this using the _**enumerate()** function_. The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.

#### List Comprehensions

List comprehension let us create new lists bases on sequences or ranges.

You can create lists from sequences using a for loop, but there's a more streamlined way to do this: **list comprehension**. List comprehensions allow you to create a new list from a sequence or a range in a single line.

For example, **[ x*2 for x in range(1,11) ]** is a simple list comprehension. This would iterate over the range 1 to 10, and multiply each element in the range by 2. This would result in a list of the multiples of 2, from 2 to 20.

Compare:

```python
multiples = []
for x in range(1, 11):
  multiples.append(x * 7)

print(multiples)
```

with:

```python
multiples = [i*7 for i in range(1,11)]

print(multiples)
```

Another example, with a list:

```python
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lenghts = [len(language) for language in languages]
print(lenghts)
```

You can also use conditionals with list comprehensions to build even more complex and powerful statements. You can do this by appending an if statement to the end of the comprehension. For example, **[ x for x in range(1,101) if x % 10 == 0 ]** would generate a list containing all the integers divisible by 10 from 1 to 100\. The if statement we added here evaluates each value in the range from 1 to 100 to check if it's evenly divisible by 10\. If it is, it gets added to the list.

Exercise:

```python
def odd_numbers(n):
    return [x for x in ___ if ___]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
```

List comprehensions can be really powerful, but they can also be super complex, resulting in code that's hard to read. Be careful when using them, since it might make it more difficult for someone else looking at your code to easily understand what the code is doing.

### Dictionaries

#### Dictionaries Defined

Dictionaries are another data structure in Python. They're similar to a list in that they can be used to organize data into collections. However, data in a dictionary isn't accessed based on its position. Data in a dictionary is organized into pairs of keys and values. You use the key to access the corresponding value. Where a list index is always a number, a dictionary key can be a different data type, like a string, integer, float, or even tuples.

When creating a dictionary, you use curly brackets: {}. When storing values in a dictionary, the key is specified first, followed by the corresponding value, separated by a colon. For example, **animals = { "bears":10, "lions":1, "tigers":2 }** creates a dictionary with three key value pairs, stored in the variable animals. The key "bears" points to the integer value 10, while the key "lions" points to the integer value 1, and "tigers" points to the integer 2\. You can access the values by referencing the key, like this: **animals["bears"]**. This would return the integer 10, since that's the corresponding value for this key.

You can also check if a key is contained **in** a dictionary using the in keyword. Just like other uses of this keyword, it will return True if the key is found in the dictionary; otherwise it will return False.

Dictionaries are mutable, meaning they can be modified by adding, removing, and replacing elements in a dictionary, similar to lists. You can add a new key value pair to a dictionary by assigning a value to the key, like this: **animals["zebras"] = 2**. This creates the new key in the animal dictionary called zebras, and stores the value 2\. You can modify the value of an existing key by doing the same thing. So **animals["bears"]\ = 11** would change the value stored in the bears key from 10 to 11\. Lastly, you can remove elements from a dictionary by using the del keyword. By doing **del animals["lions"]** you would remove the key value pair from the animals dictionary.

#### Iterating over the Contents of a Dictionary

You can iterate over dictionaries using a for loop, just like with strings, lists, and tuples. This will iterate over the sequence of keys in the dictionary. If you want to access the corresponding values associated with the keys, you could use the keys as indexes. Or you can use the _**items** method_ on the dictionary, like _**dictionary.items()**_. This method returns a tuple for each element in the dictionary, where the first element in the tuple is the key and the second is the value.

If you only wanted to access the keys in a dictionary, you could use the _**keys()** method_ on the dictionary: _**dictionary.keys()**_. If you only wanted the values, you could use the _**values()** method_: _**dictionary.values()**_.

#### Dictionaries vs. Lists

You want to use dictionaries when you plan on searching for a specific element (faster than iteratiing over a list until said element is found, or not).

Another interesting difference is the types of values that we can store in lists and dictionaries. In lists, you can store any data type.

In dictionaries, we can store any data type for the values but the keys are restricted to specific types.

The reasoning behind which types are allowed can get complex. So as a rule of thumb, you can use any immutable data type; numbers, booleans, strings and tuples as dictionary keys. But you can't use lists or dictionaries for that.

On the flip side, like we said, the values associated with keys can be any type, including lists or even other dictionaries.

You can use them to represent more complex data structures like directory trees in the file system. There's a ton of different key value pairs that we need to work with in system administration.

### Object-Oriented Programming (optional)

A flexible, powerful paradigm where classes represent and define concepts, while objects are instances of classes.

#### Object-Oriented Programming Defined

In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of this class is called an object. Almost everything in Python is an object, including strings, lists, dictionaries, and numbers. When we create a list in Python, we're creating an object which is an instance of the list class, which represents the concept of a list.

Classes also have attributes and methods associated with them. **Attributes** are the characteristics of the class, while **methods** are functions that are part of the class.

#### Classes and Objects in Detail

We can use the **type()** function to figure out what class a variable or value belongs to. For example, **type(" ")** tells us that this is a string class. The only attribute in this case is the string value, but there are a bunch of methods associated with the class. We've seen the **upper()** method, which returns the string in all uppercase, as well as **isnumeric()** which returns a boolean telling us whether or not the string is a number. You can use the **dir()** function to print all the attributes and methods of an object. Each string is an instance of the string class, having the same methods of the parent class. Since the content of the string is different, the methods will return different values. You can also use the **help()** function on an object, which will return the documentation for the corresponding class. This will show all the methods for the class, along with parameters the methods receive, types of return values, and a description of the methods.

#### Defining New Classes

Defining Classes (Optional)

We can create and define our classes in Python similar to how we define functions. We start with the **class** keyword, followed by the name of our class and a colon. Python style guidelines recommend class names to start with a capital letter. After the class definition line is the class body, indented to the right. Inside the class body, we can define attributes for the class.

Let's take our Apple class example:

```python
class Apple:
  color = ""
  flavor = ""
```

We can create a new instance of our new class by assigning it to a variable. This is done by calling the class name as if it were a function. We can set the attributes of our class instance by accessing them using dot notation. Dot notation can be used to set or retrieve object attributes, as well as call methods associated with the class.

We created an Apple instance called jonagold, and set the color and flavor attributes for this Apple object. We can create another instance of an Apple and set different attributes to differentiate between two different varieties of apples.

```python
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
```

We now have another Apple object called golden that also has color and flavor attributes. But these attributes have different values.

#### Instances Methods

##### What Is a Method?

Calling methods on objects executes functions that operate on attributes of a specific instance of the class. This means that calling a method on a list, for example, only modifies that instance of a list, and not all lists globally. We can define methods within a class by creating functions inside the class definition. These instance methods can take a parameter called **self** which represents the instance the method is being executed on. This will allow you to access attributes of the instance using dot notation, like **self.name**, which will access the name attribute of that specific instance of the class object. When you have variables that contain different values for different instances, these are called instance variables.

Methods are functions that operate on the attributes of a specific instance of a class.

Variables that have different values for different instances of the same class are called **instance variables**.

```python
class Dog:
  years = 0
  def dog_years(self):
    years = self.years * 7
    return str(years)

fido=Dog()
fido.years=3
print(fido.dog_years())
```

#### Special Methods

Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a **constructor**. Below is an example of an Apple class with a constructor method defined.

```python
class Apple:
  def __init__(self, color, flavor):
    self.color = color
    self.flavor = flavor
```

When you call the name of a class, the constructor of that class is called. This constructor method is always named **\__init__**. You might remember that special methods start and end with two underscore characters. In our example above, the constructor method takes the self variable, which represents the instance, as well as color and flavor parameters. These parameters are then used by the constructor method to set the values for the current instance. So we can now create a new instance of the Apple class and set the color and flavor values all in go:

```python
jonagold = Apple("red", "sweet")

print(jonagold.color)
"""Outputs:
Red
"""
```

In addition to the **\__init__** constructor special method, there is also the **\__str__** special method. This method allows us to define how an instance of an object will be printed when it’s passed to the print() function. If an object doesn’t have this special method defined, it will wind up using the default representation, which will print the position of the object in memory. Not super useful. Here is our Apple class, with the **\__str__** method added:

```python
class Apple:
  def __init__(self, color, flavor):
    self.color = color
    self.flavor = flavor
  def __str__(self):
    return "This apple is {} and its flavor is {}".format\
    (self.color, self.flavor)
```

Now, when we pass an Apple object to the print function, we get a nice formatted string:

```python
jonagold = Apple("red", "sweet")

print(jonagold)
"""Outputs:
This apple is red and its flavor is sweet
"""
```

It's good practice to think about how your class might be used and to define a **\__str__** method when creating objects that you may want to print later.

#### Documenting with Docstrings

The Python **help** function can be super helpful for easily pulling up documentation for classes and methods. We can call the **help** function on one of our classes, which will return some basic info about the methods defined in our class:

```python
class Apple:
     def __init__(self, color, flavor):
         self.color = color
         self.flavor = flavor
     def __str__(self):
         return "This apple is {} and its flavor is\
          {}".format(self.color, self.flavor)

 help(Apple)
Help on class Apple in module __main__:
[...]
```

We can add documentation to our own classes, methods, and functions using **docstrings**. A docstring is a short text explanation of what something does. You can add a docstring to a method, function, or class by first defining it, then adding a description inside triple quotes. Let's take the example of this function:

```python
def to_seconds(hours, minutes, seconds):
    """Returns the amount of seconds in the given hours, minutes\
     and seconds."""
    return hours*3600+minutes*60+seconds
```

We have our function called _to_seconds_ on the first line, followed by the docstring which is indented to the right and wrapped in triple quotes. Last up is the function body. Now, when we call the help function on our _to_seconds_ function, we get a handy description of what the function does:

```python
help(to_seconds)
Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    Returns the amount of seconds in the given hours, minutes\
     and seconds.
```

**Docstrings** are super useful for documenting our custom classes, methods, and functions, but also when working with new libraries or functions. You'll be extremely grateful for docstrings when you have to work with code that someone else wrote!

```python
class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name))

help(Person.greeting)
```

### Code Reuse

#### Object Inheritance

Object Inheritance

In object-oriented programming, the concept of inheritance allows you to build relationships between objects, grouping together similar concepts and reducing code duplication. Let's create a custom Fruit class with color and flavor attributes:

```python
class Fruit:
  def __init__(self, color, flavor):
    self.color = color
    self.flavor = flavor

```

We defined a Fruit class with a constructor for color and flavor attributes. Next, we'll define an Apple class along with a new Grape class, both of which we want to inherit properties and behaviors from the Fruit class:

```python
class Apple(Fruit):
  pass

class Grape(Fruit):
  pass

In Python, we use parentheses in the class declaration to have the\
 class inherit from the Fruit class. So in this example, we’re\
  instructing our computer that both the Apple class and Grape class\
   inherit from the Fruit class. This means that they both have the\
    same constructor method which sets the color and flavor\
     attributes. We can now create instances of our Apple and Grape\
      classes:

```python
granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print(granny_smith.flavor)
tart
print(carnelian.color)
purple
```

Inheritance allows us to define attributes or methods that are shared by all types of fruit without having to define them in each fruit class individually. We can then also define specific attributes or methods that are only relevant for a specific type of fruit. Let's look at another example, this time with animals:

```python
class Animal:
  sound = ""
  def __init__(self, name):
    self.name = name
  def speak(self):
    print("{sound} I'm {name}! {sound}".format(name=self.name,\
     sound=self.sound))

class Piglet(Animal):
  sound = "Oink!"

class Cow(Animal):
  sound = "Moooo"
```

We defined a parent class, Animal, with two animal types inheriting from that class: Piglet and Cow. The parent Animal class has an attribute to store the sound the animal makes, and the constructor class takes the name that will be assigned to the instance when it's created. There is also the speak method, which will print the name of the animal along with the sound it makes. We defined the Piglet and Cow classes, which inherit from the Animal class, and we set the sound attributes for each animal type. Now, we can create instances of our Piglet and Cow classes and have them speak:

```python
hamlet = Piglet("Hamlet")
 hamlet.speak()
Oink! I'm Hamlet! Oink!

 class Cow(Animal):
     sound = "Moooo"

 milky = Cow("Milky White")
 milky.speak()
Moooo I'm Milky White! Moooo
```

We create instances of both the Piglet and Cow class, and set the names for our instances. Then we call the speak method of each instance, which results in the formatted string being printed; it includes the sound the animal type makes, along with the instance name we assigned.

```python
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
    print("This {} is made of {}".format(self.___,self.___))

class Shirt():
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
```

#### Object Composition (to review :wink:)

We talked about how inheritance creates an ancestry for our objects. To check for this ancestry, we can use the is a rule: _**isinstance()**_ and _**issubclass()**_

You can have a situation where two different classes are related, but there is no inheritance going on. This is referred to as **composition** -- where one class makes use of code contained in another class. For example, imagine we have a **Package** class which represents a software package. It contains attributes about the software package, like name, version, and size. We also have a **Repository** class which represents all the packages available for installation. While there’s no inheritance relationship between the two classes, they are related. The Repository class will contain a dictionary or list of Packages that are contained in the repository. Let's take a look at an example Repository class definition:

```python
class Repository:
      def __init__(self):
          self.packages = {}
      def add_package(self, package):
          self.packages[package.name] = package
      def total_size(self):
          result = 0
          for package in self.packages.values():
              result += package.size
          return result
```

In the constructor method, we initialize the packages dictionary, which will contain the package objects available in this repository instance. We initialize the dictionary in the constructor to ensure that every instance of the Repository class has its own dictionary.

We then define the add_package method, which takes a Package object as a parameter, and then adds it to our dictionary, using the package name attribute as the key.

Finally, we define a total_size method which computes the total size of all packages contained in our repository. This method iterates through the values in our repository dictionary and adds together the size attributes from each package object contained in the dictionary, returning the total at the end. In this example, we’re making use of Package attributes within our Repository class. We’re also calling the values() method on our packages dictionary instance. Composition allows us to use objects as attributes, as well as access all their attributes and methods.

Exercise: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts.

```python
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['___']:
      if item == material:
        count += Clothing.___['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock) #Should print 10
```

**Remember** this rule of thumb: **always initialize mutable attributes in the constructor**.

#### Augmenting Python with Modules

Python modules are separate files that contain classes, functions, and other data that allow us to import and make use of these methods and classes in our own code. Python comes with a lot of modules out of the box. These modules are referred to as the Python Standard Library. You can make use of these modules by using the import keyword, followed by the module name. For example, we'll **import** the **random module**, and then call the **randint** function within this module:

```python
import random
random.randint(1,10)
8
random.randint(1,10)
7
random.randint(1,10)
1
```

This function takes two integer parameters and returns a random integer between the values we pass it; in this case, 1 and 10. You might notice that calling functions in a module is very similar to calling methods in a class. We use dot notation here too, with a period between the module and function names.

Let's take a look at another module: datetime. This module is super helpful when working with dates and times.

```python
import datetime
now = datetime.datetime.now()
type(now)
<class 'datetime.datetime'>
print(now)
2019-04-24 16:54:55.155199
```

First, we import the module. Next, we call the **now()** method which belongs to the **datetime** class contained within the **datetime** module. This method generates an instance of the datetime class for the current date and time. This instance has some methods which we can call:

```python
print(now)
2019-04-24 16:54:55.155199
 now.year
2019
print(now + datetime.timedelta(days=28))
2019-05-22 16:54:55.155199
```

When we call the print function with an instance of the datetime class, we get the date and time printed in a specific format. This is because the datetime class has a **\__str__** method defined which generates the formatted string we see here. We can also directly call attributes and methods of the class, as with **now.year** which returns the year attribute of the instance.

Lastly, we can access other classes contained in the datetime module, like the **timedelta** class. In this example, we’re creating an instance of the timedelta class with the parameter of 28 days. We’re then adding this object to our instance of the datetime class from earlier and printing the result. This has the effect of adding 28 days to our original datetime object.

#### Supplemental Reading for Code Reuse

The official Python documentation lists all the modules included in the standard library. It even has a turtle in it...

[Pypi](https://pypi.org/) is the Python repository and index of an impressive number of modules developed by Python programmers around the world.

### Problem-solving Framework

When we take the structured approach to tackling problems there really isn't a challenge too complex to solve

#### Problem Statement #1

Before we jump into solving that problem, we need to know what information we'll use as input and what information we'll have as output. We can work this out by looking at the rest of the system where our script will live. Wwe need to know exact names of the attributes, otherwise, we won't be able to access them.

When working on a problem in general, and it's solution, it's easy to get caught up in the "making it look good" part. It's better to first focus on making the program work. You can always spend time making the report look nice later.

#### Research

#### Planning

#### Writing of the Script

## 2. Using Python to Interact with the Operating System

### Course Introduction

#### Finding out more information

Throughout this course, we teach you how to do a range of things with Python, Bash, and other tools. While we’ll provide a lot of information through videos and supplemental readings, sometimes, you may need to look things up on your own, now and throughout your career. Things change fast in IT, so it’s critical to do your own research to stay up-to-date on what’s new. We recommend you use your favorite search engine to find more information about concepts we cover in this course — it’s great practice for the real world!

On top of search results, here are some good programming resources available online:

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/): This book (available online and in print) includes a lot of practical programming exercises for beginners. You can refer to this content to read more about some of the things that we'll be discussing, and get inspired with more ideas of things that can be automated.

- [Hitchhiker’s Guide to Python](https://docs.python-guide.org/): This site (available online and in print) also covers a lot of what we can do with Python. Again, you can use this resource to learn more about the subjects we cover (and the ones we had to omit for time constraints).

- The [official language reference](https://docs.python.org/3/reference/index.html): Once you know what Python tool you'll be using to do a certain task, this technical reference of all Python language components can be a great [missing from website]

#### Getting Familiar with the Operating System

The operating system is a software that manages everything that goes on in the computer.

It reads, writes, and deletes files from the hard drive. It handles how the processes start, how they interact with each other, and how they eventually finish.
It manages how memory gets allocated different processes, how network packets are sent and received, and how each programming can access the different hardware components.

Since it's cross-platform, we can use the same Python code to get to our goal on any operating system, whether the goal is opening files, processing text, or managing running processes. This makes Python a great tool for IT specialists who needs to interact with different operating systems. You can apply the skills that you learned from one platform to all the others. So how cool is that?

#### Getting Your Computer Ready for Python

Some modules of interest from the Python Standard Library, to import in our scripts with the **import** keyword:

- requests and request.get() to work with web pages
- arrow and arrow.get() to work with dates
- the Image submodule from the Python Image Library: image.open(), image.size() and image.format()
- pandas for data science: pandas.DataFrame({...})

#### Pointers for Getting Your Environment Setup

##### Learning more about operating systems

We’ve talked briefly about what an operating system is and what we'll need to know about operating systems for this course. If you want to learn some additional operating system concepts, check out the videos on this subject in the [Technical Support Fundamentals course](https://www.coursera.org/lecture/technical-support-fundamentals/module-introduction-I3n9l). If you want to dive deeper onto how to manage Windows and Linux, check out the [Operating Systems and You: Becoming a Power User course](https://www.coursera.org/learn/os-power-user).

If you want to discover more about the history of Unix, you can read all the details on the [Unix Wikipedia page](https://en.wikipedia.org/wiki/History_of_Unix).

##### Installing Python and additional modules

If you don't have Python installed yet, we recommend that you visit the [official Python website](http://www.python.org/) and download the installer that corresponds to your operating system.

There’s a bunch of guides out there for installing Python and they all follow a similar process to the one we described in the videos. This [guide from Real Python](https://realpython.com/installing-python/) includes instructions on how to install python on a range of different operating systems and distributions.

Once you have Python installed on your operating system, it's a good idea to familiarize yourself with **pip and the associated tools**. You can find more info about these [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

##### Using package management systems

Package management systems help you better manage the software installed on your machine. These management systems vary a lot from operating system to operating system. So, you need to pick the one that works for the OS you’re using. Check out these guides for help with this:

- [Installing Python 3 on Windows 10 with Chocolatey](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

- [Installing Python 3 on MacOS with Homebrew](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/)

- [Package management basics on Linux](https://www.digitalocean.com/community/tutorials/package-management-basics-apt-yum-dnf-pkg)

##### Other information

- [Python in the Microsoft Store for Windows 10](https://devblogs.microsoft.com/python/python-in-the-windows-10-may-2019-update/)

#### Running Python Locally

##### Interpreted vs. Compiled Languages

##### How to Run a Python Script

Notion of "shebang": for Python scripts file, include #!/bin/env python3 in the first line and then make the file executable by using the command chmod +x
Finally, remember to prefix the file name with ./, to let the command line interpreter know that it should find the script in the current directory.

##### Setting up Your Environment

After you’ve installed Python and checked that it works, the next step to set up your developer environment is to choose your main code editor.

These are some of the common editors for Python, available for all platforms:

- [Eclipse](http://www.eclipse.org/)

- [PyCharm](https://www.jetbrains.com/pycharm/)

- [Sublime Text](http://www.sublimetext.com/)

- [VSCodium](https://vscodium.com/)

You can read more about these editors, and others, in these overview comparatives:

- [Python IDEs and Code Editors (Guide)](https://realpython.com/python-ides-code-editors-guide/#pycharm)

- [Best Python IDEs and Code Editors](https://www.softwaretestinghelp.com/python-ide-code-editors/)

- [Top 5 Python IDEs for Data Science](https://www.datacamp.com/community/tutorials/data-science-python-ide)

We encourage you to try out these editors and pick your favorite. Then, install it on your computer and experiment with writing and executing Python scripts locally.

### Automating Tasks Through Programming

#### Benefits of Automation

Scability: when more work is added to a system, the system can do whatever it needs to complete the work.

#### Pitfalls of Automation

##### Is it worth the time?

Is the time and effort it'll take to write the script worth the potential automation benefits?

A simple heuristic that can help us decide is to estimate how long it takes us to do a certain task. And then multiply that by how many times we perform that task in a given time window. If we estimate that it would take less time to automate the tasks than it would to do it manually, chances are, it's a good candidate for automation. So, the time to write the automation is less than time to perform the task multiply by the amount of times you do it, then automate the task.

```[time_to_automate < (time_to_perform * amount_of_times_done)```

![Is it worth the time?](Images/is_it_worth_the_time.png)
Source: [xkcd](https://xkcd.com/1205)

Usually, the decision of whether to automate or not isn't so straightforward. If a task is complex and performed in frequently, it may seem like automating is more trouble than it's worth.

But keep in mind that once a task is wrapped in automation, anyone can do it. It can be very useful to automate a complex error prone task. If it's critical that the tasks be done correctly, even if it's not executed that often.

There are no hard and fast rules on when to automate, but the cost time tradeoff can help guide your decisions.

A concept called the Pareto Principle can also be a useful guideline to help you decide which tasks to automate. When applied to automation in IT, the Pareto Principle states that 20% of the system administration tasks that you perform are responsible for 80% of your work. If you can identify and automate those 20% of your tasks, you could save yourself a whole lot of time.

#### Practical Automation Example

Computer "health": a few modules can help designing a script to check the "health" of a computer system (disk usage, cpu load, etc.): the _**shutil**_ and _**psutil**_ ones.

```python
import shutil
du = shutil.disk_usage("/") #directory to check
print(du)
du.free/du.total*100
```

```python
import psutil
psutil.cpu_percent(0.1) # interval of time to check the cpu load in\
 seconds, returns the average usage over said period
```

Now that we've done some research, let's write a first basic health checking script:

```python
#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free > 20

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return  usage < 70

"""Main body of script that checks if the 2 conditions described in\
 the 2 functions are false
"""
if not check_disk_usage("/") or not check_cpu_usage():
  print("Error!")
else:
  print("Everything is OK!")
```

Remember to mark the script as executable and to test it. We'll improve on it later.

### Reading and Writing Files

#### Programming with Files

Notions of directory/folder and file, filesystem hierarchy/tree. Notions of absolute vs relative PATH.

#### Reading Files

```python
file = open("spider.txt")
```

When we open a file, like we're doing in this example, the operating system checks
that we have permissions to access that file and then gives our code a **File descriptor**: this is a token generated by the OS that allows programs to do more operations with the file.

In Python, this file descriptor is stored as an attribute of the files object.
The file object gives us a bunch of methods that we can use to operate with the file.

Now, with this file object, we can read the contents of the file and print them to the screen.

##### The "Open-Use-Close" Approach

```python
>>>file = open("spider.txt")
>>>file.readline()
The itsy bitsy spider climbed up the waterspout.
>>>file.readline()
Down came the rain
>>>file.read()
and washed the spider out.
Out came the sun
and dried up all the rain
and the itty bitsy spider climbed up the spout again.
>>>file.close()
```

Handy if we intend to work with the file several times in our code. Remember to close the file! It's best pratice to:

- Allow other programs to work with the file otherwise locked
- Prevent the OS from running out of file descriptors (even if that number is generally high)
- Prevent race conditions. "Everybody looses in a race condition."

##### The "With" Approach

```python
with open("spider.txt") as file:
  file.readline()
```

Using this approach, Python automatically closes the opened file(s). Handy if we intend to work with the file only once in our code.

#### Iterating through Files

```python
with open("spider.txt") as file:
        for line in file:
            print(line.upper())

THE ITSY BITSY SPIDER CLIMBED UP THE WATERSPOUT.

DOWN CAME THE RAIN

AND WASHED THE SPIDER OUT.

OUT CAME THE SUN

AND DRIED UP ALL THE RAIN

AND THE ITTY BITSY SPIDER CLIMBED UP THE SPOUT AGAIN.
```

The text contains the new line invisible character \n. Notion of **escaping sequences**: \t for tabs.

To remove the new line the print() command actually outputs for each line:

```python
with open("spider.txt") as file:
        for line in file:
            print(line.strip().upper())
THE ITSY BITSY SPIDER CLIMBED UP THE WATERSPOUT.
DOWN CAME THE RAIN
AND WASHED THE SPIDER OUT.
OUT CAME THE SUN
AND DRIED UP ALL THE RAIN
AND THE ITTY BITSY SPIDER CLIMBED UP THE SPOUT AGAIN.
```

The _**readlines()**_ method (≠ .readline())

```python
file = open("spider.txt")
lines = file.readlines()
file.close() # Even though the file object is now closed, the lines\
 variable has the list of lines in the file, so we can operate on it.
```

A quick word of **caution**, methods like _**read**_ or _**readlines**_ that read the whole file at once are useful, but we should be careful when reading the entire contents of a file into a variable of our programs.

If the file is super large, it can take a lot of our computer's memory to hold it,
which can lead to poor performance.

If a file is just a few kilobytes like in our example here, it's fine to read it and process it completely in memory.

But for large files, like the big log file of hundreds and hundreds of megabytes of data, it's more efficient to process it line by line.

#### Writing Files

```python
with open("novel.txt", "w") as file:
  file.write("It was a dark and stormy night")

30
```

##### Notion of file modes (see Cheat-Sheet below)

| Mode | Description                                                                     |
|------|---------------------------------------------------------------------------------|
| r    | read-only (default, not mandatory)                                              |
| w    | write-only (overwrites existing content, creates the file if it doesn't exists) |
| a    | Append at the end of the file                                                   |
| r+   | Read-Write                                                                      |

Another word of **caution**: If you open a file for **writing and the file already exists, the old contents will be deleted as soon as the file is opened**.

Remember to double check that you're opening the right file using the right mode.

#### Reading and Writing Files Cheat-Sheet

Check out the following link for more information:

[https://docs.python.org/3/library/functions.html#open](https://docs.python.org/3/library/functions.html#open)

### Managing Files and Directories

#### Working with Files

Let's explore some of the many things that we can do with files in Python with the _**os**_ module.

**Caution**: Paths can be different across different operating systems. So whenever we're using an absolute path in our code, we need to make sure we can provide alternatives for the platforms we want to support.

The OS module lets us do pretty much all the same tasks that we can normally
do when working with files from the command line. We can change the file permissions and delete or rename files through our code. This means you can write scripts to do these operations for you automatically.

```python
import os
os.remove("novel.txt") # To delete a file

os.rename("old_file_name", "new_file_name") # To rename a file

os.path.exists("some_file_name") # Returns either True or False,\
 depending on the presence of the file
```

#### More File Information

```python
os.path.getsize("spider.txt") # Returns the file size in bytes

os.path.getmtime("spider.txt") # Returns the last modification time\
 and date of the file
```

Notion of **Timestamp**: a Unix timestamp for example represents the number of seconds since January 1st, 1970.

```python
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
```

```python
os.path.abspath("spider.txt")
`/Volumes/GoogleDrive/Mon Drive/Documents/Cours/Google IT Automation\
 with Python Professional Certificate/spider.txt'
```

#### Directories

```python
print(os.getcwd()) # Prints the current working directory

os.mkdir("New folder") # To create a new folder, aptly named\
 New folder
os.chdir("New folder") # To enter this newly created folder
print(os.getcwd()) # Outputs [...]/New folder

os.mkdir("Newer folder")
os.rmdir("Newer folder") # Will only delete the folder if it's empty
```

The **rmdir** function will only work if the directory is empty. If we try to remove a directory that has files in it, we get an error. We need to first delete all the files and sub-directories in that directory before we can actually remove it but how can we find out what contents are in that directory?

There are a few techniques that we can use to do this. The **os.listdir** function returns a list of all the files and sub-directories in a given directory.
Let's see how this looks for our website directory.

```python
import os
os.listdir("website")
['images', 'index.html', 'favicon.ico']
```

So we've got a list of strings. Since they're just strings, we don't know if they're directories or files. To find out what they are, we can use functions like
**os.path.isdir** but before we look at how that works. See how the list contains just file names. If we want to know whether one of these files is a directory, we need to use **os.path.join** to create the full path. Let's see all of this in action now.

```python
dir = "website"

for name in os.listdir(dir):
     fullname = os.path.join(dir, name)
     if os.path.isdir(fullname):
         print("{} is a directory".format(fullname))
     else:
         print("{} is a file".format(fullname))

website/images is a directory
website/index.html is a file
website/favicon.ico is a file
```

What's up with that join function? It seems to just add a slash between two strings. Well, the join function let's us be independent from the operating system again.

- In **Linux and MacOS**, the portions of a file are split using a **forward slash**.

- On **Windows**, they're split using a **backslash**.

By using the os.path.join function instead of explicitly adding a slash, we can make sure that our scripts -
work with all operating systems.

#### Files and Directories Cheat-Sheet

Check out the following links for more information:

- [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

- [os.path — Common pathname manipulations](https://docs.python.org/3/library/os.path.html)

- [Unix time Wikipedia page](https://en.wikipedia.org/wiki/Unix_time)

### Reading and Writing CSV Files

#### What is a CSV file?

Notion of parsing a file: Analyzing a file's content to correctly structure the data.

CSV stands for Comma Separated Values. It's one of the many file formats used to structure data, like HTML or JSON.

A lot of programs are capable of exporting data as CSV files, such as spreadsheet applications like Microsoft Excel or Google Sheets. It can actually be helpful to think of a CSV file like it's a spreadsheet, where each line corresponds to a row and each comma separated field corresponds to a column.

#### Reading CSV Files

Python standard library includes a module which lets us read, create and manipulate CSV files: the **csv** module.

Before we can parse a CSV file, we need to open the file the same way as before. We can then parse this file using the CSV module.

```python
import csv
f = open("csv_file.csv")
csv_f = csv.reader(f) # We now have an instance of the CSV reader\
 class
for row in csv_f:
  name, twitter_handle, nickname = row # See notion of unpacking
  print("Name: {}, Twitter handle: {}, Nickname: {}.".format(name,\
   twitter_handle, nickname))
f.close() # Remember to close the file when using the "Open-Use-\
Approach"
```

**Notion of unpacking**: the row variable hold each row in the CSV file.
This variable is a list with each field in the CSV corresponding to one
element in the list. We know from the before that the first field is a name, the second one, the Twitter handle, and the third, the nickname. So we can **unpack** the values so that we can use variables to refer to them. **Remember** that for this to work we need to have the exact same amount of variables on the left side of the equal sign as the length of the sequence on the right side.

We could have used row[0] to access the name of the employee. This is valid but it can be hard to follow when reading a lot of code. Unpacking the list into name variables makes the code easier to understand later on.

#### Generating CSV

we can use the writer function to generate contents to a file. This can be really helpful if you process some data in your script and you must store it in a file.
Maybe you want to import it into a spreadsheet or use it later on in your script.
We'll start by storing the data that we want to write into a list.

There are two functions that we can use: _**writerow**_, which we'll write one row at a time; and _**writerows**_, which we'll write all of them together. In this case, we already have all the data that we want to write. So we'll call writerows.

```python
import csv
hosts = [["MacBook-Air.local", "192.168.1.43"], ["fedora.local",\
 "192.168.1.73"], ["fedorapi.local", "192.168.1.80"]]
with open("hosts.csv", "w") as hosts_csv:
  writer = csv.writer(hosts_csv) # the writer variable is now an\
   instance of the csv writer class
  writer.writerows(hosts)
```

#### Reading and Writing CSV Files with Dictionaries

We saw how we can read and write CSV files, and we use list as datatype on the Python side. This works when we know what the fields are going to be, but it can be pretty cumbersome when we have a lot of columns, and we need to remember which is which. Imagine if your lists of employees not only had name, phone number and role but also start date, username, office location, department, preferred pronouns and so on. It would soon get hard to keep track of which column corresponds to which position in the row. For cases like this, it's common for CSVs to include the names of the columns as a first line in the file.

```python
import csv
with open("software.csv") as software:
  reader = csv.DictReader(software)
  for row in reader:
    print(("{} has {} users.").format(row["name", row["users"]]))
```

```python
users = [{"name": "Sol Mansi", "username": "solm", "department":\
 "IT\  Infrastructure"}, {"name": "Lio Nelson", "username": "lion",\
 "department": "User Experience Research"}, {"name": "Charlie Grey",\
   "username": "greyc", "department": "Development"}]
keys = ["name", "username", "departement"]
with open('by_department.csv', 'w') as by_department:
  writer = csv.DictWriter(by_department, fieldnames=keys)
  writer.writeheader()
  writer.writerows(users)
```

_**DictReader()**_ allows us to convert the data in a CSV file into a standard dictionary. _**DictWriter()**_ allows us to write data from a dictionary into a CSV file. The fieldnames parameter of DictWriter() requires a list of keys.

#### CSV Files Cheat Sheet

Check out the following links for more information:

- [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

- [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)

## Regular Expressions

### Introduction to Regular Expressions

#### What are regular expressions?

Regular expressions let you answer the questions like "what are all the four-letter words in a file?", or "how many different error types are there in this error log?".

**Regular expressions** allow us to search a text for strings matching a specific pattern.

#### Why use regular expressions?

At this point, you might be wondering why do I need more processing power than just looking for strings in a text which I already know how to do in Python? The answer lies in the power and flexibility of regular expressions.

```python
import re
log = "July 31 07:51:48 mycomputer bad_process [54321]:\
 ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
```

#### Basic Matching with grep

In our last example, we used a pretty complex regular expression from a Python program to look for a process ID. This is just one example of something we might want to do when processing texts from our Python scripts. We can also use regular expressions with a bunch of command line tools. **Grep** is an especially easy to use yet extremely powerful tool for applying regexes. It's a great way to easily try out some expressions and get familiar with them. So let's look at some basic matching we can do with grep.

```bash
grep thon /usr/share/dict/words
```

When we call grep with thon as a pattern to match on and we pass our list of words as a file, we see that it matches with a bunch of different words.

It's worth calling out that the string we're passing in grep is case sensitive. So it needs to be matched exactly. If we use uppercase letters, they'll only be matched by uppercase letters. If we wanted to match a string regardless of case, we will have to pass the -i parameter to the grep command, like this:

```bash
grep -i python /usr/share/dict/words
```

We now know that any basic string is already a regular expression which will match a line that contains that string. To get the most out of regular expressions, we need to learn more of their syntax, which can be as complicated as it is powerful. In particular, we have to know the **reserved characters** that give extra meaning to the patterns that we create. It's these characters that allow us to do more advanced matching than just checking for a literal string. For example, a dot matches any character. This means that if we include a dot in our expression, that dot is a wildcard that can be replaced by any other character in the results:

```bash
grep l.rts /usr/share/dict/words
```

##### Some RegEx Reserved Characters

| Reserved Character   | Meaning                                       |
|----------------------|-----------------------------------------------|
| .                    | "wildcard", replaces any character            |
| ^ "anchor character" | Search for specified pattern at the beginning |
| $ "anchor character" | Search for specified pattern at the end       |

```bash
grep ^fruit /usr/share/dict/words

grep cat$ /usr/share/dict/words
```

### Basic Regular Expressions

#### Simple Matching in Python

As we called it out before, we use the **re** module to apply regular expressions in Python. This module includes a bunch of different functions that can help manipulate strings. Let's see how we can use this module for some basic matching.

It's a good idea/practive to always use **rawstrings** for regular expressions in Python.

```python
import re
result = re.search(r"aza", "plaza")
print(result)
"""Outputs: <re.Match object; span=(2, 5), match='aza'>"""
result = re.search(r"aza", "bazaar")
print(result)
"""Outputs: <re.Match object; span=(1, 4), match='aza'>"""
result = re.search(r"aza", "maze")
print(result)
"""Outputs: None"""
```

When we're applying regular expressions, we now know that if the search function returns None, it means it didn't find a match. Let's practice the special characters that we've seen up until now with a few examples.

```python
result = re.search(r"^x", "xenon")
print(result)
"""Outputs: <re.Match object; span=(0, 1), match='x'>"""
```

What happens when we use a dot?

```python
print(re.search(r"p.ng", "penguin"))
<re.Match object; span=(0, 4), match='peng'>

print(re.search(r"p.ng", "clapping"))
<re.Match object; span=(4, 8), match='ping'>

print(re.search(r"p.ng", "sponge"))
<re.Match object; span=(1, 5), match='pong'>
```

#### Wildcards and Character Classes

. is the ultimate wildcard character, as it can replace any charater. What if we need to be stricter? Enter character classes.
Character classes are encapsulated between square brackets.

```python
import re
print(re.search(r"[Pp]ython", "Python"))
<re.Match object; span=(0, 6), match='Python'>
```

Notion of (regex) range: [a-z], [A-Z], [0-9]...

```python
print(re.search(r"[a-z]way", "The end of the highway"))
<re.Match object; span=(18, 22), match='hway'>
print(re.search(r"[a-z]way", "What a way to go!"))
None
```

We can combine as many ranges and symbols as we want, like this:

```python
print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
<re.Match object; span=(0, 6), match='cloudy'>
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
<re.Match object; span=(0, 6), match='cloud9'>
```

We can match anything that's defined between the square brackets, which is useful. Sometimes we may want to match any characters that aren't in a group.
To do that, we use a circumflex inside the square brackets. For example, let's create a search pattern that looks for any characters that's not a letter:

```python
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))\

<re.Match object; span=(4, 5), match=' '> # the span attribute \
returns the position of the first space encountered
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
<re.Match object; span=(30, 31), match='.'>
```

If we want to match either one expression or another, we can use the pipe symbol to do that. This lets us list alternative options that can get matched. For example, we could have an expression that matches either the word cat or the word dog, like this:

```python
print(re.search(r"cat|dog", "I like cats."))
<re.Match object; span=(7, 10), match='cat'>
print(re.search(r"cat|dog", "I like dogs."))
<re.Match object; span=(7, 10), match='dogs'>
print(re.search(r"cat|dog", "I like dogs and cats."))
<re.Match object; span=(7, 10), match='dogs'>\
 # search only returns the first occurence
```

If we want to get all possible matches, we can do that using the **findall** function, which is also provided by the **re** module, like this:

```python
print(re.findall(r"cat|dog", "I like dogs and cats."))
['dog', 'cat']
```

#### Repetition Qualifiers

It's quite common to see expressions that include a dot followed by a star.
This means that it matches any character repeated as many times as possible including zero.

Notion of **repeated matches**: .* and ?

```python
print(re.search(r"Py.*n", "Pygmalion"))
<re.Match object; span=(0, 9), match='Pygmalion'>
print(re.search(r"Py.*n", "Python programming"))
<re.Match object; span=(0, 17), match='Python programmin'> # See note below
print(re.search(r"Py[a-z]*n", "Python programming"))
<re.Match object; span=(0, 6), match='Python'>
```

Remember, the Star takes as many characters as possible. In programming terms, we
say that this behavior is _**greedy**_. It's possible to modify the repetition qualifiers to make them less greedy.

```python
import re
def repeating_letter_a(text):
  """The repeating_letter_a function checks if the text passed\
   includes the letter "a" (lowercase or uppercase) at least twice"""
  result = re.search(r"___", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
```

As we called out earlier, implementations of regular expressions aren't always the same. Repetition qualifiers are one way they differ. Some implementations like the one used by grep only include the store qualifier that we just discussed. You can do a lot with just a star qualifier. So that's usually good enough. Other implementations like the one used by Python or by the Egrep command include two additional repetition qualifiers plus and question mark, that can help us construct more complex expressions.

The + character matches one or more occurrences of the character that comes before it.

```python
print(re.search(r"o+l+", "goldfish"))
<re.Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", "woolly"))
<re.Match object; span=(1, 5), match='ooll'>
print(re.search(r"o+l+", "boil"))
None # While there are both an o and a l, they're separated by a character.
```

In this case, there was one occurrence of each. In the match pattern shows us the shortest possible matching string.

The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before it. Let's see how this works:

```python
print(re.search(r"p?each", "To each to their own")) # the ? renders the p optional
<re.Match object; span=(3, 7), match='each'>
print(re.search(r"p?each", "I like peaches!"))
<re.Match object; span=(7, 12), match='peach'>
```

#### Escaping Characters

We can use a **backslash** in this way to escape any special characters, including the ones that we haven't even talked about yet.

Something to watch out for: it can get really confusing with backslashes since they're also used to define some special string characters.

```python
print(re.search(r".com", "Welcome!"))
<re.Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com", "Welcome!"))
None
print(re.search(r".com", "mydomain.com"))
<re.Match object; span=(8, 12), match='.com'>
```

We've called out, for example, that **\n** is a sequence using Python to indicate a new line, and **\t** does the same for tabs. **When we see a pattern that includes a backslash, it could be escaping a special regex character or a special string character**.

Using raw strings, like we've been doing, helps avoid some of these possible confusion because the special characters won't be interpreted when generating the string. They will only be interpreted when parsing the regular expression.

On top of this, Python also uses the backslash for a few special sequences that we can use to represent predefined sets of characters. For example, **\w** matches any alphanumeric character including letters, numbers, and underscores.

```python
print(re.search(r"\w*", "This is an example."))
<re.Match object; span=(0, 4), match='This'>
print(re.search(r"\w*", "And_this_is_another!"))
<re.Match object; span=(0, 19), match='And_this_is_another'>
```

There's also **\d** for matching digits, **\s** for matching whitespace characters like space, tab or new line, **\b** for word boundaries and a few others.

```python
import re
def check_character_groups(text):
  """Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters."""
  result = re.search(r"____", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs."))
```

#### Regular Expressions in Action

We've now looked into a bunch of syntax for using regular expressions in Python. Armed with all this knowledge, we can start combining these special characters to create patterns to match the text that we want. For example, say you had a list of all the countries in the world and you want to check which of those names start and end in a. What will the pattern look like? Maybe something like this, A.*a. Let's try that one out:

```python
print(re.search(r"A.*a", "Argentina"))
<re.Match object; span=(0, 9), match='Argentina'>
print(re.search(r"A.*a", "Azerbaijan"))
<re.Match object; span=(0, 9), match='Azerbaija'> # Not quite
print(re.search(r"^A.*a$", "Azerbaijan"))
None
print(re.search(r"^A.*a$", "Australia"))
<re.Match object; span=(0, 9), match='Australia'>
```

Using regular expressions, we can also construct a pattern that would validate if the string is a valid variable name in Python. Do you remember what the rules were? It can contain any number of letters numbers or underscores, but it can't start with a number.

```python
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "this_is_a_valid_variable_name"))
<re.Match object; span=(0, 29), match='this_is_a_valid_variable_name'>
print(re.search(pattern, "this isn't a valid variable name"))
None
print(re.search(pattern, "my_variable1"))
<re.Match object; span=(0, 12), match='my_variable1'>
print(re.search(pattern, "2my_variable_name"))
None
```

Exercise:

```python
import re
def check_sentence(text):
  """Check if the text passed looks like a standard\
   sentence, meaning that it starts with an uppercase\
    letter, followed by at least some lowercase\
     letters or a space, and ends with a period,\
      question mark, or exclamation point
  """
  result = re.search(r"^[A-Z]+[a-z0-9]+[.?!$]", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
```

#### Regular Expressions Cheat-Sheet

List of special characters/metacharacters:

```python
. ^ $ * + ? { } [ ] \ | ( )
```

Check out the following links for more information:

- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)

- [re — Regular expression operations](https://docs.python.org/3/library/re.html)

- [Greedy versus Non-Greedy](https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy)

Shout out to [regex101.com](http://regex101.com/), which will explain each stage of a regex.

### Advanced Regular Expressions

#### Capturing Groups

Up to now, we've used the search function to check if a string matched a certain pattern. But the only thing we've done with the result is print. Printing is useful when we want to see if a string matches a certain pattern.

But most of the time, we want to take the information that we matched and use it for something else. For example, we may want to extract the hostname or a process ID from a log line and use that value for another operation. For that we need to use a concept of regular expressions called **capturing groups**.

**Capturing groups are portions of the pattern that are enclosed in parentheses**.

Example:

```python
import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
```

The match object has more attributes and methods than the ones shown by print, so we are going to start using them now. Let's look at the output of the groups method:

```python
print(results.groups())$
('Lovelace', 'Ada')
```

Because we defined two separate groups, the group method returns a tuple of two elements. We can also use indexing to access these groups. The first element contains the text matched by the entire regular expression. Each successive element contains the data that was matched by every subsequent match group. So let's look at the element at index 0.

```python
print(result[0])
'Lovelace, Ada'
print(result[1])
'Lovelace'
print(result[2])
'Ada'
print("{} {}".format(result[2], result[1]))
```

Nice!

```python
import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name = rearrange_name("Ritchie, Dennis")
print(name)
name = rearrange_name("Thompson, Ken")
print(name)
```

**Exercise**: Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames (Tip: keep 2 capturing groups,   allow for the second to optionally contain a space, then a group of characters):

```python
import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name) # "^(\w*), (\w*\ ?\w*.?)$" worked
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)
name=rearrange_name("Hopper, Grace M.")
print(name)
```

Note from the course: _Oops!  We made a small error.  Un-escaped, the dot in this expression will match any character. In this case it makes the code work, but it is incorrect! Since we wanted to match the dot character specifically, we should have escaped the dot in the regular expression. The correct regular expression should be: r"^([\w \.-]*), ([\w \.-]\*)$"_

#### More on Repetition Qualifiers

Up to now, we've used the Star, Plus and question mark repetition qualifiers. What if we wanted a pattern that repeats a specific number of times? This could happen if we're processing a line that we know has some specific data in a column, or we know that we want a string of a specific length. In cases like those, we would manually write the same pattern as many times as we need it. But it would be hard to read and hard to maintain. And that's why Python also offers numeric repetition qualifiers. These are written between curly brackets and can be one or two numbers specifying a range.

For example, to match any string of **exactly** five letters, we can use an expression like this one:

```python
import re
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
<re.Match object; span=(2, 7), match='ghost'>
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
<re.Match object; span=(2, 7), match='scary'> # only the first\
 occurence is returned
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
['scary', 'ghost', 'appea']
```

Now we have an extra match for the word that's actually longer. What if we wanted to match all the words that are exactly five letters long? We can do that using **\b**, which matches word limits at the beginning and end of the pattern, to indicate that we want full words, like this:

```python
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
['scary', 'ghost']
```

We said that we can also have two numbers in the range. For example, if we wanted to match a range of five to ten letters or numbers, we could use an expression like this one.

```python
print(re.findall(r"\w{5,10}", "I really like strawberries"))
['really', 'strawberri']
```

These ranges can also be open ended. A number followed by a comma means at least that many repetitions with no upper boundary limited only by the maximum repetitions in the source text.

```python
print(re.findall(r"\w{5,}", "I really like strawberries"))
['really', 'strawberries']
```

Now, for our final example, a comma followed by a number means from zero up to that amount of repetitions. Let's check that one out:

```python
print(re.search(r"s\w{,20}", "I really like strawberries"))
<re.Match object; span=(14, 26), match='strawberries'>
```

Exercise:

```python
import re
def long_words(text):
  pattern = ___
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning."))\
 # ['morning']
print(long_words("I also have a taste for hot chocolate in the\
 afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []
```

#### Extracting a PID Using regexes in Python

Remember the example from the beginning of our discussion of regular expressions? It was way back in the first video of this module when we were looking at the log lines and extracting process IDs. Well, we now have enough info to fully understand it. Let's walk through it step-by-step:

```python
import re
log = "July 31 07:51:48 mycomputer bad_process [54321]:\
 ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
```

Let's try our expression on a different string and check that it really works,
no matter what the rest of the text is:

```python
result = re.search(regex, "A completely different string that also\
 has numbers [271274]")
print(result[1])
271274
```

But what if our string didn't actually have a block of numbers between the square brackets?

```python
result = re.search(regex, "99 elephants in a [cage]")
print(result[1])
TypeError: 'NoneType' object is not subscriptable
```

We tried to access the index 1 of a variable that was none. As Python tells us, this isn't something that we can do. So what should we do instead? We should have a function that extracts the process ID or PID when possible, and does something else if not. It's something like this:

```python
def extract_pid(log_line):
  regex = r"\[(\d+)\]"
  result = re.search(regex, log_line)
  if result is None: # See note
    return ""
  return result[1]

print(extract_pid("July 31 07:51:48 mycomputer bad_process [54321]\
  : ERROR Performing package upgrade"))
54321
print(extract_pid("99 elephants in a [cage]"))

```

**Note**: What we choose to do depends on what we want the rest of the code to do.

**Exercise**: Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.

```python
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\b[A-Z]*\b)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]:\
 ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no/
uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]:\
 RUNNING Performing backup")) # 67890 (RUNNING)
```

#### Splitting and Replacing

Up to now we've been using two functions from the **re** module: **search()** and **findall()**. There are actually a few more functions that can be really handy depending on what we're trying to do.

One of these functions is called split. It works similarly to the split function that we used before with strings. But instead of taking a string as a separator, you can take any regular expression as a separator. For example we may want to split a piece of text into separate sentences. To do that we need to check not only for the dots but also for question marks or exclamation marks since they're also valid sentence endings. It's something like this:

```python
re.split(r"[.!?]", "A sentence. Another one? And the last one!")
['A sentence', ' Another one', ' And the last one', '']
```

Check out how we are not escaping the characters that we wrote inside the square brackets. That's because anything that's inside the square brackets is taking for the literal character and not for its special meaning. Also see how the notation marks aren't present in the resulting list.

If we want our split list to include the elements that we're using to split the values we can use capturing parentheses like this:

```python
re.split(r"([.!?])", "A sentence. Another one? And the last one!")
['A sentence', '.', ' Another one', '?', ' And the last one', '!', '']
```

Another interesting function provided by the RE module is called sub. It's used for creating new strings by substituting all or part of them for a different string, similar to the replace string method but using regular expressions for both the matching and the replacing. Let's see this in an example.

```python
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Got an email for\
 user@host.name")
'Got an email for [REDACTED]'
```

The expression that we're using for identifying email addresses has two parts: the part before that at sign and the part after it. Check out the part that comes before the at sign. We include the alphanumeric characters represented by backslash w which includes letters, numbers, and the underscore sign as well as a dot, percentage sign, plus, and dash. After the at sign, we only allow the alphanumeric characters dot and dash. This will match all email addresses as well as some strings that aren't really valid email addresses like an address with two dots. In this scenario we want to be better safe than sorry. So we're going to redact anything that looks like an address. If we wanted to validate that the address is an actual email we would need to be a lot stricter.

Let's now look at an example using sub where we use regular expressions for the replacing. For that, we'll go back to our code that switched the order of names of people and use sub to create the new string.

```python
re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
'Ada Lovelace'
```

When referring to captured groups, a backslash followed by a number indicates the corresponding captured group. This is a general notation for regular expressions, and it's used by many tools that support regexes, not just Python.

We can also use them to match patterns that repeat themselves which use capturing groups as back references. We won't look into them here, but if you want to learn more, you'll find a bunch more info about them online.

#### Advanced Regular Expressions Cheat-Sheet

Check out the following link for more information:

- [Regex Cross­word](https://regexcrossword.com/)

## Managing Data and Processes

### Data Streams

#### Reading Data interactively

We've talked before about reading and writing files. Using files to store information and then processing that data over a script is a great way to build automation. But sometimes we need to interact with the user and ask them for certain pieces of information that just can't be stored in a file. To do this Python provides a function called **input**. This function allows us to prompt the user for a certain value that we can then use for our scripts. Let's see what that looks like.

```python
#!/usr/bin/env/ python3

name = input("Please enter your name: ")
print("Hello, " + name)
```

Also see to_seconds.py

#### Standard Streams

We've now seen a couple ways of getting information into and out of our scripts. We know how to read and write to files and accept input from the keyword and print it to the screen, too. But what exactly is going on behind the scenes when we do this? How does a Python program connect to both the screen and the keyboard? Well, it uses I/O streams. **I/O streams** are the basic mechanism for performing input and output operations in your programs.

We call these streams because the data keeps flowing. A program can read input and
generate output as long as it needs to achieve its goal. Okay, what do these streams mean in practice?

Most operating systems supply three different I/O streams by default each with
a different purpose

| Standard Stream                    | Description                                                                                                                      |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Standard Input stream or "STDIN"   | Usually in the form of text data from the keyboard                                                                               |
| Standard Output stream or "STDOUT" | Generally takes the form of text displayed in a terminal                                                                         |
| Standard Error or "STDERR"         | Displays output like standard out, but is used specifically as a channel to show error messages and diagnostics from the program |

#### Environment Variables

When we open a terminal application on a Linux computer, whether it's local or a remote machine, the application that reads and executes all commands is called a **shell**. A shell is a command line interface used to interact with your operating system.

Python programs get executed inside a shell command-line environment. The variables set in that environment which are called **environment variables** and are another source of information that we can use in our scripts.

We can read the contents of these variables from Python. Let's use a Python script to check that out:

```python
#!/usr/bin/env python3
# script name: variables.py
import os

print("HOME: " +) os.environ.get("HOME",""))
print("SHELL: " +) os.environ.get("SHELL",""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
```

To access environment variables, we use the environ dictionary provided by the OS module. In this case, we're using a dictionary method that we haven't used before.

The getMethod is a bit similar to how we've been accessing dictionary values up until now. The difference is what happens when the value isn't present. When we retrieve a value from a dictionary using the key as in OS.environ\[fruit] and the key isn't present, we get an error.

If we use a getMethod instead, we can specify what value should be returned if the key isn't present. In other words, the getMethod allows us to specify a default value when the key that we're looking for isn't in the dictionary. So what we're asking Python to do is try to retrieve the value associated with the key, but if the key's not defined return an empty string instead. We're doing this for three different variables; home, shell, and fruit. Let's run the script and see what happens.

We define the variable by just setting a value using the equal sign and leaving no spaces in between. Along with this, the export keyword tells a shell that we want the value we set to be seen by any commands that we call.

```bash
export FRUIT=Pineapple
```

We can now rerun our variables.py script to check the value of the FRUIT environment variable.

#### Command-Line Arguments and Exit Status

Up to now, we've seen how different programs can read from and write to standard IO streams and how the show environment can influence execution of a program. Yet another common way of providing information to our programs is through command line arguments.

Command-line arguments are parameters that are passed to a program when it started. It's a super common practice to make our scripts receive certain values by command line arguments. It allows a code of the script to be generic while also letting us run it automatically without requiring any interactive user input. This means that these arguments are really useful for system administration tasks. That's because we can specify the information that we want our program to use before it even starts.

```python
#!/usr/bin/env python3
# Script name: parameters.py

import sys

print(sys.argv)
```

Our script just imports the sys module and prints the sys.argv list. Now, let's see what happens when we call the program.

```bash
./parameters.py
['./parameters.py']
```

In this case, we called the script without any parameters. The list contains one single element. The name of the program that we just executed. Let's try passing a few parameters.

```bash
./parameters.py one two three
['./parameters.py', 'one', 'two', 'three']
```

Last up we have the concept of **exit status** or **return code**, which provides another source of information between the shell and the programs that get executed inside of it.

The exit status is a value returned by a program to the shell. In all Unix-like operating systems, the exit status of the process is zero when the process succeeds and different than zero if it fails.

The actual number returned gives additional info on what kind of error the program encountered. Knowing if a command finished successfully or not is helpful information which can be used by a program that's calling a command.

For example, it can use the information to retry the command. If it failed. To check the exit status of a program, we can use a special variable that lets us see what the exit status of the last executed command was.

The variable is the **question mark variable**. So to see the contents we use dollar sign question mark. Let's try this out using the WC command, which counts the number of lines words and characters in a file. First, we'll pass it our variables.py Script and check the exit value.

```bash
wc variables.py
       7      21     200 variables.py
echo $?
0
wc notpresent.file
wc: notpresent.file: open: No such file or directory
echo $?
1
```

Here, **wc** couldn't run for the file that we pass because it doesn't exist. The command printed an error and when printing the contents of the dollar sign question mark variable, we see that it finished with an exit value of one.

So that's with system commands, but what about Python scripts? When a Python script finishes successfully, it exits with an exit value of zero. When it finishes with an error like type error or value error, it exits with a different value than zero. We can make it exit with whatever value is relevant.

```python
#!/usr/bin/env python3
# Script name: create_file.py
import os
import sys

fielname = sys.argv[1]

if not os.path.exists(filename):
  with open(filename, w) as f:
    f.write("New file created\n")
else:
  print("Error: the file {} already exists!".format(filename))
  sys.exit(1)
```

To try this out let's first execute the script and pass a file that doesn't exist:

```bash
./create_file.py example
echo $?
0
cat example
New file created
./create_file example
Error: the file example already exists!
echo $?
1
```

See the "More About Input Functions" addendum file.

### Python Subprocesses

#### Running System Commands in Python

Up to now, we've been using Python to interact with the operating system through baked in functionality. For example, we've used file objects to read the contents of files, used the **shutil** module to check if the disk is full. And use a **sys** module to process standard input, get parameters, or generate an exit code.

But what if we needed to run a system program from a Python script?

Say, for example, that as part of a Python script, we needed to send ICMP packets to a host to check if it's responding. We could try to look for an external module that provides this functionality. Or we can just run the **ping** command, which will send packets for us. Sometimes it's easier or faster to use a system command as part of our Python script to accomplish a task, or use some functionality that doesn't exist in the Python modules, neither built-in or external.

For these cases, Python provides a way to execute system commands in our scripts, using functions provided by the subprocess module. Let's check out an example:

```python
import subprocesses

print(subprocess.run(["date"]))
Mar 27 déc 2022 17:31:10 CET
CompletedProcess(args=['date'], returncode=0)

subprocess.run(["sleep", "3"])
CompletedProcess(args=['sleep', '3'], returncode=0)

result = subprocess.run(["ls", "this_file_does_not_exist"])
ls: this_file_does_not_exist: No such file or directory
print(result.returncode)
```

#### Obtaining the Output of a System Command

If we want our Python scripts to manipulate the output of system command that we're executing, we need to tell the run function to capture it for us. This might be helpful when we need to extract information from a command and then use it for something else in our script.

For example, say you want to create some stats on which users are logging into a server throughout the day. You could do this with a script that calls the **who** command, which prints the users currently logged into a computer. The script could parse the output of the command, storing the list of logged-in users once per hour and at the end of the date to generate a daily report.

To be able to process the output of commands, we'll set a parameter called capture_output to true when calling the run function (requires Python 3.7 or later). For our next example, we'll call the **host** command, which can convert a host name to an IP address and vice versa. When calling it, we'll pass the capture output equals true parameter and store the result in a variable so that we can access it. Let's give it a try:

```python
import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode) # we can check the return code attribute like before
0
print(result.stdout)
b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
```

What's that "b" at the beginning of the string? Well, that B tells us that this string is not a proper string for Python. It's actually an array of bytes, and this is a complex subject.

- _Data in computers is stored and transmitted in bytes and each can represent up to 256 characters. But there are thousands of possible characters out there used to write in various languages. Chinese, for example, requires over 10,000 different characters. To be able to write in those languages, several specifications called encodings have been created over time to indicate which sequences of bytes represent which characters. Nowadays, most people use **UTF-8** encoding, which is part of the Unicode standard that lists all the possible characters that can be represented._

So going back to our example when we execute the command using run, Python doesn't know which encoding to use to process the output of the command. So it simply represents it as a series of bytes. If we want this to become a proper string, we can call the **decode** method. This method applies an encoding to transform the bytes into a string. By default, it uses a UTF-8 encoding which is what we want. So with all that said, let's transform our array of bytes into a string and then split it into several pieces:

```python
print(result.stdout.decode().split())
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
```

We just looked at the captured standard output. But what about standard error? If we use the capture_output parameter and the command writes any output to standard error, it will be stored in the **stderr** attribute of the completed process instance. Let's look at an example of this. We'll try executing the rm command, which we use for removing files passing a filename that doesn't exist:

```python
result = subprocess.run(["rm", "file_that_does_not_exist"], capture_output=True)
print(result.returncode)
1
print(result.stdout)
b''
print(result.stderr)
b'rm: file_that_does_not_exist: No such file or directory\n'
```

We've now seen that we can execute system commands from Python and check whether they succeeded or failed. We've also seen how to capture the standard output and standard error streams so we can use their content in our scripts. These skills can be super useful when writing scripts that your system commands for some involved task and letting our Python scripts cover a broader range of tasks.

#### Advanced Subprocess Management

We've seen how to run system commands from Python, how to check the exit value, and how to manipulate the normal output and error output of the command. The sub process module offers a lot of extra options that we can use in our scripts.

For example, we called out in an earlier video that one way of providing information to our processes is to modify the environment variables. Using this mechanism, we can change where the process looks for executable files, which commands it uses interact with some parts of the system, the kind of output it'll generate and a bunch more things.

The usual strategy for modifying the environment of a child process is to first copy the environment seen by our process, do any necessary changes, and then pass that as the environment that the child process will see. Let's take a look at this:

```python
import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp", my_env["PATH"]])

result = subprocess.run(["my_app"], env = my_env)
```

To recap, this script is modifying the contents of the path environment variable by adding a directory to it. We then call the myapp command with that modified variable. Doing it this way, the command will run in the modified environment with the updated value of path.

There are a bunch more options that we can use with the run function. For example, we can use the **cwd** parameter to change the current working directory where the command will be executed. This can be really helpful when working with a set of directories where you need to run a command on each of them.

We could also set the **timeout** parameter. This will cause the run function to kill the process if it takes longer than a given number of seconds to finish. This might be useful if you're running a command that you know might get stuck. For example, if it's trying to connect to a network and your computer is offline.

Or we can also set the **shell** parameter. If we set this to true, Python will first execute an instance of the default system shell and then run the given command inside of it. This means our command line could include variable expansions and other shell operations. Without the shell parameter, this would not be possible.

We'll learn more about the things that we can do with the shell later in this course. For now, just keep in mind that if you need to expand variables or globs, you'll need to set this parameter.

But using this can be a security risk. So make sure you actually need it and be careful when using it if you do. Before we finish our discussion of the subprocess module, a word of caution.

Interfacing the underlying system directly in your Python scripts via subprocesses and system commands can be useful especially if you need to do a specific task quickly. But it comes with some drawbacks. Using these system-level commands built assumptions into our scripts about the infrastructure, our automation will run on. If those assumptions change, it can lead to unexpected effects or failures. These kinds of assumptions can change in multiple ways.

What would happen to our automation is the flags where terminal command change and our script continues to use the old flags? What happens if we switch operating systems from Linux to Windows? Will our scripts fail outright or will they succeed in unintended and possibly harmful ways?

Any change to the system or external commands our scripts use increases the chances of something breaking. Sometimes that break might be obvious and other times it might be difficult to detect.

- If we're automating a one-off, well-defined task, we're developing a solution quickly is the biggest requirement, then using system commands and subprocesses can help a lot.

- But if we're doing something more complex or long-running, it's usually a good idea to use the baked-in or external modules that Python provides. So before deciding to use a sub processes, it's a good idea to check the standard library or pypi repository to see if we can do the task with native Python and to check if someone has already created the automation that we wanted to write.

Remember that we never want to reinvent the wheel.

#### Python Subprocesses Cheat Sheet

Check out the following link for more information:

- [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)

### Processing Log Files

#### What are log files?

Now we're going to take a look at how we can use these tools to help us with our day-to-day work. In the next few videos, we'll dive into a concrete examples centered around processing chunks of data. The kind of data that you might find in a Syslog file or a web request log. The different events that happen in programs that are running in a system and aren't connected to terminal are usually rendered to log files. Log files contain a lot of useful information, particularly when you're trying to debug a tricky problem that's happening on a computer.

On the flip side, sometimes it can be overwhelming to try to find something inside of a log file that contains a whole lot of lines with a whole lot of things in them.

So it's a good idea to learn how we can process these files and get our tools to extract information that we want out of them. To do this we'll go back to our knowledge of regular expressions. Using regex's in our scripts gives us a great deal of flexibility when processing log files and other texts data sources too. In a script, we can program any kind of behavior we want, so we can manipulate and process text data and get results we need.

#### Filtering Log Files with Regular Expressions

When working with log files and scripts, our first step is usually to open them so our code can access their contents. We've discussed various methods of operating on files. The usual technique is to call the open function which returns a file object and then iterate through each of its lines using a for-loop.

Remember that for performance reasons, when files are large, it's generally a good practice to read them line by line instead of loading the entire contents into memory.

```python
#!/usr/bin/env python3
import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    print(result[1])
```

#### Making Sense out of the Data

We just wrote a script that processed a log file and extracted the names of each user who had started a cron job in the machine that we were investigating. This can be really helpful but there's more information that we might need.

To improve our output, it would be a good idea to have a count of how many times each username appears in our log. As we've seen in earlier examples, dictionaries are great structure to use when we want to count appearances of strings.

We'll store the user name as a keys of a dictionary and we'll use the value to count the number of times that each user name appears in the file. To do this in fewer lines, we'll use the get method that we saw earlier.

```python
#!/usr/bin/env python3
import re
import sys

logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    if result is None: # Checks if the rexgex found a match in the current line
      continue # and continues on to the next one if not
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1
print(usernames)
```

## Testing in Python

### Simple Tests

#### What is testing?

When you're writing a very simple piece of code, say for example, that you're adding two variables, it's pretty straightforward to know what the code does, and be sure they'd does it correctly. As operations become more complex using loops, conditionals, calling more and more functions, it's harder to really be confident that the code will do what it's supposed to. This is where software testing comes into play.

**Software testing** is the process of evaluating computer code to determine whether or not it does what you expect it to do.

When you test a piece of software, you want to find the errors and defects and see where things go wrong. Software testing is similar in lots of ways to the tests performed in the manufacturing process of a new piece of machinery.

Scripts and programs can fail in all sorts of strange ways, especially as it become more complicated. In all but those simple programs, it's next to impossible to test for everything that could go wrong. Even though this means that a certain number of bugs might exist in your scripts without you realizing it, don't worry.

Writing tests can help you eliminate a whole bunch of bugs, helping to improve the reliability and the quality of automation. **Tests can help make good code great**. The field of software testing is pretty broad. In the next few sections we'll explore some fundamental concepts involved like **automated testing**, **unit test**, **integration test**, and **test-driven development**.

As of lots of topics covered in this course, we'll do a quick rundown of the many concepts around testing. It won't be enough instructions for you to become a testing expert, but it should help you with automatically testing your scripts.

#### Manual Testing and Automated Testing

One of the tasks that programmers had to do when writing code is test it to make sure that it behaves the way that they expected to. Having good tests for our software can help us catch mistakes, errors, and bugs before we deploy our scripts to perform real-world automation tasks.

- The most basic way of testing a script is to run it with different parameters and see if it returns the expected values. We've done this manual testing for some of the code that we've written this course already. Executing a script with different command-line arguments to see how its behavior changed is an example of manual testing.

- Using the interpreter to try our code before putting it in a script is another form of manual testing.

Formal software testing takes us process a step further, codifying tests into its own software and code that can be run to verify that our programs do what we expect them to do. This is called **automatic testing**. The goal of automatic testing is to automate the process of checking if the returned value matches the expectations.

_Why would you write more code to test code you have?_

Because when you're testing your code, you want to check if it does what it's supposed to do for a lot of different values. You ought to verify that it behaves the way you expect it to have as many possible values known as **test cases**.

### Unit Tests

As we mentioned, there are lots of different types of test that we can write to perform automatic testing. The most common type is a unit test. Unit tests are used to verify that small isolated parts of a program are correct.

As we mentioned, there are lots of different types of test that we can write to perform automatic testing. The most common type is a **unit test**.

**Unit tests** are used to verify that small isolated parts of a program are correct.

Unit tests are generally written alongside the code to test the behavior of individual pieces or units like functions or methods. Unit tests help assure the developer that each piece of code does what it's meant to do.

An important characteristic of a unit test is **isolation**. Unit test should only test the unit of code they target, the function or method that's being tested. This ensures that any success or failure of the test is caused by the behavior of the unit in question and doesn't result from some external factor like the network being down or a database server being unresponsive.

In other words, when testing a function or method, we want to make sure that we're focusing on checking that the code in that function or method behaves correctly. We don't want our test to fail for external reasons.

Unrelated note, our **tests should never modify the production environment**. This is a live environment that runs a software that users interact with. When developing test, if for any reason we do need to interact with some other software, we'll normally do that in a **test environment**, where we'll have control over how it behaves. **It's our house, our rules**.

So the goal of the unit test is to verify that small, isolated parts of a program are correct. How do we do that? It generally boils down to a simple pattern. Given a known input, does the output of our code match our expectations?

Let's take a piece of code similar to what we wrote awhile back to rearrange a name in the format last name comma first name and think about how we test it. How do you think we can test that it works the way you'd expect it to? Let's start by manually validating that for a given input, it produces expected result. We'll check this by importing the function in an interpreter. To do that, we'll use a keyword that we haven't seen before, **from**:

```python
#In a Python interpreter:
>>>from rearrange import rearrange_name
>>>rearrange_name("Lovelace, Ada")
>>>'Ada Lovelace'
```

#### Writing Unit Tests in Python

We've now looked at the principles behind automatic testing. We know that by having automatic tests, we can run them as many times as necessary to make sure that our code does what we want it to do.

So how we do this in Python? We need to write some code that runs a test and verifies the output. This way, we can get our computer to do the work for us. To demonstrate the testing workflow, we'll create unit tests for the rearrange_name function from the previous section.

As we touched on earlier, automatic tests are usually written alongside the code that we want to test. What this means in practice is creating a separate Python file with the test. **The convention is to call the script with the same name of the module that it's testing and appending the suffix _test**. So for our rearrange module, we'll create the rearrange_test.py file.

To help us with the actual writing of the test, Python provides a module called unittest. Thanks Python! This module includes a number of classes and methods that let us easily create unit tests for our code.

```python
#!/usr/bin/env python3
# Script name: rearrange_test.py
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
```

All right, we're ready to run the test. We'll do that by executing the file that we just created. Let's make our script executable (with chmod +x) and then run it:

```bash
./rearrange_test.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Looks good! The output is pretty descriptive, printing out some information
about how long a group of tests or _**test suite**_ took to run, as well as the number of tests, and whether or not, they passed.

#### Edge Cases

By now we know how to write automatic tests in Python. Our test suite includes only one test case though. We need to make it grow. Choosing test cases can be an exercise in creativity. Coming up with different ways a piece of code might break can actually be super fun.

We'll usually test that our code works in general case. But we should also see what happens when we give it some input that we may not expect it to run into under normal operations. For example, what would happen in our function if we gave it an empty string? Let's add a test for that and see:

```python
#!/usr/bin/env python3
# Script name: rearrange_test.py
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_empty(self):
    testcase = ""
    expected = ""

unittest.main()
```

**Edge cases** are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically work with.

Edge cases usually need special handling in scripts in order for the code to continue to behave correctly.

Whether or not we handle this kind of error depends on how we want the scripts to behave. In our specific case, returning the original value makes sense when we can't rearrange it.

But sometimes you might actually want your program to crash with an error rather than to go on as if nothing happened.

**Remember that it's bad for automation to fail silently**.

Other kinds of edge cases usually include things like passing zero to a function that expects a number, or negative numbers, or extremely large numbers. These types of conditions are good to consider when writing your test, since they can cause your code to crash or behave in unexpected ways. Sometimes it pays to be a pessimist. You can see how it might require some creativity to come up with these examples. The upside is that when writing automatic tests, once you've come up with example, it's there to stay.

#### Additional Test Cases

```python
#!/usr/bin/env python3
# Script name: rearrange_test.py
from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(testcase), expected)

  def test_double_name(self):
    testcase = "Hopper, Grace M."
    expected = "Grace M. Hopper"
    self.assertEqual(rearrange_name(testcase), expected)

  def test_one_name(self):
    testcase = "Voltaire"
    expected = "Voltaire"
    self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
```

One of the great things about running tests in a suite like this, is that we now know that all the test cases we wrote were handled correctly. Our code works for basic names, empty strings, double names, and single names. If we found another case that made our tests break, we could add it to the suite, fix the bug, and then run the whole suite again, being assured that all the other cases are still working.

### Other Tests Concepts

#### Black Box vs. White Box

There are lots of different tests that we can use to make sure our software is behaving how we expect it to. We've explored unit test in detail which are both simple to write and are very powerful way to catch bugs. But there's a lot more to software testing. One interesting concept is whether our test is a **white-box test or a black-box test**.

- **White-box testing** also sometimes called **clear-box** or **transparent testing** relies on the test creators knowledge of the software being tested to construct the test cases.

- **Black-box tests** are written with an awareness of what the program is supposed to do, its requirements or specifications, but not how it does it.

Both white-box and black-box tests have their own advantages.

White-box tests are helpful because a test writer can use their knowledge of the source code to create tests that cover most of the ways that the program behaves. Black-box tests are useful because they don't rely on the knowledge of how the system works. This means their test cases are less likely to be biased by the code. They usually cover situations not anticipated by the programmer who originally wrote the script.

Not all tests that we write needs to fall to one category or the other. We can write unit tests that are either white or black-box, depending on which testing methodology is chosen.

- If the unit tests are created before any code is written based on specifications of what the code is supposed to do, they can be considered black-box unit test.

- If unit tests are run alongside or after the code has been developed, the test cases are made with a knowledge of how software works. They are white-box tests. One way isn't strictly better than the other since each gives you a different path to make your code more reliable.

Not everything is so black and white or as we'd say in the coding world, binary. As an IT specialist, you may need to test that software written by others behaves the way you expect it to. To do this, you can use the combination of black-box and white-box test.

#### Other Test Types

When we looked at unit tests, we call out they should focus on one specific unit, a functional method that being tested. This allows the test to verify the unit provides expected functionality regardless of the rest of the environment. On the other hand, integration tests verify that the interactions between the different pieces of code in integrated environments are working the way we expect them to. While unit tests shouldn't cross boundaries to do things like make a network request or integrate with an API or database, the goal of an integration test is to verify these kinds of interactions and make sure the whole system works how you expect it to.

- **Integration tests**, usually take the individual modules of code that unit test verify then combine them into a group to test. Depending on what our program does, and how it interacts with the rest of the systems involved, we might need to create a separate test environment for our test. Which runs a test version of our software that we're trying to verify. We might be able to run our test against the actual version of our system that's running, but that's only if our code doesn't make any changes to the production environment. Whenever your company is deploying a system that's somewhat complex, having integration tests will help make sure that all the pieces come together the way you expect them to. These tests usually take a bit more work to set up because you'll need to make sure that you have the test versions of all relevant systems. But they might help catch issues that unit tests won't text, so the extra effort is definitely worth it. For example, if the service you're trying to test interacts with a database, you want to set up a separate test database with a test user and a test tables. This lets you run all tests you need in an environment that you can control without risking modifying the production database.

- A variant of unit tests are **regression tests**. They're usually written as part of a debugging and troubleshooting process to verify that an issue or error has been fixed once it's been identified. Say our script has a bug and we're trying to fix it. A good approach to doing this would be the first right to test fails by triggering the buggy behavior, then fix the bug so that a test passes. Regression tests are useful part of a test suite because they ensure that the same mistake doesn't happen twice. The same bug can't be reintroduced into the code because introducing it will cause the regression test to fail.

- **Smoke tests** sometimes called **build verification test**, get their name from a concept that comes from testing hardware equipment. Plug in the given piece of hardware and see if smoke starts coming out of it. When writing software smoke test serve as a kind of sanity check to find major bugs in a program. Smoke test answer basic questions like, does the program run? These tests are usually run before more refined testing takes place. Since if the software fails the smoke test you can be pretty sure none of the other tests will pass either. As they say where there's smoke there's fire. For a web service the smoke test would be to check if there's a service running on the corresponding port. For an automation script, the smoke test would be to run it manually with some basic input and check that the script finishes successfully.

- Other types of tests are **load tests**. These tests verify that the system behaves well when it's under significant load. To actually perform these tests will need to generate traffic to our application simulating typical usage of the service. These tests can be super-helpful when deploying new versions of our applications to verify that performance does not degrade. For example, we might want to measure the response time of our website while there are 100 requests per second on our pages, or a 1000, or 10,000. The actual numbers will depend on the expectations of how much traffic our website will receive.

Taking together a group of tests of one or many kinds is commonly referred to as a **test suite**. A good diversity of test types can create a more robust test suite that helps ensure your scripts and automation, do what you tell them to. There are many more kinds of tests out there, we've only touched on a few of the most common types. If you're interested in learning more about the way software can break and how to test for that, all kinds of books and articles have been written on the subject.

#### Test-Driven Development

You might expect that most testing happens after the code has been written. This seems like a natural progression. First you write your script then you write tests that verify that the script does what you want it to do. But this isn't always the best approach.

A process called **test-driven** or **TDD** calls for creating the test before writing the code. This might seem a bit counter-intuitive, but it can make for more thoughtful well-written programs. When presented with a new problem that can be solved by automation, your gut instinct might be to fire up your code editor and start writing.

But creating some tests first make sure that you've thought about the problem that you're trying to solve and some different approaches that you might use to accomplish it. Writing a test first also helps you think about the ways your program could fail and break which can lead to some valuable insights and even change the approach you take for the better.

The test-driven development cycle typically involves first writing a test then running it to make sure it fails. After all, you haven't written the code to make it passed yet. Once you've verified it fails, you write the code that will satisfy the test then run the tests again. If it passes you can continue on to the next part of your program. If it fails you Debug and run the test again. The cycle is repeated for each new feature of your script until it's up and running. So before you write your next Python program, you might want to think about the tests you can create to make sure it's working as you expect.

There are all resources out there if you'd like to learn more about how you can create code using the test-driven development approach. Lots of them are Python-centric, but the principles can be applied to any language you need to create in.

Hopefully you can see the benefits of writing tests to validate the code rate. You gain some understanding about a different testing techniques available. Remember that good tests help make any automation and script you write more robust, resilient, and less buggy. Having reliable automation makes life better for everyone.

Many companies take testing a step further and combine it with our version control systems and development processes. When engineers submit their code, it's integrated into the main repository and tests are automatically run against it to spot bugs and errors in a process called **Continuous Integration**. Although useful, setting up a continuous integration process can be a big undertaking. Wew ill talk more about it later. In the meantime, if you use unit tests to validate the code you write, you're already on your way to a more reliable and robust automation.

#### More About Tests

Check out the following links for more information:

- [https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/](https://landing.google.com/sre/sre-book/chapters/monitoring-distributed-systems/)

- [https://landing.google.com/sre/sre-book/chapters/testing-reliability/](https://landing.google.com/sre/sre-book/chapters/testing-reliability/)

- [https://testing.googleblog.com/2007/10/performance-testing.html](https://testing.googleblog.com/2007/10/performance-testing.html)

- [https://www.guru99.com/smoke-testing.html](https://www.guru99.com/smoke-testing.html)

- [https://www.guru99.com/exploratory-testing.html](https://www.guru99.com/exploratory-testing.html)

- [https://testing.googleblog.com/2008/09/test-first-is-fun_08.html](https://testing.googleblog.com/2008/09/test-first-is-fun_08.html)

### Errors and Exceptions

#### The Try-Except Construct

Along our journey learning Python, we've encountered errors generated by the interpreter a bunch of times. We've seen examples of TypeError, IndexError, ValueError, and others. Up to now whenever the interpreter threw one of these errors we changed our code to avoid the error. That's a common approach since whenever the interpreter raises one of these errors the program stops, and we don't want our scripts to come to an end before they're done doing their work.

Sometimes it's easier to make a verification with the conditional to avoid the error. Other times there are so many things that could go wrong that checking for all of them becomes challenging.

Say you had a function that opened a file and did some processing on it. What if the file doesn't exist? What if the user doesn't have permissions to read the file? Or what if the file is locked by different process and can't be opened right now? We could check all of these conditions but what if there's yet another thing that could cause the open function to raise an error. In a case like this, a better approach is to use the try-except construct.

Let's look at how it works in an example:

```python
#!/usr/bin/env python3

def character_frequency(filename):
  """Counts the frequency of each character in a given file"""
  # First try to open the file
  try:
    f = open(filename)
  except OSError:
    return None

  # Now process the file
  characters = {}
  for char in line:
    characters[char] = characters.get(char, 0) + 1

f.close()
return characters

```

Our character_frequency function here reads the contents of a file to count the frequency of each character in them. To do that, the first step is to open the file. In this example, we've put the call to the open function inside a try-except block. What this does is first try to do the operation that we want which in this case is to open the file. If there's an error, it then goes into the accept part of the block that matches the error and does whatever cleanup is necessary. Here we have only one except block, for the OSError error type, but there could be more blocks if the functions called could raise other types of errors.

So when writing a try-except block, the important thing to remember is that **the code in the except block is only executed if one of the instructions in the try block raise an error of the matching type**.

In this case, in the except-block, we're returning none to indicate to the calling code that the function wasn't able to do what was requested of it. Returning none when something fails is a common pattern but not the only one. We could also decide to set a variable to some base value like zero for numbers, empty string for strings, empty list for list, and so on. It all depends on what our function does and what we need to get that work done.

The important point is that when we have an operation that might raise an error we want handle that failure gracefully by using the try-except block. The operation could be opening a file, converting a value to a different format, executing a system command, sending data over the network or any other action that might fail and isn't trivial to check with a conditional.

To use a try-except block, we need to be aware of the errors that functions that we're calling might raise. This information is usually part of the documentation of the functions. Once we know this we can put the operations that might raise errors as part of the try block, and the actions to take when errors are raised as part of a corresponding except block.

#### Raising Errors

We looked into how to handle errors when they're raised by the functions that we call. In some cases, we might want to raise an error ourselves. This usually happens when some of the conditions necessary for a function to do its job properly aren't met and returning none or some other base value isn't good enough.

Let's look at this through an example. Say we had a function that verifies whether a chosen username is valid. One of the checks this function does is verify that the provided name is at least a certain amount of characters with the minimum value received by a parameter.

```python
#!/usr/bin/env python3

def validate_user(username, minlen):
  if len(username) > min len:
    return False
  if not username.isalnum():
    return False
  return True
```

This code works as long as the provided values are sensible. What would happen if the minlen variable is zero or negative number? Our function will allow an empty username as valid which doesn't make much sense.

To prevent this from happening, we can add an extra check to our function which will verify the receipt parameters are sane. In this case, returning false would be misleading because it's not necessarily that the username is invalid but the provided minlen value doesn't make sense. So let's add a check to verify that minlen is at least one and raise an error if that's not the case.

```python
#!/usr/bin/env python3

def validate_user(username, minlen):
  if minlen < 1:
    raise ValueError("minlen should be at least 1")
  if len(username) > min len:
    return False
  if not username.isalnum():
    return False
  return True
```

As you can see, the keyword to generate an error in Python is **raise**. We can raise a bunch of different errors that come already pre-built with Python or we can create our own, if the standard ones aren't good enough. In this case, we're raising a **value error**, a type of error that we've come across before to indicate that there was a problem with one of the values of the parameters.

What if instead of passing the string we pass something different as a username to validate?

**It's usually the responsibility of whoever is calling a function to call it the right parameters**. But in some cases, we might want to do this explicitly by checking that we're receiving a value that makes sense to that function.

So let's look at an alternative to the raise keyword that we can use for situations where we want to check that our code behaves the way it should particularly when we want to avoid situations that should never happen. This is the **assert** keyword. This keyword tries to verify that a conditional expression is true, and if it's false it raises an **assertion error** with the indicated message. Let's add an assertion to our function.

```python
#!/usr/bin/env python3

def validate_user(username, minlen):
  assert type(username) == str, "username must be a string"
  if minlen < 1:
    raise ValueError("minlen should be at least 1")
  if len(username) > minlen:
    return False
  if not username.isalnum():
    return False
  return True
```

We've added an assertion that verifies that the type of the username variable is STR which we know is a name that the interpreter uses for strings. If the function is called with a username parameter that's not a string, an error will be raised with the message we provided.

As we've called out, we usually don't need to check the types of our parameters. Depending on what our function does, it might be perfectly okay for it to allow scripts to call it with parameters of different types. Assertions can be super helpful for debugging some code that's not behaving the way we expect it to. We can add them at any point where we want to ensure that the variables contain the values and types that they should or when we think that's something that shouldn't happen is happening.

**Heads up though**: _Assertions will get **removed** from our code if we ask the interpreter to optimize it to run faster_.

So as a rule, we should use **raise** to check for conditions that we expect to happen during normal execution of our code and **assert** to verify situations that aren't expected but that might cause our code to misbehave.

#### Testing for Expected Errors

we looked into how we can create unit tests for our functions, for both the basic cases and the edge cases. We called out that we should try to cover lots of different possible cases. To make sure that our function behaves correctly in all of them. With some edge cases, like negative value of minlen in our earlier example, the expectation is that the function will raise an error and we want to be able to test that too. So, how do we do that? Well, we use the _**assertRaises** method_ provided by the unit test module. Let's check this out by adding a couple of test cases to the test suite for our validate user function:

```python
#!/usr/bin/env python3

import unittest

from validate_user import validate_user

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)

# Run the tests
unittest.main()
```

See [Handling ErrorsCheat-Sheet](Handling Errors Cheat-Sheet.html)

## Bash Scripting

### Basic Linux Commands

We've already used a bunch of Linux commands by now. So hopefully these commands aren't too foreign. You may remember that **echo** is a command used to print messages to the screen, **cat** is command for showing contents of files, **ls** is the command to list contents of a directory, **chmod** is a command to change permissions of a file, and so on. As we call that before, a lot of these commands come from Unix. Back in the 70s, when designing how these programs should behave, the philosophy was **that they should do one thing and do it very well**. Which means we have a lot of commands, each for doing specific thing.

- To create a new directory, we use the **mkdir** command. To change into that directory, we use the **cd** command. As you might notice, these commands don't print anything to the screen. This is normal and to be expected. A lot of the commands that we'd use don't print anything when they succeed. They only print something if they fail. To check that the **cd** command succeeded, we can use a command like **pwd** to print the current working directory. Okay. We have a directory which is empty. We can copy files using the **cp** command.

- Lets' call the command **ls** with the **-la arguments**. Remember, command-line arguments let us change the behavior of commands making them do what we want.

What are all those dots? These are shortcuts that we can use to refer to some special directories. But dot-dot shortcut reverses a parent directory, the previous directory and the absolute path while the dot shortcut reverses the current directory. The dot shortcut, for the current directory, and a dot dot shortcut for the parent directory.

What are these columns? The first column indicates the permissions of the file. The second column is the number of i nodes that point to the file. The third and fourth columns indicate the owner and the group to which the file belongs. Then comes the size of the file that they've less modification and finally, the name.

- To rename or move a file, we use the mv command.

- To delete these files, we can use a rm command. We can either go one-by-one or we delete them all together using the star. The star is a placeholder that gets swapped
out by the names of all the files in our directory. We can delete a directory using **rmdir**. This command only works on empty directories so I wouldn't work if we had left any files in it.

That was a quick overview of some of the commands we have in Linux to operate with files and directories. There are tons of other commands to talk about. Make sure to investigate and practice using all on your own. Remember that reading the documentation, for any given system command, can help you learn more about what it does. On Unix-based systems, this documentation can usually be found in manual or man pages using the **man** command.

### Redirecting Streams

So now that we've covered a few basic Linux commands, let's talk more about what we can do with I/O streams and Bash. We talked earlier about the standard I/O streams. By default, the input is provided by the keyboard at the text terminal and the output and error are shown on the screen. This is the case not only for our Python scripts, but for all system commands.

We can change this default using the process called redirection. Redirection is a process of sending a stream to a different destination. This process is provided to us by the operating system and can be really useful when you want to store the output of a command in a file, instead of just looking at it on a screen. To redirect the standard output of a program to a file we use the greater than  **>** symbol.

```python
#!/usr/bin/env python 3
# Script name: stdout_example.py
print("Don't mind me, just a bit of text here...")
```

If we run this program without redirection the text will be sent to the display using the **STDOUT** normally. But now if we use a greater than character to redirect the output instead something else happens entirely.

```bash
$ ./stdout_example.py > newfile.txt
$
```

When you run it this way the STD out from stdout_example.py script is redirected to a file called new_file.txt. If that file doesn't exist, it's created. Let's look at the contents new_file.txt using the cat command:

```bash
$ cat newfile.txt
Don't mind me, just a bit of text here...
```

Beware, just like we saw earlier with the w file mode used by the open function each time we perform of redirection of STD out, the destination is overwritten.

So we need to be super careful when using this redirection that we're not overwriting a file with valuable contents.

If we want to **append** the redirected standard out to a file we can use the double greater than sign >> instead of single greater than.

In a similar way we can also redirect standard input. Instead of using the keyboard to send data into a program, we can use the less than symbol to read the contents of a file. Let's try this out with a new version of the streams.py file that we saw in earlier and redirect the contents of our new file to this script:

```python
#!/usr/bin/env python 3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")
```

```bash
$ ./streams_err.py < newfile.txt
This will come from STDIN: Now we write it to STDOUT: Don't mind me, just a bit of text here...
Traceback (most recent call last):
  File "./streams_err.py", line 5, in <module>
    raise ValueError("Now we generate an error to STDERR")
ValueError: Now we generate an error to STDERR
```

In this case, we don't see the input on the screen in the STDIN portion. This is expected because the input was read from a file. So it only appears in the STDOUT portion where we see that it read one of the two lines. This is also expected because the input function only reads until it encounters a new line character.

It can also be useful to redirect STD_err or to capture errors and diagnostic messages from a program. This can be done by using the character combination **2>** than similar to how we redirected STD out before. Let's execute our stream example again, this time redirecting the err output to a separate file.

```bash
$ ./streams_err.py < newfile.txt 2> errorfile.txt
This will come from STDIN: Now we write it to STDOUT: Don't mind me, just a bit of text here...
$ cat errorfile.txt
Traceback (most recent call last):
  File "./streams_err.py", line 5, in <module>
    raise ValueError("Now we generate an error to STDERR")
ValueError: Now we generate an error to STDERR
```

So this time we don't see the error message on the screen. That's because we redirected it to the error file.

If you're wondering about the number 2, it represents the file descriptor of the STDErr stream. In this context you can think of a file descriptor as a kind of variable pointing to an IO resource. In this case the STDErr stream. 0 and 1 are the file descriptors for STDIN and STDOUT.

Like we call it out already. None of this is exclusive the python we can operate in the same way with all other commands. For example We can create a file using the **echo** command and redirecting its output to the file that we want to create.

#### Pipes and Pipelines

On top of the redirection to and from files that we saw earlier, there's another powerful way to perform IO stream redirection called **Piping**. Using **pipes**, you can connect multiple scripts, commands, or other programs together into a data processing pipeline.

Pipes connect the output of one program to the input of another in order to pass data between them. This means we can pass data between programs, taking the output of one and making it the input of the next. Pipes are represented by the pipe character **|**. Using pipes is an extremely useful tool. It allows us to create new commands by combining the functionality of one command, with the functionality of another without having to store the contents in an intermediate file. So let's work on our plumbing, shall we?

```bash
$ ls -l | less
...
```

The list of files generated by ls is piped to less, which displays them one page at a time. We can scroll up or down using the page up, page down, or arrow keys. Once we're done looking at the files, we can quit with Q.

But it doesn't have to stop there. It's possible to connect a lot more than just two programs using pipes. We'll check this out using a more elaborate example:

```bash
$ cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head
   7 the
   3 up
   3 spider
   3 and
   2 rain
   2 climbed
   2 came
   2 bitsy
   1 waterspout.
   1 washed
```

That's a complex command line. Let's go through it step by step. We're first using **cat** to get the contents of our spider.txt file. Those contents are then sent to a command called **tr**, which gets its name from the word translate. It takes the characters in the first parameter, in this case, it's a space and then transform them into a character in the second parameter. In this case, it's a newline character. So basically, what we're doing is putting each word in its own separate line. Hurrah for organization. Next, we pass results to the **sort** command through a pipe. This command sorts results alphabetically. The sorted results are then passed to the **uniq** command, which displays each match once, and by using a -c flag, it prefixes each unique line with a number of times it occurred. This output is passed via pipe to the **sort** command once more, this time, with the -nr flag, which sorts results numerically and in reverse order, from most to least hits. The output is finally passed to the **head** command, which prints the first 10 lines to STDOUT.

That's a lot of process, but when you break it down, it makes lot of sense, right? The point isn't to memorize all these commands, but to know that we can pipe as many commands as we need to do exactly what we want.

You can use your Python scripts and pipelines too. Python can read from standard input using the **stdin** file object provided by the **sys** module. This is a file object like the one we obtained using the open function, and like your local library, this file object is already open for reading. Let's say we want to write a script that reads each line of the input and then prints a line with the first character in uppercase. To do this, we'll take advantage of the capitalize string method:

```python
#!/usr/bin/env python3
# Script name: capitalize.py

import sys

for line in sys.stdin:
  print(line.strip().upper())
```

```bash
$ cat haiku.txt | ./capitalize.py
Advance your career,
Automating with python,
It's so fun to learn.
```

We don't need to use a pipe t  get the contents of the Haiku.txt file into standard input of our script. Instead  we use the redirection operator we saw earlier:

```bash
$ ./capitalize.py < haiku.txt
Advance your career,
Automating with python,
It's so fun to learn.
```

As a rule, if you just need to get something from standard input into your script, using a redirection is enough. But if you want this to be part of a bigger pipeline of commands, you'll need to combine them with pipes.

For example, if we only want to capitalize the lines that match a certain pattern, we could first call **grep** and then connect it with the pipe to our scripts.

With a little practice, creating pipelines is a fast and powerful way to perform lots of system administration tasks. When a system command doesn't exist with the functionality that you need, you can write a Python script to fill in the gap and include it in your pipeline. Understanding how to redirect IO streams can come in handy in many situations and when writing code too.

#### Signalling Processes

When dealing with the operating system, we usually have a bunch of different processes that we use to accomplish what we want. And like any well oiled machine, we generally need these processes to communicate with each other. For example, we might have a program that starts a background process and wants it to terminate after a timeout. One way of communicating this is through the pipelines we learned about in the last video. Another way of communicating is through the use of signals.

**Signals** are tokens delivered to running processes to indicate a desired action. Using signals, we can tell a program that we want it to pause or terminate. We can also cause it to reload its configuration, or to close all open files.

Knowing how to send these signals lets us interact with processes and have more control over how they behave. There are a bunch of different ways that we can send these signals. For example, let's execute the **ping** command in our terminal.

```bash
$ ping www.example.com
PING www.example.com (93.184.216.34): 56 data bytes
...
```

The ping command is now running, sending ICMP packets to machine over the network once per second. And it will keep running forever unless we interrupt it. To do that, we can use the Ctrl-C combination. hen we interrupt it, the program doesn't just end abruptly. First it prints a summary of what it did and what the results were. It's very polite under these circumstances. What's happening behind the scenes is the process received a signal indicating that we wanted it to stop. When that signal's received, the process does whatever it needs to finish cleanly. The signal that control see sense is called **SIGINT**. It's just one of many signals that we can send.

Another keyboard combination that we can use to send a signal is _Ctrl-Z_. Let's try this one out:

```bash
$ ping www.example.com
PING www.example.com (93.184.216.34): 56 data bytes
[...]
zsh: suspended  ping www.example.com
```

This time the process didn't finish properly. We get a message saying that it's stopped. What's going on? The signal that we sent is called **SIGSTOP**. This signal causes the program to stop running without actually terminating. But don't worry, we can make it run again by executing **fg**.

The fg command makes our program run once more and will keep going until we interrupt it either with Ctrl-C, Ctrl-Z, or some other signal. Let's stop it now with Ctrl-C. By pressing Ctrl-C this time, we've made the program finish cleanly.

To send other signals, we can use the command called **kill**. By default, Kill will send a signal called **SIGTERM** that tells the program to terminate. Since Kill is a separate program, we need to run it on a separate terminal. And we also need to know the **process identifier or PID** of the process that we want to send the signal to. To find out the PID that we want to send the signal to, we'll use the **ps** command which list the currently running processes. Depending on what options that we pass, it'll show different subsets of processes with different amounts of detail. For this example, we'll call ps ax, which lists all the running processes in the current computer. And then we'll use the grep command to only keep lines that contain the name of the process that we're looking for:

```bash
$ ping www.example.com
PING www.example.com (93.184.216.34): 56 data bytes
...
```

From another terminal:

```bash
$ ps ax | grep ping
46024 s000  R      0:00.00 grep ping
46011 s001  S+     0:00.01 ping www.example.com
$ kill 46011
```

We've now sent the **SIGTERM** signal and the process was terminated. Hasta la vista process. Notice how in this case, we didn't get the nice summary at the end, the program just finished.

As you might expect, there is more signals that we can send and they might cause programs to react differently. Many long running programs, for example, will reload their configuration from disk if we send them a signal. This way we can let the program know that there's an important change in the configuration and it can get applied without the program having to stop to reread it. Programs that provide web services may also receive a signal to tell them that they should finish dealing with any currently open connections and then terminate cleanly once it's done. Understanding what these signals are and how to send them will let you interact with the processes on your system that you're in charge of and make them behave as you want.

See [Basic Linux Commands Cheat-Sheet](Basic_Linux_Commands_Cheat-Sheet.html) & [Redirections, Pipes and Signals](Redirections_Pipes_and_Signals.html)

### Scripting with Bash

#### Creating Bash Scripts

We mentioned in earlier videos that bash is the most commonly used shell on Linux. **Bash** is not only the interpreter that runs our commands, it's also a _scripting language_. We can use Bash to write simple scripts when we need to use a lot of commands.

Let's start with an example of why you would even want to do this. In your job as an IT specialist, you sometimes need to debug a computer that's not behaving correctly. There are lots of commands that can tell you what's going on in there to help you with your debugging. For example, the **ps** command can list all the current running processes. The **free** command can show you the amount of free memory. The **uptime** command can tell you how long the computer has been on and so on. Anytime you need to debug a computer, you can manually run these commands one by one, followed by as many commands as you can think of that might be helpful. But that already sounds tedious just describing it.

What if instead, you can run a single command that can gather all these information in just one shot? Well, I have some good news for you. We can do this by creating a Bash script that contains all of the commands that we want to call, one after the other:

```bash
#!/bin/bash
# Script name: gather_information.sh
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"
```

The script we're seeing here is calling three main **commands**, **uptime**, **free**, and who, which lists users currently logged into the computer. It uses the **echo** command to print some other information and to make the output a bit more readable by leaving empty lines between the commands. We're also calling the **date** command to print the current date. To call this command, we're using a _special notation_ by putting the command inside dollar sign parentheses. This indicates that the output of the command should be passed to the echo command and be printed to the screen.

As the script is written right now, there's one command per line. That's a common practice, but it's not the only way. We could also write the commands on the same line using semicolons **;** to separate them.

#### Using Variables and Globs

Like we said earlier, bash is a fully powered scripting language, not just a way of executing commands one after the other. We can assign variables, conditional operations, execute loops, defined functions, and so much more. So much that will only get to cover the very basics in these next few videos. Let's start with variables. Much like Python, bash lets us use variables to store and retrieve values.

Heads up: there can be **no spaces between the name of the variable and the equal sign**, or between the equal sign and the value. If we try to define a variable and leave a space at one side or the other, the show will complain that it can't find the command with the name that we're assigning.

```bash
$ example=hello
$ echo $example
hello
```

Also remember that any variable that you define in your script or in the command line is local to the environment where you define it. If you want commands from that environment to also see the variable you need to export them using the **export** keyword. Now, let's modify our script to gather info and add a variable to it. We'll use it to make our script look nicer by adding lines in between each of the commands. To do this, we'll define a variable called line, and we'll put a bunch of dashes in it.

```bash
#!/bin/bash
# Script name: gather_information.sh
line="------------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"
```

Let's move on to another interesting feature available in bash called **globs**. Globs are characters that allow us to create list of files. The star **\*** and question mark **?** are the most common globs. Besides being extremely fun to say globs, using these globs lets us create _sequences of filenames that we can use as parameters to the commands we call an our scripts_. You've probably come across them before, but let's do a quick recap of how we can use them.

- In bash, using a star in the command line we'll match all filenames that follow the format that we specify. A star with no prefix or suffix would match all the files in the current directory.

- Alternatively, the question mark symbol can be used to match exactly one character instead of any amount of characters, and we can repeat it as many times as we need. For example, we can get the Python files with five characters in their name by using the five question marks together.

Using globs like this lets us create list of files that we might operate on, like calling other commands in passing this list. If you want to use this functionality in Python, it's available through the glob module.

#### Conditional Execution in Bash

One of the main concepts of programming is being able to branch the execution according to a condition. In other words, making our program behave in different ways depending on one or more values.

In Python, we use the if block and the condition is an expression that has to evaluate to true or false.

In Bash scripting, the condition used is based on the exit status of commands. Reminder: we can check the exit status for command using the dollar sign question mark **$?**. And in Bash scripting an exit value of zero means success. This logic is used by the if operator in bash.

To create a conditional expression, we're going to call a command and if the exit status of that command is zero, then the condition will be considered true. Say we wanted to verify that the /etc/hosts file contains an entry for 127.0.0.1, which it should. Knowing that grep will return it exit status of zero when it finds at least one match and different than zero if it doesn't find a match, we can use it to do this verification.

```bash
#!/bin/bash
# Script name: check_localhost.sh

if grep "127.0.0.1" /etc/hosts; then
  echo "Everything ok"
else
  echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi
```

Let's test it:

```bash
$ ./check_localhost.sh
127.0.0.1       localhost
Everything ok
```

So our script said that everything was okay. If **grep** hadn't found that line, it would have exited with a value different than zero and we would've received a different message. There is plenty of other conditions that we might want to check in our scripts, if the file exists, if two strings are equal, if a number is less than another number, and so on. To help us with evaluating these conditions, there is a command called **test**.

Test is a command that evaluates the conditions received and exits with zero when they are true and with one when they're false.

```bash
$ if test -n "$PATH"; then echo "Your PATH is not empty"; fi
Your PATH is not empty
```

We're using the -n option for the test command, which checks if a string variable is empty or not. In this case, path is an empty, so we get the message. Using the test command like this is so common, there's another way of writing it, which looks more like other programming languages. It's something like this:

```bash
$ if [ -n "$PATH" ]; then echo "Your PATH is not empty"; fi
Your PATH is not empty
```

In this case, the command we're calling is the opening square bracket. This is an _alias_ to the **test** command, but to call it successfully, we also need to include a closing square bracket. **When using this syntax, remember that there needs to be a space before the closing bracket**.

There's plenty of other things that we can check with test, but we won't cover them here. We'll include some of them in the upcoming cheat sheet and
you can also see all of them by looking at the manual page for test.

#### Bash Scripting Resources

Check out the following links for more information:

- [https://ryanstutorials.net/bash-scripting-tutorial/](https://ryanstutorials.net/bash-scripting-tutorial/)

- [https://linuxconfig.org/bash-scripting-tutorial-for-beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)

- [https://www.shellscript.sh](https://www.shellscript.sh)

### Advanced Bash Concepts

Bash provides similar looping structures to Python. We can iterate while a condition is true using a _while loop_ and iterate over a list of elements using a _for loop_. Although of course, the syntax for these loops is slightly different.

#### While Loops in Bash Scripts

Let's check out a simple while loop in Bash. The condition for the while loop usesthe same format as a condition for an if block. The loop itself starts with the do keyword and finishes with a done keyword. To increment the value of the variable n, we're using a bash construct of double parentheses that lets us do arithmetic operations with our variables:

```bash
#!/bin/bash

n=1
while [ $n -le 5]; do
    echo "Iteration number $n"
    ((n+=1))
done
```

So that works but what about making our loop a bit more interesting. When using while loops and bash scripts, it's common to have a loop that retries a command a number of times until it succeeds. This is really useful with commands that use network connections or that access resources that might be locked. These commands can fail for external reasons and they're likely to succeed after a retry or two.

To simulate a command that sometimes succeeds or sometimes fails, we have a small Python script that will return an exit value picked at random by a range that we give it:

```python
#!/usr/bin/env python3
# Script name:random-exit.py

import sys
import random

value = random.randint(0, 3)
print("Returning: " +str(value))
sys.exit(value)
```

Let's trun the simulation:

```bash
$ ./retry.sh ./random-exit.py
Returning: 1
Retry #1
Returning: 2
Retry #2
Returning: 0
```

#### For Loops in Bash Scripts

Both in Python and Bash, _for loops_ are used to iterate over a sequence of elements. You might remember that the key to for loops is that they let us perform an operation on each of the elements in a sequence.

- In Python, the sequences are data structures like a list or a tuple or a string.

- In Bash, we construct these sequences just by listing the elements with spaces in between. Let's check this out using a very simple example:

```bash
#!/bin/bash
# Script name: fruits.sh
for fruit in peach orange apple; do
    echo "I like $fruit!"
done
```

Let's use a practical example to see this in action. Imagine that you're migrating your company's website from one web server software to another. Your web content is stored in a bunch of files that all end in uppercase HTM, and the new software requires that they all end in lowercase html, disaster!

You can manually rename them one by one using the MV command, but that could get really old really fast. You'd likely end up making mistakes after the first few commands. Instead, you could do the same thing with short Bash script.

First, let's check out our files.

```bash
$ cd old_website
$ ls -l
-rwx------@ 1 user  staff  0 Jan  9 12:26 about.HTM
-rwx------@ 1 user  staff  0 Jan  9 12:26 contact.HTM
-rwx------@ 1 user  staff  0 Jan  9 12:26 footer.HTM
-rwx------@ 1 user  staff  0 Jan  9 12:26 header.HTM
-rwx------@ 1 user  staff  0 Jan  9 12:26 index.HTM
```

Looks like we have five files that we need to rename. So how can we extract the part before the extension? There's a command called **basename** that can help us with that. This command takes a filename and an extension and then returns the name without the extension. Just like that, we're ready to write our script and rename the files.

```bash
#!/bin/bash

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    echo mv "$file" "$name.html" #prefixing mv with echo for testing purposes
done
```

We're surrounding our file variable with double-quotes to allow the command to work even if the file has spaces in its name. This is a good practice in Bash scripts when dealing with file names or any variables that could include spaces

We'll then call the **mv** command with the old and new names. In this case, we use double quotes for both parameters. Again, we want to make sure that it works correctly for file names with spaces, and that's all that our loop needs to do. We'll finish our loop of the done keyword, and we're done, almost.

We still need to run our script to see if it does what it should. Now, let me share a trick with you that might save you a few headaches. **Whenever you're going to run a script like this that modifies the files in your file system, it's a really good idea to first run it without actually modifying the file system**. This will catch any possible bugs that the script might have.

So instead of just running it as it is right now, we'll add an echo in front of the MV command. This means that instead of actually renaming, our script we'll print the renaming that it plans to do.

Hopefully by now, you're starting to see how you can benefit from using Bash scripts when dealing with files and system commands, especially to compliment your Python scripts.

#### Advanced Command Interaction

We've learned a lot about how to do things in the Linux command line and in Bash scripts. We will now look at a couple of interesting applications for all these Bash scripting powers that we just learned to put all this new knowledge into action. Let's go back to our old friend, the system log file located in var/log/syslog. The system log file contains a trove of information about what's going on in the system. So it's really important to learn how to get information out of it.

Let's use the tail command to look at the last 10 lines from the file right now.

```bash
$ tail /var/log/syslog
[...]
```

The load lines we see follow a similar pattern. First, they include the date and time of when the entry was added to the file, then the name of the computer, then the name and PID of the process that trigger the event and finally, the actual event that's being logged. Take a second and look at those lines. Say that we had a computer that was under significant load but we didn't know why, and to find out we wanted to check what events are being logged the most to our Syslog. To do that we need to extract the part of the line that has the actual event without the date and time. We can use a command called **cut** to help us with that. This command, let's us take only bits of each line using a field delimiter. In this example, we can split the line using spaces. That would look something like this.

```bash
$ tail /var/log/syslog | cut -d' ' -f5-
[...]
```

In our example, we're passing -d' ' to **cut** to tell it that we want to use a space as a delimiter, and -f5- that tell it that we want to print the field number 5 and everything that comes after it. With that, we remove the date and the name of the computer keeping only the process and the event message. Now that we have the information that we care about, we can pipe this to the same pipeline of commands that we saw earlier  to find out the lines that are repeated the most, like this:

```bash
$ cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head
[...]
```

There are more files in var/log that we might be interested in. So we can use a _for loop_ to iterate over each of the log files in var/log and get the most repeated lines in each of them.

```bash
#!/bin/bash
# Script name: toploglines.sh

for logfile in /var/log/*log; do
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
```

#### Choosing Between Bash and Python

As you can probably tell by now, there's a lot of interesting things that we can do with the system commands. We've come across a bunch of different commands that can help us operate with files and processes, and get more information about the computer, process the contents of files, and all sorts of other things. By using bash scripts, we can very quickly turn a command that operates on just one file into an automated script that handles 1,000 files. Pretty powerful, right? As we saw with our log file examples, there's a bunch of terminal commands that provide text processing functionality.

Plenty of them also support regular expressions, allowing us to do some very advanced processing of the data in our files. When these commands are linked together in a data processing pipeline, they can become a powerful tool for processing text data. They can give us information we're looking for quickly about the need to write a full script.

But you know what they say about great power? We need to be careful not to abuse this because it can quickly become unreadable.

Compare:

```bash
$ for i in $(cat story.txt); do B='echo -n "${i:0:1}" | tr "[:lower:]" "[:upper:]"'; echo -n "${B}${i:1} ": done; echo -e "\n"
Once Upon A Time There Was An Egg Of A Programming Language Called Python
```

with:

```python
#!/usr/bin/env python3
# Script name: capitalyze_words.py
import sys

for line in sys.stdin:
  words = line.strip().split()
  print(" ".join([word.capitalize() for word in words]))
```

Once we have the script, we can execute it as part of a pipeline like this:

```bash
$ cat story.txt | ./capitalize_words.py
Once Upon A Time There Was An Egg Of A Programming Language Called Python
```

So it's a good idea to choose bash when we're operating with files and system commands, as long as what we're doing is simple enough that the script is self-explanatory.

As soon as it becomes hard to understand what the script is doing, it's better to write it in a more general scripting language like Python. Bash scripts aren't as flexible or robust as having entire Python language available, with its many functions to operate on strings, lists, and dictionaries.

There's another gotcha when it comes to bash and Linux commands, and it's something that we've said before. Their availability depends on the platform that we're using. Some commands might not be present on certain operating systems. Running a bash script can get the job done very quickly on a Linux machine, but it won't work on a Windows machine. There, we need to write the same script in PowerShell. So if the tasks that you're trying to accomplish is limited to the current server or a fleet of servers, all running the same operating system, a simple bash script can get the job done. But if your code is complex or it needs to work across platforms, you might be better off using the Python standard library or other external modules that provide the same functionality.

Last thing, there are lots of situations where either a bash script or a Python script might solve the problem just fine. In those cases, you can choose whichever one you feel more comfortable with.

### Final Project

Well, here we are. We're finally at the last module of the course. Congratulations on making it all the way here. It's been a long and challenging road and hopefully you're now feeling confident about automating system task through Python. Great work. Along our journey, we've become much more familiar with lots of tools that Python has to offer.

We've learned about managing files and directories, reading and writing both text files and CSV files using regular expressions, understanding how the system interacts to our programs, executing system commands, and writing automated test to name a few. We've even learned a bit about different scripting language called Bash.

#### Writing a Script from the Ground Up

Whenever you're tackling a project that requires coding like writing a small script to automate a single task or writing a large programming project that handles a lot of information, there's a process that we recommend that you follow. We looked at this already in the first course of the program, but let's go over it once again to have it fresh in our minds. Things run much smoother when you remember to check all the boxes.

1. The first step to handle any coding project is to fully understand the **problem statement**. This includes: spelling out what needs to be done and identifying what the given inputs and desired outputs are for that program that we need to write.

2. After that, we recommend doing some **research**. This means figuring out how we can tackle the problem by the tools provided by the Python standard library or by external modules. Remember, we want to avoid reinventing the wheel. No matter how tricky and intricate the challenge appears, chances are that others have solved something similar before. Coding is a bit like Hollywood. There are not that many new ideas, mostly re-imaginings. So it's valuable that we spent some time looking into what resources exist to help us solve our problem. This research phase also includes looking at the documentation of the modules, classes, and functions that we'll need to use, and understanding how they should be applied. A lot of the documentation also includes examples. So it's helpful to absorb those and see how they relate to the code that we need to write.

3. Once we know what we need to write and what tools we can use to make it work, we should do some **planning**. This means thinking about what data types are useful for our solution, the order of operations that we need to perform, and how all the pieces have come together to form our solution. Synergy. If the problem is complex, it might help to write down the plan for quick reference, either on a piece of paper or in a digital document. Writing down the plan helps us focus on how we're going to do things and identify any problems our plan might have. At many companies, it's a common practice to write a design document at this stage, detailing the problem statement, the tools that will be used to solve it, and the plan of attack towards a solution. Having others comment on your design helps make sure that all the twists have been untangled.

4. Finally, once we have a clear plan, we do the actual **writing** of the script. This step includes not only writing the code, but also checking that the code does what it's supposed to do. We do that by both manually testing the code and adding some automatic test. Sometimes, it's tempting to just jump right into the coding stage, about spending any necessary time to fully understand the problem, research tools, or plan the solution. But our experience shows us spending a while getting familiar with what we're trying to do and what tools we have available to do it can make a big difference. Both in how long it takes to do the actual implementation and ultimately how well our solution behaves.

So practice following this process as you dig into the final course project, and then try to apply this to any coding projects that you might tackle in the future.

#### Problem Statement #2

Imagine a scenario, one of the servers used by your company runs a service called Ticky. This service is an internal ticketing system used by a lot of different teams in the company to manage their work. The service logs a bunch of events to syslog, both when it runs successfully and when it encounters errors. Developers of the service are asking for your help with getting some information out of those logs, to better understand how the software is being used and how to improve it.

No sweat. As an up and coming IT Professional, you enthusiastically accept this mission. So for your final project in this course, you'll write some automation scripts that will process the system log and generate a bunch of reports based on the information extracted from log files. The log lines follow a pattern similar to the ones we've seen before. Something like this:

```text
May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)
Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)
```

When the service runs correctly, it logs an info message to syslog, stating what it's done, the username, and the ticket number related to the event. If the service encounters a problem, it logs in error message to the syslog, indicating what was wrong and the username that triggered the action that caused the problem.

The developers of the service want two different reports out of this data.

1. The first one is a ranking of errors generated by the system. This means a list of all error messages logged, and how many times each of them was found, not taking into account the users involved. They should be sorted by the most common error to the least common error.

2. The second one is a usage statistics for the service. This means, a list of all users that have used the system including how many info messages and how many error messages they've generated. This report should be sorted by username.

- To visualize the data in these reports, you want to generate a couple of webpages that'll be served by a web server running on the machine. To do this, you can make use of a script that's already in the system called csv_ to_html.py. This script converts the data in a CSV file into an HTML file containing a table with the data.

- Then, put the files in the directory that's used by the webserver to display the webpages. The goal is to have one script that can get all the necessary work done automatically, every day without any user interaction. This script doesn't need to do all the work itself. It can call on other scripts to do individual task and then put the results together. In fact, we recommend splitting the task so that each piece can be written and tested separately.

I imagine that your mind is racing, your pulse might have spread up a little bit, and your palms are sweating all over the keyboard. Don't worry. This might sound like a lot of work. But once you've understood the problem and done some research and planning, everything will start to fall into place. In our next video, we'll give you some tips on how to start breaking this task down. Here we go.

#### Help with Research and Planning

We've now gone over the problems statement of our final project. At first sight, it might sound pretty complex. But let's break it down into smaller more digestible pieces and discuss how we can move into the next steps to do the necessary research and planning.

We've said that we want to find some specific log lines in the syslog file. We strongly recommend that you use regular expressions to find them. It'll be easier to extract information you want that way. To figure out the right regular expression, you can use a website like [regex101.com](https://regex101.com) which can help you test your expression and understand what's going on with it. Once you have a pattern that you think and work, try it out in a Python interpreter to verify that it matches the right lines and captures the right information.

After extracting the information, you'll need to count how many errors are of the same type, and how many info and error messages there are for a given user. Can you think of what data structure might help you with that? If you're thinking dictionaries, then you're on the right track. You'll want to use a couple of different dictionaries. One to account error messages and another to count per user usage. You'll then need to sort the data in a dictionary's by different criteria. We looked at sorting in the Introduction to Python course. Feel free to re-watch that video and reread the Python documentation on sorting.

The output of your Python script should be a couple of CSV files. Each of them containing the names of the columns and the data in the order that it needs to be presented. Once those files are generated, you'll need to call the csv_to_html.py script to create HTML files based on CSV data. You'll have access to look at how the script works but the key is to pass two parameters to it. The name of the CSV file to read and the name of the HTML file generate. You could do this last step from either a Python script or a bash script. Since the script will be only calling commands and moving files, we recommend doing a bash. Keep it short and sweet.

We recommend that you research, plan and even write the pieces of code all before starting the actual lab. Good luck. You've got it!

## Introduction to Git and GitHub

### Before Version Control

#### Module Introduction

When you work in IT, you manage information across a lot of different files:

- You write automation scripts that might evolve over time. For example, you might add new features to your script or take into account additional conditions or modify the scope of systems where the script will be executed.

- You also manage configuration related to your infrastructure like the default settings on an application or the IP addresses assigned to the computers in your fleet, etc.

This information changes over time as the security requirements increase. The fleet grows or new versions of software gets deployed.

When trying to manage change in IT, it's super important to have detailed historical information for your organization's configuration files and automation code. This let's the administrators see what was modified and when, which can be critical to troubleshooting. It also provides a documentation trail that will let future IT specialists know why the infrastructure is the way it is, and it provides a mechanism for undoing a change completely. This way, we don't have to undo changes from memory and there's less chance of human error. We'll see this in action when we talk about rollbacks.

Imagine this, your team has added a new feature to a script that checks the health of all the computers that you're responsible for. The new check verifies that the firmware of the computer, also known as the UEFI, is updated to the latest version. When you roll this out, you suddenly realize that half the computers now say they're broken. After some investigation, you discover that the check needs to take into account different computer models.

You might be tempted to do a quick code fix, push it to the affected machines right away especially if it seems like an easy fix. But more often than not, quick fixes include their own bugs because we don't take the time to test a new code properly. So after the first fix, you might end up doing a second or even third emergency push until things are really working correctly. To avoid these headaches, you can use a version control system to easily roll back your code to the previous version. Since you know that this version was working correctly before the change was made, it would be safe to go back to that one until you had time to fix the code, run some tests, and make sure everything works correctly for all machine models.

By releasing code only after properly testing, you avoid having to push quick-fix after quick-fix. Version control systems let us do this and much more. They are crucial to maintaining a healthy codebase for all kinds of IT resources, and for letting multiple people collaborate on the same coding projects together.

We're now going to take our first steps to learning this new tool, which will let us keep track of the changes that we make to our scripts, our configuration files, and any other kind of documents that need to be tracked.

We'll start by looking at what people tend to do when they don't know about version control and then check out some related tools, like **diff** and **patch**.

Once we have a clear idea of why we need proper version control, we'll jump into our first **Git** experience. We'll talk about what **Git** is and how it does what it does.

To follow along, you'll need to install Git locally on your machine and learn how to use it from the command line. If this sounds a bit scary, don't panic. We'll guide you along the way and you'll be using it in no time. Once you have Git installed in your computer, we'll do an overview of the basic Git workflow which will let you start keeping track of your scripts.

#### Keeping Historical Copies

The principle behind version control is the following one: it lets us keep track of the changes in our files. These files can be _code_, _images_, _configuration_, or even a _video editing project_, _whatever_ it is you're working with. Throughout this course, we'll see the many ways that **Git** helps us keep track of our changes, and also how we can use it to collaborate with others or avert changes. We'll use a bunch of terms that have special meanings in the world of version control, but don't let those intimidate you. In the end, all we're doing is having better control over our historical copies. So, say you have two copies of the same code made at different points in time. How can you compare them?

#### Diffing Files

Imagine you had two copies of some code, and you wanted to see what the difference was between them. How would you do it? You could open both files in the editor side by side, look at one then look at the other to spot the differences, but that's super error-prone. We're human and by comparing with our eyes we are bound to miss some differences. Fortunately, there's a better way. You can use some nifty tools that will do this automatically. We can use the diff command line tool to take two files or even to directories, and show the differences between them in a few formats.

Let's say we have two files rearrange 1.py and rearrange 2.py which contain two different versions of the same function. We could take a look at them using **cat**. Could you spot the difference? Maybe you can but it's not super obvious. Let's use the **diff** command so that we don't have to
strain our eyes trying to spot it.

When we call the diff command, we get only the lines that are different between two files. It's much easier to find the difference when we just have two lines.

When differences or changes are less so obvious or common, we can use the **diff -u** flag to tell diff to show the differences in another format. This _unified format_ is pretty different from the one that we saw before. It shows the change lines together with some context, using the minus sign to mark lines that were removed, and the plus sign to mark lines that were added. The extra context let's us better know what's going on with the change that we're diffing.

#### Applying Changes

Imagine a colleague sends you a script with a bug and asked you to help fix the issue. Once you understood what was wrong with the script, you could describe to them what they need to change. Something like, _"Well, you can only return values inside functions. I think you meant to use sys.exit instead. Also, you're converting to gigabytes twice, so your script will always fail."_

But this could still be hard for them to understand if the code is complex. To make the change clear, you could send them a diff with the change so that they can see what the modified code looks like. To do this, we typically use a command line like:

```bash
diff-u old_file new_ file > change.diff.
```

As a reminder, the greater than sign redirects the output of the diff command to a file. So with this command, we're generating a file called change.diff with the contents of diff-u command. By using the -u flag, we include more context which helps the person reading the file understand what's going on with the change. The generated file is usually referred to as a **diff file** or sometimes a **patch file**. It includes all the changes between the old file and the new one, plus the additional context needed to understand the changes and to apply those changes back to the original file.

Now, say you're the one receiving a diff file with a change and you want to apply it to a script you wrote. You could read the diff file you receive carefully and then manually go through the file that needs to be changed, and apply the modifications. But it sounds like a lot of manual work that could be automated, don't you think? Well, it sure is.

There's a command called patch to do exactly this. Patch takes a file generated by diff and applies the changes to the original file. Let's check this out in an example. Say we have a small script that checks whether the computer is under too much load, like this one.

```python
#!/usr/bin/env python3

import psutil

def check_cpu_usage(percent):
  usage = psutil.cpu_percent()
  return usage < percent

if not check_cpu_usage(75):
  print("ERROR! CPU is overloaded")
else:
  print("Everything ok")
```

This script uses the psutil module to check the percentage of the CPU that's currently in use. When the load is above a threshold, in this case 75 percent, it prints a message with an error. When it's under the threshold, it says that everything's okay.

Now, we've shared this script with a few colleagues and one of them tells us that the script doesn't work correctly. Even if a computer is completely overloaded, the script will say that everything's okay. Our colleague is so helpful that they sent us a diff with the fix for our problem. Let's check that one out.

```bash
--- cpu_usage.py        2023-01-17 18:19:26.000000000 +0100
+++ cpu_usage2.py       2023-01-17 18:21:20.000000000 +0100
@@ -3,7 +3,8 @@
 import psutil

 def check_cpu_usage(percent):
-  usage = psutil.cpu_percent()
+  usage = psutil.cpu_percent(1)
+  print("DEBUG: usage: {}".format(usage))
   return usage < percent

 if not check_cpu_usage(75):
```

We can see that our colleague made two changes. They added a one as a parameter to the CPU percent function and they added a debugging line, that prints the value returned by the function. Our colleague explains that by calling the CPU percent function without a parameter, we were not averaging over a period of time, and so the call always returns zero.

So we have the diff file and we want to apply it to our script. How do we do that? We'll use the **patch** command. We'll pass the name of the file that we want to patch in this case, cpu_usage.py, as the first parameter to the command and then we'll provide the diff file through standard input. Let's check this out:

```bash
$ patch cpu_usage.py < cpu_usage.diff
patching file cpu_usage.py
```

So we told patch to apply the changes that come from cpu_usage.diff to our cpu_usage.py file. We get one single line that says the file was patched, which means that we've successfully applied the changes. Let's verify that by looking at the contents of our script. Nice. We see that our file was modified with the changes that we got from our colleague. The CPU percent function is being called with a parameter of one and the debugging line is printed. Once we're happy with the script, we could remove the debugging line. But for now, we'll leave it in there.

You might be wondering, why go through all this trouble diffing, and patching, and not just send the whole file instead? There are a few reasons for this?

- The main reason is that the original code could have changed. In our example, it's possible that the code our colleague was using to prepare the fix wasn't the latest version. By using a diff instead of the whole file, we can clearly see what they changed, no matter which version they were using. The **patch** command can detect that there were changes made to the file and will do its best to apply the diff anyways. It won't always succeed but in many cases it will.

- Another reason is structure. In this case we're patching a single small file. But sometimes, you might be modifying a bunch of large files inside of a huge project. Say you are changing four files in a project tree that contain 100 different files, arranged in different directories according to what they do. If you were to send the whole files, you'd need to specify where those files were supposed to be placed. As we called out,_** we can diff whole directory structures and in that case the diff file can specify where each change file should be without us having to do any manual juggling**_. Cool right? Okay, great work. We've now seen how to generate diff files and how to apply their contents with the patch command.

#### Practical Application of diff and patch

Imagine this, a colleague is asking our help with fixing a script named disk_usage.py.

```python
#!/usr/bin/env python3

import shutil

def check_disk_usage(disk, min_absolute, min_percent):
    "Returns True if there is enough free disk space, False otherwise"
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = du.free / du.total * 100
    # Calculate how many free gigabytes are left
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


# Check for at least 2 GB and 10% free space
if not check_disk_usage("/", 2*2**30, 10):
    print("ERROR: Not enough disk space")
    return 1
print("Everything ok")
return 0
```

The goal of the script is to check how much disk space is currently used, and print an error if it's too little space for normal operation. But the script is currently broken because it has a few bugs. We’ll help our colleague fix those bugs to demonstrate how to use diff and patch. Before we change anything, let’s make a couple copies of the script. We'll add \_original to one copy, which we’ll keep unmodified and use for comparison and \_fixed to the other copy, which we’ll use to repair our fix.

```bash
$ cp disk_usage.py disk_usage_orginal.py
...
$ cp disk_usage.py disk_usage_fixed.py
```

Okay, now that we have our copies, we'll edit the _fixed version and actually fix it. This file has a bunch of code. Before we try to understand what it does and what's wrong with it, let's execute it and see what we get.

```bash
$ ./disk_usage.py
File "disk_usage.py", line 20
    return 1
    ^^^^^^^^
SyntaxError: 'return' outside function
```

The Python interpreter isn't too happy. It's complaining that there's a return outside of function. And if we look at the code, we can clearly see that there's a return that's not inside any function.

You might remember that in Python, we can only use return statements inside functions. So how do we fix this? There's a couple options. We could turn the current code into a function and then call that function from the main part of our script. Or we could use sys.exit to make the return number of the exit code of our script, which is the code that causes a program to exit with the corresponding exit value. For now, let's go with the second option.

Okay, we've made the change. Let's execute this new version of our script.

```bash
$ ./disk_usage.py
ERROR: Not enough disk space
```

Darn, we fixed the syntax error, but now the script is telling us we don't have enough space on our disk. But we know that we actually do have some free space, right? What's up with that?

If you look closely at the code, you might notice that the script is converting to gigabytes twice. The function call to check_disk_usage is passing 2 times 2 double star 30. You might remember that the double star operator is used to calculate powers. In this case, 2 to the power of 30, which is how many bytes are in a gigabyte. So, this would be 2 gigabytes, but that be if the check_disk_usage function was expecting a value in bytes. If we look at the code of the function, we can see that it's already dividing the amount of free bytes by 2 to the power of 30. So in other words, we're doing the gigabyte conversion twice. Once when calling the function and once inside the function. We need to get rid of one of them. Let's change how we call the function.

Okay, let's try it out again.

```bash
$ ./disk_usage.py
Everything ok
```

It works now. Okay, now we need to send a fixed to our colleague so that they can fix their script. To do that, we'll use a technique we just learned to generate a diff file, like this:

```bash
$ diff -u check_usage_orginal.py check_usage_fixed > check_usage.diff
...
$ cat check_usage.diff # just to check
--- disk_usage_original.py      2023-01-18 12:08:03.000000000 +0100
+++ disk_usage_fixed.py 2023-01-18 15:06:46.000000000 +0100
@@ -15,8 +15,11 @@


 # Check for at least 2 GB and 10% free space
-if not check_disk_usage("/", 2*2**30, 10):
+if not check_disk_usage("/", 2, 10):
     print("ERROR: Not enough disk space")
-    return 1
+    sys.exit(1)
 print("Everything ok")
-return 0
+sys.exit(0)
```

Awesome. This seems to have what we want. So this is what we need to send to our colleague to have them patch their file. How would they do that? They would run the patch command like this.

```bash
$ patch disk_usage.py < disk_usage.diff
patching file disk_usage.py
```

By calling patch with the diff file, we've applied the changes that were necessary to fix the bugs.

So we've now seen how we can look at differences between files, generate diff files together to gather our changes, and then apply those changes using patch. But this is still a very manual process, where version control systems can really help.

### Version Control Systems

#### What is version control?

We've seen up till now, how we can use existing tools to extract differences between versions of files and apply those changes back to the original files. Those tools are really useful. But most of the time, we won't be using them directly. Instead, we'll use them through a Version Control System, or VCS.

_A Version Control System keeps track of the changes that we make to our files_. By using a VCS, we can know when the changes were made and who made them. It also lets us easily revert a change if it turned out not to be a good idea. It makes collaboration easier by allowing us to merge changes from lots of different sources.

At first-look, a Version Control System can seem like a complicated, possibly intimidating tool. But if you look closer, you'll see that it's really just a system that stores files. However, unlike a regular file server which only saves the most recent version of a file, a VCS keeps track of all the different versions that we create as we save our changes. There are many different version control systems, each with their own implementation and with their own advantages and disadvantages. But, no matter how the VCS is implemented internally, they always access the history of our files. Let us retrieve past versions of the file or directory and see who changed which files, how each file was changed and when the file was changed. On top of this, we can make edits to multiple files and treat that collection of edits as a single change which is commonly known as a, **commit**.

A VCS even provides a mechanism to allow the author of a commit to record why the change was made, including what bugs, tickets or issues were fixed by the change. _This information can be a lifesaver when trying to understand a complex series of changes, or to debug some obscure issue. So, be sure to record this extra info in your commits to be truly committed to better code._

In any organization that produces software, a VCS is a key part of managing the code. Files are usually organized in **repositories** which contains separate software projects or just group all related code. If there's a lot of people involved in developing software, some developers may have access to only some of the repositories. A single **repository** can have as little as one person using it. And it can go up to thousands of contributors.

And, as we called that earlier, a Version Control System can be used to store much more than just code. We can use it to store configuration files, documentation, data files, or any other content that we may need to track. Because of the way tools like diff and patch work, a VCS is especially useful when tracking text files, which can be compared with diff and modified with patch. We can also store images, videos or any other complex file formats in a VCS, but, it won't be easy to check the differences between versions when comparing these file formats.

#### Version Control and Automation

At first glance, using a VCS might seem like a lot of work for an IT specialist to set up and learn. It might especially seem like overkill, if you're the only member of your IT team that writes code or maybe even the only member period. So can a VCS help, even if you don't need to share your scripts or collaborate on them with others?

The short answer is yes. A VCS can be invaluable, even in a one-person IT department. A VCS stores your code and configuration. It also stores the history of that code and configuration. A version control system can function a lot like a time machine, giving you insights into the decisions of the past. Whenever you write a commit message, after making a change, it's as if the current version of yourself is explaining your decisions to a future you or others who might work on the same scripts and configurations in the future. This can help you avoid finding yourself staring at a piece of code that you or someone else wrote three months ago and puzzling over how it works or even why it exists. With a VCS, you can view, track and select snapshots from the history of your project. So nothing you do is lost, and since we can use a VCS to store both code and configuration files, we can make the overall IT systems more scalable and reliable.

This functionality enhances the reliability of systems you operate. Because of the audit trail provided by the VCS, you know exactly what version of the zone file to rollback to, which reduces the time it takes to fix the problem. It's generally better to quickly roll back first and stop errors before spending time figuring out what went wrong. You can curb the fix after the bleeding has stopped. Figuring out the bug might take up valuable time or worse, your first attempt at a solution can have its own bugs.

#### What is Git?

Git is a VCS created in 2005 by Linus Torvalds. The developer who started the Linux kernel.

Git is a free open source system available for installation on Unix based platforms, Windows and macOS. Linus originally created get to help manage the task of developing the Linux kernel. This was difficult because a lot of geographically distributed programmers were collaborating to write a whole bunch of code. Linus had some requirements for the way that the system worked, and its performance that weren't being met by the VCS tools at a time. So he decided to write his own. Git is now one of the most popular version control systems out there and is used in millions of projects. Unlike some version control systems that are centralized around a single server, Git has a distributed architecture. This means that every person contributing to a repository has full copy of the repository on their own development machines.

Collaborators can share and pull in changes that others have made as they need. And because the repositories are all local to the computer being used to create the files, most operations can be done really fast. If you want to collaborate with others, it usually makes sense to set up a repository on a server to act as a kind of hub for everyone to interact with. But Git doesn't rely on any kind of centralized server to provide control organizations to its workflow. Git can work as a standalone program as a server and as a client. This means that you can use Git on a single machine without even having a network connection. Or you can use it as a server on a machine where you want to host your repository. And then you can use Git as a client to access the repository from another machine or even the same one. Git clients can communicate with Git servers over the network using HTTP, SSH or Git's own special protocol.

So you can use Git with or without a network connection. You can use it for small projects with like one developer or huge projects with thousands of contributors. You can use it to track private work that you can keep to yourself or you can share your work with others by hosting a code on public servers like Github, Gitlab or others.

As with most things in the IT world, though, there are plenty of other tools that can be used to accomplish the same task. There are other VCS programs like Subversion or Mercurial. Feel free to experiment with alternatives if you think another VCS might better serve your needs.

#### More Information About Git

Check out the following links for more information:

- [https://git-scm.com/doc](https://git-scm.com/doc)

- [https://www.mercurial-scm.org/](https://www.mercurial-scm.org/)

- [https://subversion.apache.org/](https://subversion.apache.org/)

- [https://en.wikipedia.org/wiki/Version_control](https://en.wikipedia.org/wiki/Version_control)

#### Installing Git

The first step on the way to using Git is to install it! The directions found in the Git documentation below are pretty thorough and helpful, check them out for the best method of getting Git onto your platform of choice.

- [Git download page](https://git-scm.com/downloads)

- [Git installation instructions for each platform](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Using Git

#### First Steps with Git

When starting with Git, there are a bunch of concepts that we need to learn to understand how things are organized and how our files are tracked.

Let's start by setting some basic configuration. Remember when we said that a VCS tracks who made which changes, for this to work, we need to tell Git who we are. We can do this by using the **git config** command and then setting the values of user.email and user.name to our email and our name like this:

```bash
git config --global user.email "me@example.com"
git config --global user.name "My Name"
```

With that done, there are two ways to start working with a git repository. We can create one from scratch using the **git ini**t command or we can use the **git clone** command to make a copy of a repository that already exists somewhere else. We'll talk about remote repositories later in the course. For now, let's start by creating a new directory and then a git repository inside that directory.

```bash
mkdir checks
cd checks
git init
Initialized empty Git repository in ~/checks/.git/
```

So when we run **git init** we initialize an empty git repository in the current directory. The message that we get mentions a directory called. git. We can check that this directory exist using the **ls -la** command which lists files that start with a dot. We can also use the **ls -l .git** command to look inside of it and see the many different things it contains. This is called a _Git directory_.

```bash
ls -l .git
Total 24
-rw-r--r--   1 user  staff   23 20 jan 17:16 HEAD
-rw-r--r--   1 user  staff  137 20 jan 17:16 config
-rw-r--r--   1 user  staff   73 20 jan 17:16 description
drwxr-xr-x  15 user  staff  480 20 jan 17:16 hooks
drwxr-xr-x   3 user  staff   96 20 jan 17:16 info
drwxr-xr-x   4 user  staff  128 20 jan 17:16 objects
drwxr-xr-x   4 user  staff  128 20 jan 17:16 refs
```

> _If you've already run git init on a project directory containing a .git subdirectory, you can safely run git init again on the same project directory. The operation is what we call **idempotent**; running it again doesn't override an existing .git configuration._

You can think of it as a database for your Git project that stores the changes and the change history. We can see it contains a bunch of different files and directories. We won't touch any of these files directly, we'll always interact with them through Git commands. So whenever you clone a repository, this git directory is copied to your computer. Whenever you run git init to create a new repository like we just did, a new git directory is initialized.

The area outside the git directory is the _**working tree**_. The _**working tree**_ is the current version of your project. You can think of it like a workbench or a sandbox where you perform all the modification you want to your file. This working tree will contain all the files that are currently tracked by Git and any new files that we haven't yet added to the list of track files.

Right now our working tree is empty. Let's change that by copying the disk usage that pyfile that we created earlier into our current directory.

```bash
cp ../disk_usage.py .
```

We now have file and a working tree but it's currently untracked by Git. To make Git track our file, we'll add it to the project using the **git add** command passing the file that we want as a parameter. With that, we've added our file to the _**staging area**_.

The staging area which is also known as the _**index**_ is a file maintained by Git that contains all of the information about what files and changes are going to go into your next command.

We can use the **git status** command to get some information about the current working tree and pending changes.

To get our file committed into the.git directory, we run the **git commit** command.

When we run this command, we tell Git that we want to save our changes. It opens a text editor where we can enter a commit message. The texts that we get tells us that we need to write a commit message and that the change to be committed is the new file that we've added. For now, let's enter a simple description of what we did which was to add this one file and then exit the editor saving our commit message and with that we've created our first git commit.

#### Tracking Files

In the previous section, we mentioned that any Git project will consist of three sections: the Git directory, the working tree and the staging area.

- The _**Git directory**_ contains the history of all the files and changes.

- The _**working tree**_ contains the current state of the project, including any changes that we've made.

- And _**the staging area**_ contains the changes that have been marked to be included in the next commit.

This can still be confusing. So it might be helpful to think about Git as representing your project. Which is the code and associated files and a series of snapshots.

Each time you make a commit, Git records a new snapshot of the state of your project at that moment. It's a picture of exactly how all these files looked at a certain moment in time. Combined, these snapshots make up the history of your project, and it's information that gets stored in the Git directory. Now, let's dive into the details of how we track changes to our files.

When we operate with Git, our files can be either _**tracked**_ or _**untracked**_. Tracked files are part of the snapshots, while untracked files aren't a part of snapshots yet. This is the usual case for new files.

Each tracked  file can be in one of three main states: _**modified**_, _**staged**_ or _**committed**_. Let's look at what each of these mean.

- If a file is in the modified state, it means that we've made changes to it that we haven't committed yet. The changes could be adding, modifying or deleting the contents of the file. Git notices anytime we modify our files. But won't store any changes until we add them to the staging area.

- So, the next step is to stage those changes. When we do this, our modified files become staged files. In other words, the changes to those files are ready to be committed to the project. All files that are staged will be part of the next snapshot we take.

- And finally, when a file gets committed, the changes made to it are safely stored in a snapshot in the Git directory.
This means that typically a file tracked by Git, will first be modified when we change it in any way. Then it becomes staged when we mark those changes for tracking. And finally it will get committed when we store those changes in the VCS.

So to sum up, we work on modified files in our working tree. When they're ready, we staged these files by adding them to the staging area. Finally, we commit the changes sitting in our staging area, which takes a snapshot of those files and stores them in the database that lives in the Git directory. If the way Git works is not totally clear yet, don't worry. It will all sink in with a bit more practice.

#### The Basic Git Workflow

We discussed earlier some of the basic concepts involved in working with **Git**. We saw that each repository will have a _**Git directory**_, a_** working tree**_, and a _**staging area**_. And we called out that files can be in three different states, modified, staged, and committed. Let's review these concepts one more time by looking at the normal workflow when operating with Git on a day to day basis.

- First, all the files we want to manage with Git must be a part of a Git repository. We initialize a new repository by running the git init command in any file system directory. For example, let's use the mkdir command to create a directory called scripts, and then change into it and initialize an empty Git repository init.

```bash
mkdir scripts
cd scripts
git init
```

Our shiny new Git repository can now be used to track changes to files inside of it. But before jumping into that, let's check out our current configuration by using the **git config -l** command. There's a bunch of info in there, and we won't cover all of it. For now, pay special attention to the _user.email_ and the _user.name_ lines, which we touched on briefly in an earlier video. This information will appear in public commit logs if you use a shared repository. For privacy reasons, you might want to use different identities when dealing with your private work and when submitting code to public repositories. We'll include more details about changing this information in our next reading.

Okay, our repo is ready to work, but it's currently empty. Let's create a file in it, we'll start with a basic skeleton for a Python script, which will help us demonstrate the Git workflow. As with any Python script, we'll start with the shebang line. For now, we'll add an empty main function, which we'll fill in later. And at the end, we'll just call this main function.

```python
#!/usr/bin/env python3
def main():
  pass

main()
```

All right, we've created our file. This is a script that we'll want to execute, so let's make it executable. And then let's check the status of our repo using **git status** command.

  ```bash
  git status
  ```

- As we called out before, when we create a new file in a repository, it starts off as untracked. We can make all kinds of changes to the file, but until we tell Git to track it, Git won't do anything with an untracked file. We need to call the **git add** command. This command will immediately move a new file from untracked to stage status. And as we'll see later, it will also change a file in the modified state to staged state. Remember that when a file is staged, it means it's been added to the staging area and it's ready to be committed to the Git repository.

- To initiate a commit of staged files, we issue the **git commit** command. When we do this, Git will only commit the changes that have been added to the staging area, untracked files or modified files that weren't staged will be ignored. Calling git commit with no parameters will launch a text editor, this will open whatever has been set as your default editor. If the default editor is not the one you'd like to use, there are a bunch of ways to change it. For now, let's edit our message with Nano, which is the current default for this computer. We'll say that our change is creating an empty all_checks.py file, then save and exit.

Voila! We've just recorded a snapshot of the code in our project, which is stored in the Git directory. Remember that every time we commit changes, we take another snapshot, which is annotated with a commit message that we can review later.

- Okay, that's how we add new files, but usually we'll modify existing ones. So let's add a bit more content to our script to see that in action. We'll add a function called check_reboot, that will check if the computer is pending a reboot. To do that, we'll check if the run/reboot-required file exists. This is a file that's created on our computer when some software requires a reboot. And of course, since we're using os.path.exists, we need to add import os to our script.

```python
#!/usr/bin/env python3
import os

def check_reboot():
  "Returns True if the computer has a pendign reboot"
  return os.path.exists("/run/reboot-required")

def main():
  pass

main()
```

- All right, we've added a function to our file. Let's check the current status using **git status** again. Our file's _modified_, but not _staged_. To stage our changes, we need to call **git add** once again.

- Okay, our changes our now staged. We have to call **git commit** to store those changes to the Git directory. This time, we'll use the other way of setting the commit message. We'll call **git commit -m**, and then pass the commit message that we want to use. So in this case, we'll say that we've added the check_reboot function.

With that, we've demonstrated the basic Git workflow. We make changes to our files, stage them with git add, and commit them with git commit. If there's anything that's not totally clear yet, remember, that the only way to get familiar with these concepts is practice.

#### Anatomy of a Commit Message

Earlier, we saw how we can commit snapshots of changes to the Git repository. Let's now talk a little bit more about what makes a good commit message.

Writing a clear informative commit message is important when you use a VCS, future you or other developers or IT specialists who might read the commit message later on will really appreciate the contextual information as they try and figure out some of the parts of the code or configuration.

So what makes a good commit message? It can be helpful to keep your audience in mind when you write commit messages. What would someone reading a message weeks or months from now want to know about the changes you've made?

- What might be especially important or tricky to understand about them?

- Is there extra information that might help the reader out, like links to design documents or tickets in your ticketing system?

Similarly to how style guides exist for writing code, your company might have specific rules for you to follow when you write commit messages. Even if they don't, it's good to use a few general guidelines to make sure your commit messages are as clear and useful as possible.

A commit message is generally broken up into a few sections.

- The first line is a short summary of the commit followed by a blank line.

- This is followed by a full description of the changes which details why they're necessary and anything that might be especially interesting about them or difficult to understand. When you run the git commit command, Git will open up a text editor of your choice so you can write your commit message. A good commit message might look something like this.

So the first line is usually kept to about 50 characters or less. The line contains a short description of what the commit changes are about. After the first line, comes an empty line, and the rest of the text is usually kept under 72 characters. This text is intended to provide a detailed explanation of what's going on with the change. It can reference bugs or issues that will be fixed with the change. It can also include links to more information when relevant. The line limits can be annoying but they help in making the commit message be more digestible for the reader.

There's a git command used to display these commit messages called **git log**. This command will do any line wrapping for us. Which means that if we don't stick to the recommended line wrapping, long commit messages will run off the edge of the screen and be difficult to read.

Sometimes it can be tempting to just write something short like update, change or fix as the description of our commit messages. Don't do it. It's super frustrating to go back to repositories history and discover that there's not enough context to understand what was changed and why. It takes only a few more seconds to write a better description. This can be invaluable down the line.

Following these guidelines can help make your commit message really useful, and the investment of work now will really pay off later. If you're interested in learning more about git commit style, there are plenty of resources out there to read including the Linux kernel documentation itself along with impassioned opinions from other developers.

#### Initial Git Cheat Sheet

Check out the following links for more information:

The [Linux kernel documentation](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/process/submitting-patches.rst?id=HEAD) itself, as well as [impassioned](http://stopwritingramblingcommitmessages.com/) opinions from [other developers](https://robots.thoughtbot.com/5-useful-tips-for-a-better-commit-message).

You can check out [Setting your email in Git](https://help.github.com/articles/setting-your-email-in-git/) and [Keeping your email address private](https://help.github.com/articles/keeping-your-email-address-private/) on the GitHub help site for how to do this.

### Using Git Locally

Up till now, we've talked about what version control is, why it's necessary, and how we might benefit from it in diverse context. We also started learning some basic Git commands, and procedures, nice job!

Over the course of the next sections, we'll go into much more detail about what we can do with Git. These are Git's greatest hits:

- We'll start by learning some handy shortcuts and looking into how we can get more info out of our version control system.

- Then we'll experience the true power of Git by seeing how we can undo some of our changes. The ability to revert previous changes is one of the most useful aspects of version control systems. Depending on what needs to be undone, there's a bunch of different techniques that we can use in Git. We can discard the changes made to a file, fix a commit that was incorrect and even roll back our project to an older snapshot. We'll look into all these techniques and dive into when to use each of them.

- Finally, we'll check out yet another important concept, Branches. We can use branches to work on an experimental feature without affecting the main code of our project. Support separate versions of a program that can't be merged together and much more. We'll dive into what branches are, when and how to use them and how to deal with merge conflicts.

#### Advanced Git Operations

When we covered the basic Git workflow, we called out that the process is usually to make changes, stage them, and then commit them. The separate step between staging and committing allows us to stage several changes in one commit.

But if we already know that the current changes are the ones that we want to commit, we can skip the staging step and go directly to the commit. No dress rehearsals. We do this by using the **-a flag** to the **git commit** command. This flag automatically stages every file that's tracked and modified before doing the commit letting it skip the git add step.

At first, you might think that git commit dash a is just a shortcut for git add followed by git commit but that's not exactly true. Git commit -a doesn't work on new files because those are untracked. Instead, git commit -a is a shortcut to stage any changes to tracked files and commit them in one step. If the modified file has never been committed to the repo, we'll still need to use git add to track it first.

So let's make a change to our example script from an earlier video and try out this new flag. We'll now modify our main function and make it call the check reboot function that we wrote before. If a reboot is pending, we'll print a message and then exit our program with an exit status of one. Since we're using the sys module, we'll need to import it. All right. Now that we've made the change, we're ready to try out the new -a flag. We'll also use the -m flag to add the commit message directly. This time, we'll say that we're calling check underscore reboot and exiting with one on the error condition.

These shortcuts are useful when making small changes that we know we'll want to commit directly without keeping them in the staging area and having to write long and complex descriptions. Keep in mind that when you use the -m shortcut, you can only write short messages and can't use the best practices regarding commit descriptions that we talked about earlier. So it's best reserved for truly small changes that don't require extra context or explanation, short and sweet.

Heads up, when you use the -a shortcut, you skip the staging area, meaning, you can't add any other changes before creating the commit. So you need to be sure that you've already included everything you want to include in that commit.

In the end, using a shortcut like -a is just like using the regular commit workflow. The commit will show up in the log along with the message just as usual. Let's check that out. See how our latest commit was added to the top of the list of commits and notice how the head indicator has now moved to the latest commit.

You might be wondering, what is this _**HEAD**_ and where is it heading? We'll keep coming across it. So let's clarify. Git uses the head alias to represent the currently checked out snapshot of your project. This lets you know what the contents of your working directory should be. In this case, the current snapshot is the latest commit in the project. We'll soon learn about branches. In that case, head can be a commit in a different branch of the project. We can even use git to go back in time and have head representing old commit from before the latest changes were applied. _**In all cases, HEAD is used to indicate what the currently checked out snapshot is**_. This is how git marks your place in the project. Think about it as a bookmark that you can use to keep track of where you are. Even if you have multiple books to read, the bookmark allows you to pick up right where you left off. When you run git commands like diff, branch, or status, git will use the head bookmark as a basis for whatever operation it's performing. We'll see Head used when we learn how to undo things and perform rollbacks. As a shortcut, it's generally easy to think of head as a pointer to the current branch, although it can be more powerful than that.

#### Getting More Information About Our Changes

We've seen how **git log** shows us the list of commits made in the current Git repository. By default, it prints the commit message, the author, and the date of the change. This is useful, but if we're combing through a history of changes in a repo to try and find what caused the latest outage, we'll probably also need to look at the actual lines that changed in each commit.

To do this with git log, we can use the **-p flag**. The p comes from patch, because using this flag gives us the patch that was created. Let's try it out. The format is equivalent to the diff-u output that we saw on an earlier video. It shows added lines with plusses and remove lines with dashes. Because the amount of text is now longer than what fits on your screen, Git automatically uses a paging tool that allows us to scroll using page up, page down, and the arrow keys. We still have one commit below the other, but now each commit takes up a different amount of space, depending on how many lines were added or removed in that commit. Using this option, we can quickly see what changes were made to the files in our repository. This can be especially useful if we're trying to track down a change that recently broke our tools.

If we don't want to scroll down until we find the commit that we're actually interested in, another option is to use the **git show** command. This command takes a _commit ID as a parameter_, and will display the information about the commit and the associated patch. We'll talk more about commit IDs in a later video. But for now, remember that this is an identifier that we see next to the word commit in the log. Let's check this out by first listing the current commits in the repo and then calling git show for the second commit in the list. First, I'm going to exit out by pressing q. We've shown how we can use git log for listing commits, and git log -p for showing the associated patches.

Another interesting flag for git log is the **--stat flag**. This will cause git log to show some stats about the changes in the commit, like which files were changed and how many lines were added or removed. Let's try it with our repo. There are a bunch of other options to git log, so we won't cover them all. You can always use the reference documentation or the manual pages to find out more. And as we called up before, _you don't need to memorize any of this, you'll learn the different commands and flags by using them. The important thing to remember is that all the information is stored in the repository and you have it at your fingertips when you need it._ You're welcome.

Now, what about changes that haven't been committed yet? Until now, whenever we've made changes to our files, we've either added them to the staging area with git add and committed them with git commit, or committed them directly using git commit -a. This works fine, but it means we have to know exactly which changes we've made.

Sometimes it can take a while until we're ready to commit. We call these commitment issues. Just kidding. But imagine you've been working on adding a new complex feature to a script and it requires thorough testing. Before committing it, you need to make sure that it works correctly. Check that all the test cases are covered and so on and so on. So while doing this you find bugs in your code that you need to fix. It's only natural that by the time you get to the commit step you don't really remember everything you changed. To help us keep track git gives us the **git diff** command.

Let's make a new change to our all_checkcs.py script and then try this command out. We'll add another message to the user to say that everything is okay when the check is successful and then exit with 0 instead of 1.

Okay, we've made the change. Let's now save it and check out what git diff shows us. Again, this format is equivalent to the **diff -u** output that we saw earlier. In this case, we see that the only change is the extra lines that we've added. If our change was bigger and included several files, we could pass a file by parameter to see the differences relevant to that specific file instead of all the files at the same time.

Something else we can do to review changes before adding them is to use the **-p flag** with the **git add** command. When we use this flag, git will show us the change being added and ask us if we want to stage it or not. This way we can detect if there's any changes that we don't want to commit.

 Let's try that one out. We've staged our change and it's now ready to be committed. If we call git diff again, it won't show any differences, since git diff shows only unstaged changes by default. Instead, we can call **git diff --staged** to see the changes that are staged but not committed. With this command, we can see the actual stage changes before we call **git commit**. Let's commit these changes now so that they aren't pending anymore. We'll say that we've added a message when everything's okay.

Nice, and with that, we've learned a bunch of different ways to get more information about our changes.

#### Deleting and Renaming Files

Let's say that you've decided to clean up some old scripts and want to remove them from your repository. Or you've done some refactoring, which makes that particular file, obsolete. You can remove files from your repository with the **git rm** command, which will stop the file from being tracked by git and remove it from the git directory.

File removals go through the same general workflow that we've seen. So you'll need to write a commit message as to why you've deleted them.

What if you have a file that isn't accurately named? This can happen. For example, if you start writing a script that you thought would only do one thing, and then expands to cover more use cases. Or conversely, if you named your script thinking that it would be very generic, but it ends up being more specific. You can use the **git mv** command to rename files in the repository.

The **git mv** command works in a similar way to the **mv** command on Linux and so can be used for both moving and renaming. If our repository included more directories in it, we can use the same **git mv** command to move files between directories.

As you can probably tell from our examples, the output of git status is a super useful tool to help us know what's up with our files. It shows us which files have tracked or untracked changes, and which files were added, modified, deleted or renamed. It's important that the output of these commands stays relevant to what we're doing.

If we have a long list of untracked files, we might lose an important change in the _noise_. If there are files that get automatically generated by our scripts, or our operating system generates artifacts that we don't want in our repo, we'll want to _ignore_ them so that they _don't add noise_ to the output of git status. To do this, we can use the _**.gitignore**_ file. Inside this file, we'll specify rules to tell git which files to skip for the current repo. This file needs to get tracked just like the rest of the files in the repo with **git add**.

### Undoing Things

#### Undoing Changes Before Committing

Being able to _revert our changes is one of the most powerful features offered by version control systems_. There's a bunch of different techniques available depending on which changes we need to undo. In this section and the next few coming up, we'll talk about the most common ways to revert changes in Git and when to use each approach.

For example, you might find yourself in a situation where you've made a bunch of changes to a file but decide that you don't want to keep them. You can change a file back to its earlier committed state by using the **git checkout** command followed by the name of the file you want to revert.

Speaking of, let's try this out using our scripts repository. We'll edit our all checks pi script and remove the check reboot function, then save and go back to the command line. Cool. We've made our change. Let's try our script and see what happens.

By deleting that function, we've actually broke the script. Let's see what git status has to say about this. As expected, we see that our file is modified and the changes aren't staged yet. Check out how git gives us a couple helpful tips on what to do now. We can run **git add** to stage our changes or we can run **git checkout** to discard them. If you need help remembering what this command does, think of it this way, you're checking out the original file from the latest storage snapshot. Let's do that now

We'll check out at the original file and then take a look at what git status has to say about it and finally retry our script. Looks like we have a typo. Let's go back and fix it. Done and done.

With that, we've demonstrated how we can use **git checkout** to revert changes to modify files _before they get staged_. This command will _restore_ the file to the latest storage snapshot, which can be either _committed_ or _staged_. So if you've made additional changes to a file after you've staged it, you can restore the file to the earlier stage version.

If you need to check out individual changes instead of the whole file, you can do that using the **-p flag**. This will ask you change by change if you want to go back to the previous snapshot or not. That's it for undoing unstaged changes.

What if you added the changes to the staging area already? If we realize we've added something to the staging area that we didn't actually want to commit, we can unstage our changes by using the **git reset** command. Staging changes that we don't actually intend to commit happens all the time. Especially if we use a command like **git add \***, where the star is a file glob pattern used in Bash that expands to all files.

This command will end up adding any change done in the working tree to the staging area. While sometimes that might be what we want, it can also lead to some surprises.

Let's try it out with an example. First, we'll pretend we're trying to debug a problem in our script. For that, we create a temporary file with the output of our script. Then, we'll add all unstaged changes in our working tree using git add **\***. Finally, check the status using **git status**. We can see that this output file, which was supposed to be a temporary file for debugging, has now been staged in our repo but we didn't want to commit it. Conveniently, the **git status** command tells us how to unstage the file right there in the output. The example output mentions the head alias. Remember it's the current checked out snapshot. So by running the suggested **git reset** command, we're resetting our changes to whatever's in the current snapshot. Let's try it out. The file is once again untracked in our working tree and no longer staged. You can think of reset as the counterpart to add. With add, you can well add changes to the staging area. With reset, you remove changes from the staging area. You can use **git reset -p** to get git to ask you which specific changes you want to reset.

With that, we've seen how we can revert unstaged and stage changes. But what if you've already created a commit with the changes that you want to undo?

#### Amending Commits

In general, we try to make sure our commits include all the right changes and descriptions.

But we're all human and we make mistakes. It's not uncommon for developers and IT specialists to realize that there is an error in a recent commit, which is why it's important to know how to take action and fix it.

Let's say you just finished committing your latest batch of work, but you've forgotten to add a file that belongs to the same change. You'll want to update the commit to include that change. Or maybe the files were correct, but you realize that your commit message just wasn't descriptive enough. So you want to fix the description to add a link to the bug that you're solving with that commit. What can you do?

We can solve problems like these using the **--amend** option of the **git commit** command. When we run **git commit --amend**, git will take whatever is currently in our staging area and run the git commit workflow to overwrite the previous commit. Let's see this in an example. We'll go to our scripts directory and create two new files using the touch command. Then list the contents of the directory using ls at our Python script and commit it saying that we've added two files. As you can see, the message printed by git says that only one file was added. Our commit message said that we added two files, but we forgot to add one of them. Ouch. Don't panic. We can fix it. We'll start by adding the missing file and then amending our commit. We call git commit --amend and an editor opened up showing the commit message and the stats about the commit that we're working with. The list of added files for this commit now includes both files that we wanted to add. Yay. Now that the files have been added, we can also improve our initial commit message which was a bit too short. We'll keep the existing description as the first sentence of our commit, and then add a line of description about the intended purpose of each file. With that, our commit is ready to be amended. Let's save the new description as usual. We've amended our previous commit to include both files and a better message. You could also just update the message of the previous commit by running the git commit --amend command with no changes in the staging area.

_**An important heads up**_. While **git commit --amend** is okay for fixing up _local commits_, _**you shouldn't use it on public commits**_. Meaning, those that have been pushed to a public or shared repository. This is because using --amend rewrites the git history removing the previous commit and replacing it with the amended one. This can lead to some confusing situations when working with other people and should definitely be avoided. So remember, fixing up a local commit with amend is great and you can push it to a shared repository after you fixed it. But you should **avoid amending commits that have already been made public**.

We've covered how to fix staged and unstaged changes, and how to fix a commit that was incomplete. Up next, we'll talk about what to do if you come across a bad commit that needs to be completely reverted.

#### Rollback

Fixing your work before you commit is good. But what happens if it's already been snapshotted by Git?

Let's say you host to Git repository on a company server that contains all kinds of useful automation scripts that you and your coworkers use. One morning before coffee, you make a few changes to one of these scripts and commit the updated files. A few hours later, you start to receive tickets from users indicating some part of the script is broken. From the errors they describe, it sounds like the problem is related to your recent changes.

Oh oh, you could look at the code you updated to see if you can spot the bug. But more tickets are pouring in and you want to fix the problem as fast as possible. You decided it's time for a rollback.

There are a few ways to rollback commits in Git. For now, we'll focus on using the **git revert** command. Git revert doesn't just mean undo. Instead, it creates a commit that contains the inverse of all the changes made in the bad commit in order to cancel them out. For example, if a particular line was added in the bad commit, then in the reverted commit, the same line will be deleted. This way you get the effect of having undone the changes, but the history of the commits in the project remains consistent leaving a record of exactly what happened. So **git revert** will create _a new commit_, that is the opposite of everything in the given commit. We can revert the latest commit by using the _HEAD alias_ that we mentioned before. Since we can think of HEAD as a pointer to the snapshot of your current commit, when we pass HEAD to the **revert** command we tell Git to rewind that current commit.

To check this out, we'll first add a faulty commit to our example repo. We've added some code to our script. Let's save and commit this. So now, our code is committed. We didn't even test it which is a bad idea if you're doing this for real. You might have already spotted the problem with our code. This is where users start filing tickets and saying that things are broken, and so we run our script to see what happens. Oops, we use the function that we forgot to define. Okay. It's rollback time.

Let's get rid of this faulty code by typing **git revert head**. So once we issue that git revert command, we're presented with the text editor commit interface that we've all seen before. In this case, we can see that git has automatically added some text to the command indicating it's a rollback. The first-line mentions that it's reverting the commit we just did called Add call to disk full function. The extra description even includes the identifier of the commit that got reverted.

While we could use this description as is, _it's usually a good idea to add an explanation of why we're doing the rollback_. Remember that the goal of these descriptions is to help our future selves understand why things happen. In this case, we'll explain that the reason for the rollback is that the code was calling a function that wasn't defined. Once we're done entering the description, we can exit and save as usual.

You'll notice the output that we get from the git revert command looks like the output of the git commit command. This is because git revert creates a commit for us. Since a revert is a normal commit, we can see both the commit and the reverted commit in the log. Let's look at the last two entries in the log using dash P and dash two as parameters. As demonstrated before, the **-p** parameter lets us see the patch created by the commit while the **-2** perimeter limits the output to the last two entries.

So in this log, we can see that when we called revert, git created a new commit that's the inverse of the previous one. This removes the lines that we added in the previous commit. We can see that the original commit shows the lines we added by preceding them with a plus sign. The same line shows up with a minus sign in the newer commit message indicating that they were removed. Just like that, the bad commit is reverted and the error stopped. In this example, we reverted the latest commit in our tree. But what if we had to revert a commit that was done before that?

#### Identifying a Commit

So far we've used the head alias to specify the most recently checked out commit in our Git history. In our bad snapshot example, the error also happened to be in the most recently created commit, but errors can sometimes take a while to be detected. And so, we might need to revert other commits farther back in time. We can target a specific commit by using its commit ID.

We've seen commit IDs a few times already. They show up when we're running the git log command, and we also saw the commit ID of the reverted commit in our last example. Commit IDs are those complicated looking strings that appear after the word commit in the log messages. Let's have a look at the latest log entry in our checks repo.

The commit ID is the 40 character long string after the word commit, you really can't miss it. This long jumble of letters and numbers is actually something called a hash, which is calculated using an algorithm called **SHA1**. Essentially, what this algorithm does is take a bunch of data as input and produce a 40 character string from the data as the output. In the case of Git, the input is all information related to the commit, and the 40 character string is the commit ID. Cryptographic algorithms like SHA1 can be really complex, so we won't go too deep into what this means. If you're interested, you'll find links to more information in the next reading. Still you might be wondering, why on earth would you use a long jumble of letters as an ID for commit, instead of incrementing an integer, like 123, etc?

To answer that, let's take a quick look at the reason why Git uses a hash instead of a counter, and how that hash is computed. Although SHA1 is a part of the class of cryptographic hash functions, Git doesn't really use these hashes for security. Instead, they're used to guarantee the consistency of our repository. Having consistent data means that we get exactly what we expect. To quote Git's creator, _**Linus Torvalds**_:

> "you can verify the data you get back out is the exact same data you put in". [Google Tech Talk: Linus Torvalds on git](https://www.youtube.com/watch?v=4XpnKHJAok8)

This is really useful in distributed systems like Git because everyone has their own repository and is transmitting their own pieces of data. Computing the hash keeps data consistent because it's calculated from all the information that makes up a commit. The commit message, date, author, and the snapshot taken of the working tree. The chance of two different commits producing the same hash, commonly referred to as a collision, is extremely small. So small, it wouldn't happen by chance. It'd take a lot of processing power to cause this to happen on purpose. If you use a hash to guarantee consistency, you can't change anything in the Git commit without the SHA1 hash changing too.

Each time we amend a commit, the commit ID will change. This is why it's important not to use dash dash amend on commits that have been made public. The data integrity offered by the commit ID means that if a bad disk or network link corrupt some data in your repository, or worse, if someone intentionally corrupt some data, Git can use the hash to spot that corruption. Aha, it will say, the data you've got isn't the data you expected, something went wrong.

Okay, enough backstory. How can you use commit IDs to specify a particular commit to work with, like during a rollback?

Let's look at the last two entries in our repo using the git log -2 command. Say we realized that we actually liked the previous name of our script, and so we want to revert this commit where we renamed it. First, let's look at that specific commit using git show, which we mentioned in an earlier video. We've copied and pasted the commit ID that we wanted to display, and that works. Alternatively, we could provide just the first few characters identifying the commit to the command, and Git will be smart enough to guess which commit ID starts with those characters, as long as there's only one matching possibility.

Let's try this out. Two characters is not enough, but usually four to eight characters will be plenty. Okay, now that we've seen how we can identify the commit that we want to revert, let's call the **git revert command with this identifier**. As usual, this will open an editor where we should add a reason for the rollback. In this case, we'll say that the previous name was actually better. Hooray for flip-flopping.

As we called out before, when we generate the rollback, Git automatically includes the ID of the commit that we're reverting. This is useful when looking at a repo with a complicated history that includes a lot of commits. Now, once we save and exit the commit message, Git will actually perform the rollback and generate a new commit with its own ID. See how before the name of our commit the revert command already shows the first eight characters of the commit ID? Let's use git show to look at it. All right, we've managed to revert a commit that wasn't the most recent one. Well done, time travelers.

Over the past several videos we've covered a bunch of ways to undo things in Git. Whether for unstaged changes, staged changes, amending commits, or rolling back changes. If anything still seems unclear, now's a great time to practice these commands on your local computer, try things out, and come up with more examples of use cases you want to test. Up next, we've spun up a handy cheat sheet summarizing all the content we just covered.
