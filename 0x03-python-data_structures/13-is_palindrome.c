#include "lists.h"

/**
 * is_palindrome - yes is 1 no is 0
 * @head: the list head
 * Return: 1 is pal 0 isnot
 */
int is_palindrome(listint_t **head)
{
	int size, i;
	int *array;
	listint_t *trav;

	size = list_int(head);
	array = malloc(sizeof(int) * size);
	trav = *head;
	if (size % 2)
		return (0);
	for (i = 0; i < size; i++)
	{
		array[i] = trav->n;
		trav = trav->next;
		if (i >= size / 2)
		{
			if (array[i] != array[size - i - 1])
				return (0);
		}
	}
	return (1);


}

/**
 * list_len - list len
 * @head: list head
 * Return: the size
 */
int list_len(listint_t **head)
{
	listint_t *trav;
	int len = 0;

	trav = *head
	while (trav)
	{
		len++;
		trav = trav->next;
	}
	return (len);
}
