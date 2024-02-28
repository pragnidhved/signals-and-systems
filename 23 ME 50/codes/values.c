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
    float n[10];
    int y=0;
    n[0]=1;
    for (int i = 0; i < 9; i++) {
        
        n[i+1]=-(n[i]);
        fprintf(file, "%d %f\n", i, n[i]);
    }
fprintf(file, "Values for stem plot of x_2(n):\n");
    float m[9];
    int z=0;
    m[0]=1;
    fprintf(file, "%d %f\n", z+1, m[0]);
    for (int i = 1; i < 8; i++) {
        
        m[i]=power((-1),i);
        fprintf(file, "%d %f\n", i+1, m[i]);
    }


    fclose(file);  // Close the file

    return 0;

}
