#include "lists.h"

/**
 * check_cycle - checks for a cycle within a singly linked list
 *
 * @list: head node address
 * Return: (1) has a cycle; otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list, *temp;
	int i = 0, j = 0;

	current = list;
	while (current->next != list)
	{
		if (current->next == NULL)
		{
			return (0);
		}

		temp = list;
		while (j <= i)
		{
			if (current->next == temp)
				return (1);
			temp = temp->next;
			j++;
		}
		current = current->next;
		i++;
	}

	return (1);
}
