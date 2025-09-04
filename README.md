# PA3: Interaction and Arithmetic

### Learner Objectives
At the conclusion of this programming assignment, participants should be able to:
* Use variables and cout and cin statements
* Compute values using arithmetic operators
 
### Acknowledgments
Content used in this assignment is based upon information in the following sources:
* https://code.tutsplus.com/articles/become-a-flash-mathemagician-with-fun-math-tricks--active-8893
* This programming assignment is adapted from Dr. Gina Sprint's Computer Science I class at Gonzaga University

## Overview and Requirements
For this programming assignment, we are going to write a basic [chatbot](https://en.wikipedia.org/wiki/Chatterbot_) program. For fun, you can try having a conversation with an online chatbot [here](https://www.pandorabots.com/mitsuku/). 

The chatbot we are going to design wants to know a few things about you! Such as:
1. What is your name?
2. Where are you from?
3. What year were you born?
4. What is your dream car?
5. How much does your dream car cost?
 

## Program Details
- [ ] Create a C++ source code file named `chatbot.cpp`. 

Write a chatbot program that interacts with the user in the following manner:
- [ ] Find out the name of the user (`string`). Reply with a greeting, such as "It's so nice to meet you <user's name>! My name is <name of your chatbot>".
- [ ] Find out where the user is from (`string`). Reply with a positive statement, such as "<location> sounds like a pleasant place to be from!".
- [ ] Find out what year the user was born in (`int`). Figure out how old the user is in years based on their birth year. Reply with a value that relates the user's age to your chatbot's age (pick an age for your chatbot), such as "You are <user's age> years old, that makes you 1.5 times as old as I am! I'm only <chatbot's age> years YOUNG!."
- [ ] Find out the user's dream car (`string`). Reply with a comment that expresses interest in the car, such as "Wow, I've always wanted a <car> as well.
- [ ] Find out how much the dream car costs (`float`). Then start a conversation about the cost of the car:
   - [ ] A comment about how expensive the car is, such as "Gee, that is spendy."
   - [ ] Find out how many years the user would take a loan out to pay for <car> (`int`)
   - [ ] Find out what annual interest rate (percent) the user expects to get for <car> (`float`)
   - [ ] Reply with the expected monthly payment and the total amount of money the user would pay for <car> (car price + interest), such as "Your monthly payment for the <car> is <monthly payment>, that is a total of <total cal cost>!”.
- [ ] Say goodbye to <user's name>.
  
For calculating monthly payments, use the following formula:


$$PMT = {P {r \over n} \over [1-(1 + {r \over n})^{-nt}]} $$

where,
* **_r_** is the yearly interest rate,
* **_P_** is the cost of the car, and
* **_n_** is the number of payments per year. 
* **_t_** is the number of  years. 

You can figure out **_r_** by converting the annual interest rate the user enters to a decimal (divide by 100).

> **NOTE**: To raise a base to an exponent, you’ll want to use the [pow function](https://en.cppreference.com/w/cpp/numeric/math/pow)
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pow(base, exponent)`
>
> function from the `cmath` [library](https://en.cppreference.com/w/cpp/header/cmath).

 
## Sample Run
Here is an example run of my "CarBot" program:

<pre>
Hello there! My name is CarBot. What is your name? 
<b>Jane</b>
Hello Jane, it is great to meet you!
Jane, where are you from?
<b>Washington</b>
Washington sounds like a pleasant place to grow up. Hmmmm, what else can I ask you... oh! What year were you born?
<b>1950</b>
You are 67 years old, that makes you 33.5 times as old as I am! I'm only 2 years YOUNG!
What is your dream car? 
<b>BMWi8</b>
Wow, I have always wanted a BMWi8 as well. How much does a BMWi8 cost? 
<b>141695</b>
What is a reasonable yearly interest rate on a beautiful car like that? 
<b>2.0</b>
And if you had to take out a loan to buy the BMWi8, how many years would you take the loan out for? 
<b>5</b>
If you bought the BMWi8, you would have a monthly payment of $2483.60, hopefully, that is reasonable for your budget. 
That's a total of $149015.76! I hope you can make the purchase!

\< This part for EC (10pts) \>
Before I go, let's play a math trick!
Step 1. In your head, think of any four-digit number, like 5623. Don't follow my number, be original!
Step 2. Write down on paper the first digit (in my case, 5).
Step 3. Now write the first two digits (in my example, 56).
Step 4. And lastly, the first three digits (here, 562).
Step 5. Now, the part that everyone is scared of, sum up the three numbers from the three previous steps.
Step 6. Multiply the answer from the previous step by 9. What is the result?
<b>5607</b>
Step 7. Sum up the 4 digits of the original number in Step 1. What is the sum?
<b>16</b>
I believe the number you wrote down is 5623! Am I right?!?!
Anyway, I gotta go. It's been nice chattin' with ya Jane :)
</pre>
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![BMWi8](https://farm8.static.flickr.com/7550/15608475810_df987c5dac.jpg "BMWi8")


## Grading
**Functionality (2/4)**
* Output does not have to exactly match mine but it should be very interactive and console displays should be descriptive to the user of the program.
* Very important, any part of the program that uses arithmetic computation, the results should be correct.
* Give your chatbot its own personality!

**Style (1/4)**
* Variable names should be descriptive. Do not use single-character variable names. For example, the **_r_** in the formula could have a variable name of `monthlyInterestRate`.
* Add some blank lines to separate sections of your program to make the code more readable.
* Proper indentation!
* Consistency in your programming style.
* Committing your code to Github frequently, and having useful commit messages.

**Presentation (1/4)**
* Must have a file header comment
* Must add in-line comments to your code to describe what that section of the code does.

## Starter Code
You may use the starter code provided below or you may start with your own code from scratch. In any case, ensure that you have included a **header comment**.

```cpp
/**
 * @file   WRITE FILENAME
 * @author WRITE STUDENT NAME
 * @brief  WRITE DESCRIPTION ABOUT THE PROGRAM/FILE
 * @date   WRITE DATE STARTED
 * 
 */
#include <iostream>
#include <string>
using namespace std;

int main()
{
    // Prompt user to input name
    string userName;
    cout << "What is your name?" << endl;
    cin >> userName;   // Only use first name. You can modify this to allow multi-word
    cout << "Hi there, it is nice to meet you " << userName << endl;

    // Prompt user to input location
    string userFrom;
    cout << "Where are you from? " << endl;
    cin >> userFrom;   // Only use single word. You can modify this to allow multi-word

    return 0;
}
```

## Submitting Assignments
- [ ] It is VERY IMPORTANT that besides pushing the code to GitHub that you still submit the GitHub URL of this lab assignment in Canvas. This allows the instructor to be notified of your final submission.

> **_NOTE: By submitting your code to be graded, you are stating that your submission does not violate the Academic Integrity Policy outlined in the syllabus._**
