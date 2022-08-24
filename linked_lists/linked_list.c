#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct Node {
	int value;
	struct Node *next;
};


typedef struct Node node_t;


node_t print_list(node_t *head) {
	node_t *temporary = head;
	
	while (temporary != NULL) {
		printf("%d - ", temporary->value);
		temporary = temporary->next;
	}
	
	printf("\n");
}


node_t *create_new_node(int value) {
	node_t *result = malloc(sizeof(node_t));
	result->value = value;
	result->next = NULL;
	return result;
}


node_t *insert_at_head(node_t **head, node_t *node_to_insert) {
	node_to_insert->next = *head;
	*head = node_to_insert;
	return node_to_insert;
}


void *insert_after_node(node_t *node_to_insert_after, node_t *new_node) {
	new_node->next = node_to_insert_after->next;
	node_to_insert_after->next = new_node;
}


node_t *find_node(node_t *head, int value) {
	node_t *tmp = head;
	
	while(tmp != NULL) {
		if(tmp->value == value) return tmp;
		tmp = tmp->next;
	}

	return NULL;
	
}


int main(int argc, char **argv)
{
	node_t *head = NULL;
	node_t *tmp;
	
	/*
	tmp = create_new_node(32);
	head = tmp;
	
	tmp = create_new_node(8);
	tmp->next = head;
	head = tmp;
	
	tmp = create_new_node(34);
	tmp->next = head;
	head= tmp;
	*/
	
	for (int i = 0; i < 25; i++) {
		tmp = create_new_node(i);
		insert_at_head(&head, tmp);
	}
	
	tmp = find_node(head, 13);
	printf("Found node with value %d\n", tmp->value);	
	
	insert_after_node(tmp, create_new_node(75));
	
       	print_list(head);
	
	return 0;
}
