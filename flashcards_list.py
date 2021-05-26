from flashcards import Flashcard

FLASHCARDS = [
                Flashcard(
                    "Name the 4 methods for solving recurrences.",
                    "1. Substitution method: guess & verify. 2. Iteration method - when the relation isn't too complicated, this one is best. 3. Recursion tree. 4. Master Theorem."),
                Flashcard(
                    "What is the sum rule?",
                    "If f1(n) = O(g1(n)) and f2(n) = O(g2(n)), f1(n) + f2(n) = O(g1(n) + g2(n)),",
                    ),
                Flashcard("What is the loop invariant for BuildMaxHeap?",
                    "At the start of each iteration of the while loop, each node (i+1), ..., len(A) -1 is the root of a max heap.",
                    ),
                Flashcard("What are the 3 procedures used for a binary max-heap?",
                    "1. MaxHeapify. 2. BuildMaxHeap. 3. HeapSort."),
                Flashcard(
                    "What is the height of a tree with n nodes?",
                    "With n nodes, height is the log2(n) (rounded down)."
                    ),
                Flashcard("What is the maximum number of nodes at height h?",
                    "There are at most n/2^(h+1) (rounded down) nodes with height h."
                    ),
                Flashcard(
                    "What is the worst case running time for MaxHeapify?",
                    "Worst case: There is a constant amount of work at each height of the tree. Then it is O(h) for a node of height h.",
                    ),
                Flashcard(
                    "What is the difference between the size and length of a max heap?",
                    "Length of the list/array: n = len(A). Size of the max-heap: The number of elements satisfying the max-heap property."
                    ),
                Flashcard(
                    "What is a min heap?",
                    "For every i besides the root, A[parent(i)] ≤ A[i]."
                    ),
                Flashcard(
                    "What is the height of a binary heap?",
                    "The total height of the tree is the maximum simple path from the root to the bottom (or, to a 'leaf'). The height of a specific node is the maximum simple path from the node to the bottom."
                    ),
                Flashcard(
                    "List 3 properties of exponential functions which are useful for using O(g(n)) notation.",
                    "![](https://i.imgur.com/OWmcUCe.png)"
                    ),
                Flashcard(
                    "What is a binary heap?",
                    "A binary heap is a list that we can see as a nearly-complete binary tree. Each node has 0, 1 or 2 children. If it has only one child, that child must be a left child. The tree is filled on all levels execept, maybe, the bottom level."
                    ),
                Flashcard(
                    "What is the master theorem?",
                    "![](https://i.imgur.com/KIguNdV.png)",
                    ),
                Flashcard(
                    "How does HeapSort beat both InsertionSort and MergeSort?",
                    "InsertionSort is slow but it sorts 'in place', so it doesn't use too much memory. MergeSort is faster but involves creating more than 1 list, so it uses a lot of memory on long lists. HeapSort has the advantages of both: sorts in place, quickly."
                    ),
                Flashcard(
                    "What is the pseudocode for HeapSort?",
                    "![](https://i.imgur.com/NDNp7w6.jpg)"
                    ),
                Flashcard(
                    "What is the max-heap property?",
                    "For every node i other than the root A[parent(i)] >= A[i]"
                    ),
                Flashcard(
                    "What is the max-heapify procedue?",
                    "In order to maintain the max-heap property, we call max-heapify on array A and index i. It runs in time O(log(n)) and assumes the binary trees rooted at Left(i) and Right(i) are also max-heaps - A[i] can be smaller than it's children, so max-heapify allows A[i] to 'float down' the heap."
                    ),
                ]

