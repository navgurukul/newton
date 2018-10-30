```ngMeta
name: bool
completionMethod: manual
```
# Boolean Values

While the integer, floating-point, and string data types have an unlimited number of possible values, the Boolean data type has only two values: True and False. (Boolean is capitalized because the data type is named after mathematician George Boole.) When typed as Python code, the Boolean values True and False lack the quotes you place around strings, and they always start with a capital T or F, with the rest of the word in lowercase. Enter the following into the interactive shell. (Some of these instructions are intentionally incorrect, and they’ll cause error messages to appear.)

# Comparison Operators

| Operator  | Meaning    |
|-----------|------------|
| ==        | Equal to   |
| !=        | Not equal to   |
| <        | less than   |
| >        | Greater than   |
| <=        | Less than or equal to   |
| >=        | greater than or equal to   |

These operators evaluate to True or False depending on the values you give them. Let’s try some operators now, starting with == and !=.

As you might expect, == (equal to) evaluates to True when the values on both sides are the same, and != (not equal to) evaluates to True when the two values are different. The == and != operators can actually work with values of any data type.
The <, >, <=, and >= operators, on the other hand, work properly only with integer and floating-point values.

## The Difference Between the == and = Operators

You might have noticed that the == operator (equal to) has two equal signs, while the = operator (assignment) has just one equal sign. It’s easy to confuse these two operators with each other. Just remember these points:

1. The == operator (equal to) asks whether two values are the same as each other.

2. The = operator (assignment) puts the value on the right into the variable on the left.

To help remember which is which, notice that the == operator (equal to) consists of two characters, just like the != operator (not equal to) consists of two characters.

# Boolean Operators

The three Boolean operators (and, or, and not) are used to compare Boolean values. Like comparison operators, they evaluate these expressions down to a Boolean value. Let’s explore these operators in detail, starting with the and operator.

# Binary Boolean Operators

The and and or operators always take two Boolean values (or expressions), so they’re considered binary operators. The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False. Enter some expressions using and into the interactive shell to see it in action.

A truth table shows every possible result of a Boolean operator. Table 2-2 is the truth table for the and operator.

| Expression | Evaluates to... |
|------------|-----------------|
|True and True| True           | 
|True and False| False           | 
|False and True| False          | 
|False and False| false           | 

On the other hand, the or operator evaluates an expression to True if either of the two Boolean values is True. If both are False, it evaluates to False.

You can see every possible outcome of the or operator in its truth table, shown in Table 2-3.

Table 2-3. The or Operator’s Truth Table

| Expression | Evaluates to... |
|------------|-----------------|
|True or True| True           | 
|True or False| True           | 
|False or True| True          | 
|False or False| false           | 

# The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or expression). The not operator simply evaluates to the opposite Boolean value.

Much like using double negatives in speech and writing, you can nest not operators ❶, though there’s never not no reason to do this in real programs. Table 2-4 shows the truth table for not.

| Expression | Evaluates to... |
|------------|-----------------|
| not True| False           | 
| not False| True           |

# Mixing Boolean and Comparison Operators

Since the comparison operators evaluate to Boolean values, you can use them in expressions with the Boolean operators.

Recall that the and, or, and not operators are called Boolean operators because they always operate on the Boolean values True and False. While expressions like 4 < 5 aren’t Boolean values, they are expressions that evaluate down to Boolean values. Try entering some Boolean expressions that use comparison operators into the interactive shell.

The computer will evaluate the left expression first, and then it will evaluate the right expression. When it knows the Boolean value for each, it will then evaluate the whole expression down to one Boolean value. You can think of the computer’s evaluation process for (4 < 5) and (5 < 6) as shown in Figure 2-2.

You can also use multiple Boolean operators in an expression, along with the comparison operators.

The Boolean operators have an order of operations just like the math operators do. After any math and comparison operators evaluate, Python evaluates the not operators first, then the and operators, and then the or operators.
 

