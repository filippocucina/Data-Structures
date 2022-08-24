#include <stdio.h>
#include <string.h>


int main(void)
{
	char *string = "Hello Reddit";
	char *my_pointer = (string + 6);

	printf("%s\n", string);
       	printf("%c\n", *my_pointer);	

	return 0;
}
