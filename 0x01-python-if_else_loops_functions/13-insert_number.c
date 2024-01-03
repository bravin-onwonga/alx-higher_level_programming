#include "lists.h"

/**
 * insert_node - inserts a node into a singly-linked list
 *
 * @head: head node
 * @number: integer
 * Return: address of new node (success)
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *curr, *prev = NULL;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	curr = *head;
	while (curr != NULL)
	{
		if (curr->n > number)
		{
			new_node->next = curr;
			prev->next = new_node;
			return (new_node);
		}
		prev = curr;
		curr = curr->next;
	}
	new_node->next = curr;
	prev->next = new_node;
	return (new_node);
}
