#include "lists.h"


/**
 * check_cycle - it will Check whther Linked_List Contains Cycle
 *
 * @list: Linked_List To be Check
 * Return: in case The List has a cycle return 1, otherwise 0
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
