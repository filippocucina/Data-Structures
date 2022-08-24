#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
	for (int i = 0; i <= argc; i++) {
		printf("Argument %d - %s, %i, %f \n", i, argv[i], atoi(argv[i]), atof(argv[i]));
	}	

	return 0;
}
