# Final Exam

## Question 1

18 / 18 pts

The purpose of this section is to assess your understanding of test coverage metrics and your ability to critically evaluate test suites. You may use the blank fields in the testing suite table if it helps you answer the question, but this not mandatory. Please exclusively consider statement, branch, and basic condition coverage in your answers.

Pseudo-code:

```
t = 8;
if ((x > 6 && y < 0) && (z != 0))
{ t = (x - y) * z; }
r = t * 2;
```

Testing Suite:

| Input                | Expected | Pass | Sub Condition 1? | Sub Condition 2? | Sub Condition 3? |
|----------------------|----------|------|------------------|------------------|------------------|
| x = 8, y = -2, z = 4 | r = 40   |      |                  |                  |                  |
| x = 0, y = 2, z = 0  | r = 16   |      |                  |                  |                  |

How many statements are executed by the test suite? 

> 4

What is the total number of statements? 

> 4

What is the percentage statement coverage? 

> 100%

How many branches are executed by the test suite? 

> 2

What is the total number of branches? 

> 2

What is the percentage branch coverage? 

> 100%

How many branch conditions are executed by the suite? 

> 6

What is the total number of branch conditions? 

> 6

What is the percent branch condition coverage? 

> 100%
 
## Question 2

30 / 30 pts

### Instructions

To be successful, you should:

Identify independently testable features,
Recognize the inputs or behaviors that are worth testing for these features,
Derive the input equivalence partitions classes,
Select representative values from each partition as test data.
It should go without saying that not just any value selections will suffice. Test data must be selected that are particularly representative of the span of the functions' domains and sub-domains; we know that errors tend to occur at the boundaries thereof. We can do this by conducting a Boundary Value Analysis and testing values at both valid and invalid boundaries.

The challenges of the tester are to devise a small, manageable set of test cases in order to:

Maximize the chances of detecting a fault
Minimize the chances of wasting a test case
You should include an explanation on how the test cases were selected, including describing:

What classes of input have produced good test cases
If the system is particularly sensitive to certain input values
How the boundaries of a data class were identified
For a test case to be valid, it must belong to an identified equivalence class and be identified in terms of its position within that class (hint: this is related to boundary value analysis). Only one test case per combination of these two properties will be counted (i.e. redundant test cases do not count). Only one invalid input equivalence class for each function will be counted.

The format for test cases are not rigidly defined, but it must include the following four properties:

Input
Expected output
Equivalence class
Position with partition

### Question

The following function returns the square of the signed int argument, which must be greater than or equal to zero that is sent to it.

```c
unsigned long int square (int number)
```

For reference, the minimum/maximum values for the types in this specification are:

```c
unsigned long int     [0 .. 4294967295]            // 0 ... ULONG_MAX
int                   [-32,767 .. +32,767]          // INT_MIN  ... INT_MAX
```

### Answer

Test Cases Concerning input (int number)

int valid range: INT_MIN to INT_MAX inclusive
number valid range 0 to INT_MAX inclusive

Testing boundary 0

Equivalence classes defined to be:

[INT_MIN, 0) - these are alike in that they are all valid but will cause failure. 

[0, INT_MAX] - this is the entire set of valid input values

Less than 0 is assumed to be a fault, we will test close to 0 to catch errors that occurr at boundary and are representative of the class of unacceptable numbers less than zero but more than (or equal to) INT_MIN. (ECP 1)

Input: -1
Expected output: FAILURE
Equivalence class: INT_MIN <= x < 0
Position with partition: less than partition 0

Input: INT_MIN
Expected output: FAILURE
Equivalence class: INT_MIN <= x < 0
Position with partition: on partition INT_MIN

Greater than zero has two boundaries, 0 and INT_MAX, we will test close to each of those. I have included a couple test cases here. (ECP 2)

Input: INT_MAX
Expected output: INT_MAX ^ 2 == 1073676289
Equivalence class: 0 <= x <= INT_MAX
Position with partition: testing less than partition INT_MAX

Input: INT_MAX-1
Expected output: (INT_MAX-1)^2
Equivalence class: 0 <= x <= INT_MAX
Position with partition: testing less than partition INT_MAX (redundant with prev test)

Input: 0
Expected output: 0
Equivalence class: 0 <= x <= INT_MAX
Position with partition: Testing lower boundary, 0

Input: 1
Expected output: 1
Equivalence class: 0 <= x <= INT_MAX
Position with partition: testing above lower boundary, 0, but close to it. (redundant with prev. test)

## Question 3

30 / 30 pts

### Instructions

To be successful, you should:

Identify independently testable features,
Recognize the inputs or behaviors that are worth testing for these features,
Derive the input equivalence partitions classes,
Select representative values from each partition as test data.
It should go without saying that not just any value selections will suffice. Test data must be selected that are particularly representative of the span of the functions' domains and sub-domains; we know that errors tend to occur at the boundaries thereof. We can do this by conducting a Boundary Value Analysis and testing values at both valid and invalid boundaries.

The challenges of the tester are to devise a small, manageable set of test cases in order to:

Maximize the chances of detecting a fault
Minimize the chances of wasting a test case
You should include an explanation on how the test cases were selected, including describing:

