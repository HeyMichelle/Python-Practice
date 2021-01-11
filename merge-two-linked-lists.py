##### Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists. ####

# Singly-linked lists are aldread defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#   self.value = x
#   self.next = None

### Understand
    # Your solution should have O(l1.length + l2.length) time complexity
    # remember l1 is not a whole linked list, it's just a pointer to a node in the list
    # example: [l1] 1o -> 2o -> 3o -> [l2] 4o -> 5o -> 6o
    # traverse over the lists
    # we are given the pointer for the first node, l1 (linked-list-node-1)
    # we want to build the new linked list, by taking the nodes and duplicate them as we see them or manipulate them
    # process for merging:
        # merge them in a way that is still in order
        # lower value first, whether l1 or l2, in our case in the example above it's l1
        # why not given node of every list? We are not always given the tail
        # Possible to find but probably won't make a difference in making this problem in particular easier to solve
    # Linked lists process:
        # we want to create a copy of each node and add it to a new linked list
        # eventually l1 will go to none
        # we will have to compare between none and four, so we will add four and move l2 over and so on
        # at the end of a linked list is a None value
    # example of not in order:
        # [l1] 1o -> 2o -> 3o -> [l2] 4o -> 5o -> 6o

### Plan
    # solution 1: 
    # eventually want to return a new list
    # traverse these lists, until they are both None
    # each time we move either L1 or L2 forward:
        # we duplicate that node and add to the end of the new_list


def mergeTwoLinkedLists(l1, l2):
    new_list_head = None
    new_list_tail = None 
    # traverse these lists, until they are both None
        # when do we know that both of the lists are done? What has to be true about l1 and l2? They both point to None
    # each time we move either L1 or L2 forward:
        # we duplicate that node and add to the end of the new_list
        # we would need a lot of if statements for this 

    # when do we know that both of the lists are done? What has to be true about l1 and l2? They both point to None
    while l1 is not None or l2 is not None:
        # first figure out which node we are adding (doing that by comparing the values)
        new_node = None # until we compare them, node is none
        # compare values at L1, and L2
        if not l1:
            # if l2 does not exist, use l2 value
            new_node = ListNode(l2.value)
            l2 = l2.next
        elif not l2:
            # if l2 does not exist, use l1 value
            new_node = ListNode(l1.value)
            l1 = l1.next
            # why is it ok to check if niether of them are None?
        elif l1.value <= l2.value:
            # add L1 node to new_list
            new_node = ListNode(l1.value)
            l1 = l1.next
        else:
            new_node = ListNode(l2.value)
            l2 = l2.next
            # why create a new node? Do you move the values or duplicate them? Easier to duplicate them, only want a list to return new values
            # what is new_list really? What does is have in common with l1 and l2?
                # new_list is just pointing to None, it's a variable that hasn't been touched yet. We can turn that variable into a 3rd pointer to point to the new node
                # can't do None.next, so you add the new_node and handle the case when the new_list is empty
        # actually add the node to the end of the list
        # handle the case when the new_list is empty
        if new_list is None:
            new_list_head  = new_node
            new_list_tail = new_node
                #  the head and tail can point to the same node/data and be two different variables
                # we are making it the head, so we can advance l1
                # which nodes are going to be added to the new list? see above {first figure out...}
                # how to add to a node? with .next
                # what about adding a third item? We don't have track of the tail
                    # the alternative: if we are adding to the end, maybe we want to keep track of the tail also. Doesn't say we can't in directions. 
        else:
            #  add the new node to the EXISTING linked list
            new_list_tail.next = new_node
            new_list_tail = new_node # before this line, the tail was pointing 2 along with the head
            # they are simply pointers that point to a place in memory, you can view it as accessing the list from the head or tail
            # .next applies new_list_tail to the item it's pointing to, and new_list_tail = (equals) you are reassigning what it is pointing to altogether
            #  now go back and advance l1 and l2, how do you move them over to the next value? l1 = l1.next


    return new_list_head
    # pointed to entire linked list which is generated
    # what does it mean to return a linked list?
        # linked lists exist in memory and connect to one another, but it's not like an array where you have a variable that seems like it's all there or like you're actually pushing in a block of data
    # a linked list is just a variable pointing to a node, the first node, and everything connected to it gets dragged around
        # an array you're taking the whole thing and handing it over, a linked list you hand over from a specific node and what comes after
