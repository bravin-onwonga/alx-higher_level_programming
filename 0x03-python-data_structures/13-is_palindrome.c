#include "lists.h"

int check_for_palindrome(listint_t *temp, int len);

/**
 * is_palindrome - checks if a singly-list is a palindrome
 *
 * @head: head node
 * Return: 1 if palindrome; otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr, *temp;
	int len_list = 0, res;

	if (*head == NULL)
		return (1);

	curr = *head;
	while (curr != NULL)
	{
		len_list++;
		curr = curr->next;
	}

	temp = *head;

	res = check_for_palindrome(temp, len_list);

	return (res);
}

int check_for_palindrome(listint_t *temp, int len)
{
	int arr[len], i = 0, mid_point, k = 0;

	while (i <= len && temp != NULL)
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
			return (0);
		}
		k++;
		i--;
	}
	return (1);
}
