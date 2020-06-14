# Assignment 6: Test Coverage

## Question 1
Pseudo-code:

```
y = 10;
if (x > 1)
{
   y = x / 0;
}
z = x + y;
```

Testing Suite:

| Input  | Expected | Pass? |
|--------|----------|-------|
| x = 0  | z = 10   |       |
| x = -1 | z = 9    |       |

How many statements are executed by the test suite? 

> 3

What is the total number of statements? 

> 4

What is the percentage statement coverage? 

> 75%

## Question 2

Pseudo-code:

```
y = 10;
if (x > 1)
{
   y = x / 0;
}
z = x + y;
```

Testing Suite:

| Input  | Expected | Pass? |
|--------|----------|-------|
| x = 0  | z = 10   |       |
| x = -1 | z = 9    |       |

All of the tests pass, but statement coverage is not 100%. Therefore, the statements not covered might be defective. How do we improve coverage?

Your Answer:
To improve coverage, we need to test the codepath where x > 1 (I.e. line 4), which is currently not tested. To test this, I would add test case: 

| Input  | Expected | Pass? |
|--------|----------|-------|
| x = 0  | z = 10   |       |
| x = -1 | z = 9    |       |
| x = 2  | Error    | NO    |
 
## Question 3

Pseudo-code:

```
y = 10;
if (x > 1)
{
   y = x / 0;
}
z = x + y;
```

Testing Suite:

| Input  | Expected | Pass? |
|--------|----------|-------|
| x = 0  | z = 10   |       |
| x = -1 | z = 9    |       |

Invent more test data that forces all statements to be executed. Use the same format as the other test data provided, and indicate whether this test passes or fails.

Your Answer:

| Input        | Expected | Pass?                  |
|--------------|----------|------------------------|
| x = 0        | z = 10   |                        |
| x = -1       | z = 9    |                        |
| x = 2        | Error    | NO: Div Dy Zero Error  |
| x = INT_MAX  | Error    | NO: Div Dy Zero Error  |

## Question 4


Pseudo-code:

```
y = 0;
if (x > 1)
{
   y = x + 5;
}
z = x + y;
```

Testing Suite:

| Input        | Expected | Branches  | Pass?      |
|--------------|----------|-----------|------------|
| x = 5        | z = 15   |           |            |
| x = 0        | z = 0    |           |            |

How many statements are executed by the test suite? 

> 4

What is the total number of statements? 

> 4

What is the percentage statement coverage? 

> 100%

How many branches are executed by the suite? 

> 2

What is the total number of branches? 

> 2

What is the percentage branch coverage? 

> 100%

## Question 5

Pseudo-code:

```
s = 3;
if (x > 1 || y == 0)
{
   s = x - y;
}
z = s * 2;
```

Testing Suite:

| Input        | Expected | Pass? | Condition 1? | Condition 2? |
|--------------|----------|-------|--------------|--------------|
| x = 2, y = 2 | z = 15   |       |              |              |
| x = 0, y = 2 | z = 0    |       |              |              |

How many statements are executed by the test suite? 

> 4

What is the total number of statements? 

> 4

What is the percentage statement coverage? 

> 100%

How many branches are executed by the suite? 

> 2

What is the total number of branches? 

> 2

What is the percentage branch coverage? 

> 100%

How many branch conditions are executed by the suite? 

> 1

What is the total number of branch conditions? 

> 2

What is the percentage branch condition coverage? 

> 50%

NOTE: Fudge points for added acceptable answers: 5.7 can be 1 or 2 5.8 can be 2 or 4 More details to follow either in class or via canvas announcement. Email me if you have any questions.