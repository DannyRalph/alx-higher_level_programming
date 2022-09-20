#include "lists.h"

/**
 * check_cycle - A function in C that checks if a
 *               singly linked list has a cycle in it
 * @list: pointer to the beginning of the the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list;
	check = current->next;

	while (current && check->next && check->next->next)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
