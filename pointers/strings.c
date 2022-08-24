#include <stdio.h>
#include <string.h>

void reverse_string(char *to_reverse) {
	int length_string = strlen(to_reverse);
	
	for (int i = 0; i <= length_string/2; i++) {
		char temporal_variable = to_reverse[i];
		to_reverse[i] = to_reverse[length_string-1-i];
		to_reverse[length_string-1-i] = temporal_variable;
	}
}


int main(void)
{
	char *name = "Filippo";
	printf(reverse_string(name));	

	return 0;
}
