#include "helpers.h"

#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < height; i++) {
        for(int j = 0; j < width; j++) {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            // Calculating the avg
            int avg = round((red + green + blue) / 3.0);

            // Assigning the new values to the image arr
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
}

// Helper function for values over 255
int overRange(int num) {
    if (num > 255) {
        num = 255;
    }
    return num;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++) {
        for(int j = 0; j < width; j++) {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            int sepiaRed = overRange(round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue));
            int sepiaGreen = overRange(round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue));
            int sepiaBlue = overRange(round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue));

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width / 2; j++) {
           RGBTRIPLE temp = image[i][j];
           image[i][j] = image[i][width -j - 1];
           image[i][width -j - 1] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++) {
        for(int j = 0; j < width; j++) {
           int sumRed = 0, sumGreen = 0, sumBlue = 0;
           int count = 0;
            for(int x = -1; x <= 1; x++) {
                for(int y = -1; y <= 1; y++) {
                    int neighborRow = i + x;
                    int neighborColumn = j + y;

                    if (neighborRow >= 0 && neighborRow < height && neighborColumn >= 0 && neighborColumn < width)
                    {
                        sumRed   += image[neighborRow][neighborColumn].rgbtRed;
                        sumGreen += image[neighborRow][neighborColumn].rgbtGreen;
                        sumBlue  += image[neighborRow][neighborColumn].rgbtBlue;
                        count++;
                    }
                }
            }
            temp[i][j].rgbtRed   = round((float)sumRed / count);
            temp[i][j].rgbtGreen = round((float)sumGreen / count);
            temp[i][j].rgbtBlue  = round((float)sumBlue / count);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}
