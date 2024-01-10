#include "lists.h"

int get_digit_from_end(listint_t *curr, int n);

/**
 * is_palindrome - checks if a singly-list is a palindrome
 *
 * @head: head node
 * Return: 1 if palindrome; otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *curr, *temp;
	int len_list = 0, i = 0, n, digit;

	if (*head == NULL)
		return (1);

	curr = *head;
	while (curr != NULL)
	{
		len_list++;
		curr = curr->next;
	}
	curr = *head;
	temp = *head;

	n = len_list - 1;

	while (i < (len_list / 2))
	{
		digit = get_digit_from_end(temp, n);
		if (curr->n != digit)
		{
			return (0);
		}
		n = n - 2;
		temp = temp->next;
		curr = curr->next;
		i++;
	}

	return (1);
}

/**
 * get_digit_from_end - gets the digit from the other end to compare
 *
 * @curr: pointer to a node
 * @n: number of iterations
 * Return: integer at node
 */

int get_digit_from_end(listint_t *curr, int n)
{
	int i = 0;

	while (i < n)
	{
		curr = curr->next;
		i++;
	}

	return (curr->n);
}
