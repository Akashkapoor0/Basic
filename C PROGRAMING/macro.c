#include <stdio.h>

#define PI 3.14159
#define AREA(r) (PI * (r) * (r))

int main() {
    float radius = 5.0;
    printf("Area of the circle with radius %.2f is %.2f\n", radius, AREA(radius));
    return 0;
}
