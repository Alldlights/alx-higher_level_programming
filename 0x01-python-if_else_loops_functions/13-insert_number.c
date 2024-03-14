#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number int a sorted singly linked list
 * @head: Pointer to pointer of head node
 * @number: number to insert to the list
 * Return: address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;

	return (new);
}
