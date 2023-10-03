#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - add node to linkedlist
 * @listint_t: linked list pointer to head pointer
 * @number: to be added
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{

	listint_t *new;
	listint_t *i = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (0);

	new->n = number;
	new->next = 0;

	while()

}
