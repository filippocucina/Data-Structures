#include <stdio.h>
#include <string.h>
#include <stdlib.h>


struct point {
	int x, y;
	void (*print)(const struct point*);

};

void print_x (const struct point *p) {
	printf("x = %d\n", p->x);

}

void print_y (const struct point *p) {
	printf("y = %d\n", p->y);
}


int main(int argc, char **argv) 
{
	struct point p1 = {2, 7, print_x};
	struct point p2 = {7, 1, print_y};

	p1.print(&p1);
	p2.print(&p2);

	return 0;

}
