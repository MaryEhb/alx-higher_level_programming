#include "lists.h"
#include <stdio.h>
/**
 * print_dlistint -  prints all the elements of a dlistint_t list.
 * @h: head
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	int count = 0;
	dlistint_t *tmp = (dlistint_t *)h;

	if (h)
	{
		while (tmp)
		{
			printf("%d\n", tmp->n);
			tmp = tmp->next;
			count++;
		}
	}
	return (count);
}
