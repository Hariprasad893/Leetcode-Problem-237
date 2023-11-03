# Leetcode-Problem-237

This repository consists of the solution to the following problem (as defined in Leetcode), as well as the solution when the head node of the linked list is known:

There is a singly-linked list head and we want to delete a node node in it. You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.Delete the given node. Note that by deleting the node, we do not mean removing it from memory. 

We mean:

1) The value of the given node should not exist in the linked list.

2) The number of nodes in the linked list should decrease by one.

3) All the values before node should be in the same order.

4) All the values after node should be in the same order.

Example:

Input: head = [4,5,1,9], node = 5

Output: [4,1,9]

Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

The link to the problem: https://leetcode.com/problems/delete-node-in-a-linked-list/description/

