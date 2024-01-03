#include "lists.h"

/**
 * check_cycle - checks for a cycle within a singly linked list
 *
 * @list: head node address
 * Return: (1) has a cycle; otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list, *current;

	current = list;
	while (current->next != temp)
	{
		if (current->next == NULL)
		{
			return (0);
		}
		current = current->next;
	}

	return (1);
}
