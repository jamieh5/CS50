#include <stdio.h>
#include <cs50.h>

// Create a function that uses the remainder % to continue and divides the num
// for example: 120 % 25 = 20; 120 / 25 = 4;
// Continue the programm with the num 20 and add 4 to the number of coins

int get_positive_int(void);
int calculate_Quarters (int change);
int calculate_Dimes(int change);
int calculate_Nickels(int change);
int calculate_Pennies(int change);

int coins = 0;

int main(void) {
    int change = get_positive_int();

    change = calculate_Quarters(change);
    change = calculate_Dimes(change);
    change = calculate_Nickels(change);
    change = calculate_Pennies(change);

    printf("%i\n", change);
    printf("%i\n", coins);
}

int get_positive_int(void) {
    int num;
    do {
        num = get_int("Change owed: ");
    } while (num < 0);
    return num;
}

// Calculating the Quarters
int calculate_Quarters(int change) {
    coins += change / 25;
    change = change % 25;

    return change;
}

// Calculating the Dimes
int calculate_Dimes(int change) {
    coins += change / 10;
    change = change % 10;

    return change;
}

// Calculating the Nickels
int calculate_Nickels(int change) {
    coins += change / 5;
    change = change % 5;

    return change;
}

// Calculating the Pennies
int calculate_Pennies(int change) {
    coins += change / 1;
    change = change % 1;

    return change;
}
