#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: linked list to check
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *check1, *check2;

	if (list == NULL)
		return (0);
	check1 = list;
	check2 = list;
	while (check1->next != NULL && check2->next != NULL && check2->next->next != NULL)
	{
		check1 = check1->next;
		check2 = check2->next->next;
		if(check1 == check2)
			return(1);
	}
	return(0);
}
