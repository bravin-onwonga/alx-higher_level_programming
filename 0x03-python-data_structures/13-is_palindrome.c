#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *curr, *temp;
	int len_list = 0, i = 0, k = 0;
	char *arr;

	if (*head == NULL)
		return (1);

	curr = *head;
	while (curr != NULL)
	{
		len_list++;
		curr = curr->next;
	}

	arr = malloc(sizeof(char *) * len_list);
	temp = *head;
	while (i <= len_list && temp != NULL)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i--;

	while (k < i / 2)
	{
		if (arr[k] != arr[i])
		{
			return (0);
		}
		k++;
		i--;
	}
	return (1);
}
