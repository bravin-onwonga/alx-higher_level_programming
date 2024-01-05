#include "lists.h"

/**
 * check_cycle - checks for a cycle within a singly linked list
 *
 * @list: head node address
 * Return: (1) has a cycle; otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *curr = list, *temp;
	int i = 1, j;

	if (list == NULL)
		return (0);

	temp = list->next;
	while (curr != NULL)
	{
		j = 0;
		while (j < i)
		{
			if (curr == temp)
			{
				return (1);
			}
			temp = temp->next;
			j++;
		}
		curr = curr->next;
		i++;
	}

	return (0);
}
