#include "lists.h"
/**
 * check_cycle - check for cycle lists
 * @list: head pointer
 * Return: 0 no cycle 1 has cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *trav;
	listint_t *prev;

	if (!list)
		return (0);
	prev = list;
	trav = list->next;
	while (trav && prev && trav->next)
	{
		if (trav == prev)
			return (1);
		prev = prev->next;
		trav = trav->next->next;
	}

	return (0);
}
