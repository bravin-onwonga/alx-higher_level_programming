#include "lists.h"

/**
 * check_cycle - checks for a cycle within a singly linked list
 * @list: head node address
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *curr = list, *next = list;

	if (list == NULL)
		return (0);

	while (curr != NULL && curr->next != NULL)
	{
		next = next->next;
		curr = curr->next->next;

		if (next == curr)
			return (1);
	}

	return (0); /* No cycle found */
}
