#include<stdio.h>
int main()
{
     double power(double b, int e)
     {
     double r=1;
     int i;
     for(i=0;i<e;i++)
     {
     r*=b;
     }
     return r;
     }

    FILE *file = fopen("values.dat", "w");  // Open a text file for writing

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;  // Return an error code
    }

    // Use fprintf to write values to the file directly without arrays
    fprintf(file, "Values for stem plot of x_1(n):\n");
    float x[10];
    for (int i = 0; i < 8; i++) {
        x[i]=(i+1)*power(0.5,i);
        fprintf(file, "%d %f\n", i, x[i]);
    }
     fprintf(file, "\nValues for stem plot of x_2(n):\n");  // Add a newline and heading
    float y[10];
    for (int i = 0; i < 8; i++) {
        y[i]=((i+1)*(power(0.5,i+2))-(i+2)*(power(0.5,i+1))+1)/(0.25);
        fprintf(file, "%d %f\n", i, y[i]);
    }

    fclose(file);  // Close the file

    return 0;

}
