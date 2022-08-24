#include <stdio.h>
#include <stdint.h>
#include <string.h>

int get_string_length(char * str) {
	int offset = 0;
	while (str[offset] != 0) {
		offset++;
	}
	return offset;

}

void copy_string(char *from, char *to) {
	int offset = 0;
	while

}


int main(void)
{
		
	char *str1 = "Hello World!";
       	char str2[] = "Hello World!";

	printf("Hello World!\12\12");	
	printf("Print a Backslash Character \\ \n");

	printf("%s has length %d bytes\n", str1, get_string_length(str1));
	printf("%s has length %lu bytes\n", str1, strlen(str1));

	return 0;
}
