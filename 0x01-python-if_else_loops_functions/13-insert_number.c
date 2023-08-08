#include "lists.h"

/**
 * insert_node - insert at sorted
 * @head: head pointer
 * @number: the inserted number
 * Return: the pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *trv;
	listint_t *pre;

	new = malloc(sizeof(listint_t));
	new->n = number;
	pre = *head;
	if (*head == NULL)
	{
		*head = new;
		pre->next = NULL;
		return (new);
	}
	trv = pre->next;
	if (pre->n > new->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (trv->n < new->n)
	{
		trv = trv->next;
		pre = pre->next;
	}
	pre->next = new;
	new->next = trav;
	return (new);
}
