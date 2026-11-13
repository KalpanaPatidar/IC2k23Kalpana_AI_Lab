#include <stdio.h>

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

void solve_water_jug_problem(int jug1_capacity, int jug2_capacity, int target) {
    if (target > jug1_capacity && target > jug2_capacity) {
        printf("Target cannot be measured with these jug capacities.\n");
        return;
    }

    if (target % gcd(jug1_capacity, jug2_capacity) != 0) {
        printf("Target cannot be measured.\n");
        return;
    }

    int a = jug1_capacity;
    int b = 0;

    printf("\nSolution steps:\n");
    printf("(%d, %d)\n", a, b);

    while (a != target && b != target) {
        if (a == 0) {
            a = jug1_capacity;
            printf("Fill jug 1 -> (%d, %d)\n", a, b);
        } else if (b == jug2_capacity) {
            b = 0;
            printf("Empty jug 2 -> (%d, %d)\n", a, b);
        } else {
            int pour_amount = (a < jug2_capacity - b) ? a : (jug2_capacity - b);
            a -= pour_amount;
            b += pour_amount;
            printf("Pour from jug 1 to jug 2 -> (%d, %d)\n", a, b);
        }
    }

    printf("\nTarget reached: (%d, %d)\n", a, b);
}

int main() {
    int jug1, jug2, target;

    printf("Enter capacity of Jug 1: ");
    scanf("%d", &jug1);

    printf("Enter capacity of Jug 2: ");
    scanf("%d", &jug2);

    printf("Enter target amount: ");
    scanf("%d", &target);

    solve_water_jug_problem(jug1, jug2, target);
    return 0;
}
