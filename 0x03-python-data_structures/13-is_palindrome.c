#include "lists.h"

/**
 * is_palindrome - checks if a singly-list is a palindrome
 *
 * @head: head node
 * Return: 1 if palindrome; otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr, *temp;
	int len_list = 0, i = 0, k = 0, mid_point;
	int *arr;

	if (*head == NULL)
		return (1);

	curr = *head;
	while (curr != NULL)
	{
		len_list++;
		curr = curr->next;
	}
	arr = malloc(sizeof(int) * len_list);

	if (arr == NULL)
		exit(EXIT_FAILURE);

	temp = *head;
	while (i <= len_list && temp != NULL)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	i--;
	mid_point = i / 2;

	while (k <= mid_point)
	{
		if (arr[k] != arr[i])
		{
			free(arr);
			return (0);
		}
		k++;
		i--;
	}
	free(arr);
	return (1);
}
