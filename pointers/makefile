file: file.c
	gcc file.c -o file

file_function: function_struct.c
	gcc function_struct.c -o file_function	

run_function: file_function
	./file_function

run: file
	./file

clean_function: file_function
	rm -f file_function

clean: file
	rm -f file