What classes of input have produced good test cases
If the system is particularly sensitive to certain input values
How the boundaries of a data class were identified
For a test case to be valid, it must belong to an identified equivalence class and be identified in terms of its position within that class (hint: this is related to boundary value analysis). Only one test case per combination of these two properties will be counted (i.e. redundant test cases do not count). Only one invalid input equivalence class for each function will be counted.

The format for test cases are not rigidly defined, but it must include the following four properties:

Input
Expected output
Equivalence class
Position with partition

### Question

The following function returns the square root of the double argument that is sent to it.

```c
double sqrt (double x)
```

For reference, the minimum/maximum values for the types in this specification are:

```c
double     [-2^53 ... 2^53]             // DBL_MIN ... DBL_MAX
```

### Answer

Given that it is impossible to find the square root of x<0, all negative inputs must produce an error.

Even with no knowledge of this function's workings, there are special values that we will test here, these include 0, 1 - these are unique as they will be *identity* values, i.e. the result will be the same as input, and thusly they are likely hardcoded. For this reason, we also test input 2 to catch the lower partition of the EC 0 <= x <= DBL_MAX.

Equivalence Classes will be defined as

[DBL_MIN, 0) - these are alike in that they are all valid but will cause failure within function. 

[0, DBL_MAX] - this is the entire set of valid input values

Test Cases Concerning input (double x)

Less than 0 is assumed to be a fault, we will test close to 0 to catch errors that occurr at boundary and are representative of the class of unacceptable numbers less than zero but more than (or equal to) DBL_MIN. (ECP 1)

Input: -1
Expected output: FAILURE
Equivalence class: DBL_MIN <= x < 0
Position with partition: less than partition 0

Input: DBL_MIN
Expected output: FAILURE
Equivalence class: DBL_MIN <= x < 0
Position with partition: on partition DBL_MIN

Greater than zero has two boundaries, 0 and DBL_MAX, we will test close to each of those. I have included a couple test cases here. (ECP 2)

Input: DBL_MAX
Expected output: sqrt(DBL_MAX)
Equivalence class: 0 <= x <= DBL_MAX
Position with partition: testing less than partition DBL_MAX

Input: DBL_MAX-1
Expected output: sqrt(DBL_MAX - 1)
Equivalence class: 0 <= x <= DBL_MAX
Position with partition: testing less than partition DBL_MAX (redundant with prev test)

Input: 0
Expected output: 0
Equivalence class: 0 <= x <= DBL_MAX
Position with partition: Testing lower boundary, 0

Input: 1
Expected output: 1
Equivalence class: 0 <= x <= DBL_MAX
Position with partition: testing above lower boundary, 0, but close to it. (redundant with prev. test)

Input: 2
Expected output: sqrt(2)
Equivalence class:0<=x<=DBL_MAX
Position with partition: greater than partition 0, first value that will not result in same output as input
 
## Question 4

15 / 15 pts

The scope of this question is to assess your understanding of the fundamentals of acceptance testing, to place specific testing techniques i the larger context of software testing, and to show awareness of the role that user testing serves.

This question requires a 2-3 paragraph essay response to the following prompt:

Compare and describe the following two user testing practices: Alpha Testing and Beta Testing.

> Alpha testing is the first real stage of testing that involves possible software users (most often existing software users). This testing format consists of a limited, often invite-only-distributed release of the working product (i.e. in progress version) of the software that is being developed. Access to this software is granted to the limited set of users, who are able to test it out and discover problems with it. This often takes place at the development site, or on the development team's equipment, rather than on user devices, hardware or premises. This is likely as a result of the alpha code being buggy and prone to error. An alpha release is almost always offered to users that have deeper knowledge of the software (past versions), so that they may be better qualified to describe and even understand the causes of bugs. Alpha testing also involves a decent amount of cooperation with the dev team from the testers.

> This differs greatly from a Beta test, where the software, now in a more complete and more functioning (while not perfect) format is semi-publicly released (opt in, typically) to users who choose to get and test the Beta version. Beta testing takes place on the users hardware, devices and or premises, and is often accompanied with some user/tester-friendly way to submit bug reports. Beta testing involves a formal beta release that is offered to the user/testers so they can find bugs. 

> The differences between these two testing methods are many-fold. First of all, Alpha testing precedes Beta testing, as for beta testing the software is more complete (as a result of Alpha testing) than when it is presented to alpha testing. Secondly, Alpha testing is released to a limited group of people, whereas there are *fewer* limits on the distribution of the beta code. Also, alpha testers are assumed often to have a better understanding of the software or software construction in general, and are often assumed to be able to perform more debugging rather than immediately submitting a bug report. Further, alpha testing does not formally involve a release as much or as publicly as a beta test would. In alpha testing, the tests are done on the development machines, premises, rather than on the testers hardware or premises - this contrasts with beta testing where the users run the beta code on their own premises or hardware. In alpha testing, the testers have more contact than beta testing with the developers. 

 
## Question 5

7 / 7 pts

For the following quote, do you find the statements to be true or false?

> "The ISO 9001 standard is a framework for developing software standards. It sets out general quality principles, describes quality processes in general and lays out the organizational standards and procedures that should be defined. These should be documented in an organizational quality manual."

> [C] True 

> False 