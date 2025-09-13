/**
 * @file chatbot.cpp
 * @author David Espinoza
 * @brief CarBot tells you car monthly payments
 * @version 0.1
 * @date 2025-09-11
 * 
 * @copyright Copyright (c) 2025
 * 
 */

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    // Prompt user to input name
    string userName;
    cout << "What is your name?" << endl;
    cin >> userName;   // Only use first name. You can modify this to allow multi-word
    cout << "Hi there, it is nice to meet you " << userName << "! My name is CarBot." << endl;

    // Prompt user to input location
    string userFrom;
    cout << userName << ", where are you from? " << endl;
    cin >> userFrom;   // Only use single word. You can modify this to allow multi-word
    cout << userFrom << " sounds like a pleasant place to be from!" << endl;

    int yearBorn = 0;
    int userAge = 0;
    double chatAge = 10.0;
    double ageDifference = 0.0;
    cout << "What year were you born?" << endl;
    cin >> yearBorn;
    userAge = 2025 - yearBorn;
    ageDifference = userAge / chatAge;
    cout << "You are " << userAge << " years old, that makes you " << ageDifference << " times as old as I am! I'm only " << chatAge << " years YOUNG!" << endl;
   
    float carCost = 0.0;
    int carYears = 0;
    float annualRate = 0.0;
    float monthlyPayment = 0.00;
    float r = 0.0;
    int n = 0;
    string userCar;
    cout << "What is your dream car?" << endl;
    cin >> userCar;
    cout << "Wow, I've always wanted a " << userCar << " as well. How much does a " << userCar << " cost?" << endl;
    cin >> carCost;
    cout << "Gee that is spendy, what would the yearly interest rate (%) be on a car like that?" << endl;
    cin >> annualRate;
    cout << "How many years would you be paying that off?" << endl;
    cin >> carYears;
    r = annualRate / 100;
    n = 12;
    monthlyPayment = (carCost * (r / n)) / (1 - pow((1 + (r / n)), ((-n) * carYears)));
    cout << "If you bought a " << userCar << " at $" << carCost << " with a rate of " << annualRate << "% for " << carYears << " years, you would have a monthly payment of $" << monthlyPayment << ". Hopefully that is reasonable for your budget." << endl;
    cout << "Best of luck with your car " << userName << " and goodbye!" << endl;

    return 0;
}