#include <stdio.h>

/**
Run:
# Stack smashing detected fno-stack-protector  https://stackoverflow.com/questions/1345670/stack-smashing-detected
gcc -fno-stack-protector  -o insert_arrays insert_arrays.c && ./insert_arrays
**/

void insert_position(int arr[]) {
    int i = 0, pos, num;
    size_t n = sizeof(*arr);
    printf("Enter the number to be inserted : ");
    scanf("%d", &num);
    printf("Enter position at which the number is to be added :");
    scanf("%d", &pos);
    for (i = n; i>= pos; i--) {
         arr[i+1] = arr[i];
    }

    arr[pos] = num;
    n = n + 1;  // increase total number of used positions

    // Print the results
    for (int i = 0; i < n - 1; i++) {
        printf("Num: %d \n", arr[i]);
    }



}


int main(int argc, char *argv[]) {
    int arr[3] = {1, 2, 3};
    insert_position(arr);
    return (0);
}