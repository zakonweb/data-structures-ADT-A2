# Understanding Queues

Queues are a fundamental data structure that follows the **First-In-First-Out** (FIFO) principle. They are commonly used to manage data in a sequential manner. In this guide, we'll explore the concept of queues, their operations, and different implementations.

## Anatomy of a Queue

A queue is a collection of elements where the **rear** (also known as the tail) is responsible for adding elements, and the **front** (also known as the head) is responsible for removing elements. The elements are added at the rear and removed from the front, similar to how people wait in a line or a queue.


## Linear Queue

A linear queue is the simplest implementation of a queue. It is implemented using a fixed-size array or a dynamic array. The key characteristic of a linear queue is that it has a fixed capacity, and once it becomes full, it cannot accept any more elements. If elements are dequeued from the front, new elements can be enqueued at the rear.

![Linear Queue](https://simplerize.com/wp-content/uploads/2023/01/linear_queue_diagram-2.svg)

## Circular Queue

A circular queue is an extension of the linear queue where the rear and front "wrap around" to the beginning of the array when they reach the end. This allows efficient utilization of the available space in the queue. In a circular queue, the indices of the rear and front pointers are updated modulo the size of the array to ensure the circular behavior.

![Circular Queue](https://cdn.programiz.com/sites/tutorial2program/files/circular-increment.png)

### Circular Queue Operations

In addition to the common queue operations mentioned earlier, circular queues have an additional consideration:

#### Enqueue (Addition)

When enqueuing an element in a circular queue, the rear pointer is incremented, and if it reaches the end of the array, it wraps around to the beginning. If the rear and front pointers become equal after the increment, it means the queue is full.

![Enqueue Operations](https://afteracademy.com/images/queue-and-its-basic-operations-circular-array-enqueue-operation-80a129832af41e63.png)

#### Dequeue (Removal)

When dequeuing an element in a circular queue, the front pointer is incremented, and if it reaches the end of the array, it wraps around to the beginning. If the rear and front pointers become equal after the increment, it means the queue is empty.

![Dequeue Operations](https://afteracademy.com/images/queue-and-its-basic-operations-circular-array-dequeue-operation-4ae74edd676059d4.png)

## Implementations

### Array-based Queue

In the array-based implementation, a fixed-size array is used to store the elements of the queue. The front and rear pointers keep track of the indices in the array. Elements are enqueued at the rear and dequeued from the front. In a circular array-based implementation, the rear and front pointers wrap around to the beginning when they reach the end of the array.

### Linked List-based Queue

In the linked list-based implementation, a dynamic linked list is used to represent the queue. Each node in the linked list contains the element and a pointer to the next node. The front and rear pointers point to the first and last nodes of the linked list, respectively. Elements are enqueued at the rear and dequeued from the front.

![Queue Implementations](https://www.prodevelopertutorial.com/wp-content/uploads/2019/05/12-1.png)

## Summary

Queues are a simple yet powerful data structure that follows the First-In-First-Out principle. They allow efficient insertion and removal of elements, making them suitable for applications where data needs to be processed in the order it was added. Circular queues provide a more efficient
