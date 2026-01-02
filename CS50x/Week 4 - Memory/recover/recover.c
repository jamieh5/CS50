#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    int counter = 0;
    uint8_t buffer[512];

    FILE *card = fopen(argv[1], "r");
    FILE *img = NULL;
    char filename[8];

    // If card doesnt exits return 1
    if (card == NULL) {
        return 1;
    }

    // Reading 512 byte blocks of input file
    while(fread(buffer, 1, 512, card) == 512) {
        // Checking if the first four bytes are the img header bytes
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0) {
            // If img is already open -> closing img
            if (img != NULL) {
                fclose(img);
            }
            sprintf(filename, "%03i.jpg", counter);
            img = fopen(filename, "w");
            counter++;
        }
        // Writing the img
        if (img != NULL)
        {
            fwrite(buffer, 1, 512, img);
        }
    }
    // Closing the existing img and the input file
    if (img != NULL)
    {
        fclose(img);
    }
    fclose(card);

    return 0;
}
