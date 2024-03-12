#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list ti be checked
 *
 * Return: always 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr, *fast_ptr;

	if (!list)
	{
		return (0);
	}
	slow_ptr = list;
	fast_ptr = list -> next;
	while (fast_ptr && slow_ptr && fast_ptr->next)
	{
		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	return (0);
}
