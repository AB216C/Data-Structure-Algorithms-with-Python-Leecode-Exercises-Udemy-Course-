# Linkedlist
- Linked list doesn't have index
- With a List, all nodes are next to each other in memory and can be accessed using index
- For Linked List, nodes are spread all over the place
- First node is called head
- Last node is called tail
- First node is connected to the next
- Last node is connected to none

Head -> A → B -> C -> null(none)
                 ↑
                 Tail
 * A,B,C are nodes

# Big(O) Linked List
   ## Preppending& Appending a new node to a Linked list(begining or end of the linked List)
   - Step1: Last node in a linked list will point to the new node
   - Step2: Tail or Head will point to a new node
    * All together will create a new Linked List- New Linked list will be O of 1 or O(1) because No matter how many nodes are added at the beginning or end, the number of operations will remain the same

    ## Removing a node from the end of the tail
    * This is more complicated

    - Step 1: Remove a node
    - Stop 2: Make a tail point to the last node

    * How to make a tail point to the last node

    - Step 1: Set a tail pointer equal to something else that is pointing to the last node
    - Stop 2: Iterate from from head to the List untill you get to the pointer 
    - Step 3: Set tail equal to that pointer

    Notes:Since this require iterating the entire list,this is reffered to as O of n or O(n)

    ## Removing a node from the beginning of the linked List
    * This is not complicated
     - Step 1 : Set Head to point to the next node in the Linked List
     - Step 2 : Remove the node

     * This is O of 1 or O(1)

     ## Adding an item somewhere in the middle of the linkedlist
     - Step1 : Iterate untill you reach a node in the middle you want to attach a new item
     - Step2 : Make new item arrow to point to the node right next to the middle node
     - Step2 : Set a pointer of middle node equal to the pointer of a new item
     - Step3 :  Add a new item

     * This is O of n  or O(n)-iteration is required


     ## Removing the item in the middle of the Linkedlist

     - Step1: Iterate through the linked list until you reach the node before the one you want to remove
       if removing C from A, B, C,D stop at B
     - Step2: Change the arrow of the B node so it skips C and points to D node. By skipping C node will remove it from the chain
    
     * This is O of n  or O(n)-iteration is required


     ## Look up the value from a linkedlist

     - Step1: Iterate through the linked list until you reach index of the value you're looking for

     * This is O of n  or O(n)-iteration is required




    




