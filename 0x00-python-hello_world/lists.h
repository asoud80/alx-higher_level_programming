#ifndef LISTS_H

#define LISTS_H

#include <stdlib.h>


/**
 * struct listint_s - the Singly_Linked_List
 *
 * @n: Int
 *
 * @next: it will Points To Next Node
 * Description: the Singly_Linked_List_Node_Structure
 *
 * for python Project
 */

typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
