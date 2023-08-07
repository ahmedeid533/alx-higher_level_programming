/**
 * check_cycle - check for cycle lists
 * @list: head pointer
 * Return: 0 no cycle 1 has cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *trav;
	listint_t *prev;

	prev = head;
	trav = head->next;
	while (trav != NULL && prev != NULL)
	{
		if (trav->next == prev)
			return (1);
		prev = prev->next;
		trav = trav->next;
	}

	return (0);
}
