#include <cs50.h>
#include <stdio.h>

// Declaring prototype functions
int get_positive_int(void);

int main(void)
{
    int num = get_positive_int();
    int numOfHashtags = 1;
    int numOfSpaces = num - 1;

    for (int columns = 0; columns < num; columns++)
    {
        // The two inner for loops print the spaces first and then the hashtags
        for (int spaces = 0; spaces < numOfSpaces; spaces++)
        {
            printf(" ");
        }
        for (int hashtags = 0; hashtags < numOfHashtags; hashtags++)
        {
            printf("#");
        }

        // Decreasing the numOfSpaces and increasing the numOfHashtags after every outer loop
        // iteration(after every column)
        numOfSpaces--;
        numOfHashtags++;
        printf("\n");
    }
}
// Getting a positive integer between 1 and 8
int get_positive_int(void)
{
    int num;
    do
    {
        num = get_int("Enter a number between 1 and 8. ");
    }
    while (num < 1 || num > 8);
    return num;
}
