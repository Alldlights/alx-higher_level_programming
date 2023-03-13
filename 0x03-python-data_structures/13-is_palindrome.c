#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if list is palindrome
 * @h: pointer to the pointer of first node of the listint_t list
 * Returns: 0 if not plaindrome
 * 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int values[9999], i = 0, c = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	node = *head;
	if (!node->next)
	{
		return (1);
	}
	while (node)
	{
		values[i] = node->n;
		node = node->next;
		i++;
	}
	i--;
	while (i >= 0 && c <= i)
	{
		if (values[i] != values[c])
		{
			return (0);
		}
		i--;
		c++;
	}
	return (1);
}
