# Notes

## Programming Fundamentals

- Data Structures:
  - Queue: good for processing events that should be FIFO
  - Stack: good when needing to go back, undo functionality, news feeds
  - Array: good when accessing data by index, when ordering is important. Very fast since size is set and stored in same memory space.
  - Array List: similar to an Array, but dynamically sized. Can hold any type of data.
  - List: Simliar to an array, but provides more simplified data access, sorting, etc
  - Linked List: simliar to stack, but can also be doubly linked
  - Hash Table/Hash Map/Dictionary: good when accessing data by key, when ordering is not important
  - Tree/Binary Search Tree: good for storing data based on less than/greater than
  - Graph: good when nodes may require multiple links together, for things like route optimization
- Algorithms:
  - Sorting:
    - Quick sort (log)
    - Bubble sort (log)
    - Merge sort (n^2)
    - Radix sort (n^k)
  - Searching:
    - Linear (n): searchs one by one
    - BFS (n): uses queue, traverses level by level
    - DFS (n): uses stack, searches by depth

## Object Oriented Programming

- 4 Tenants of OOP
  - Encapsulation: grouping related methods, properties, etc into a single object
  - Inheritance: the ability to gain/inherit methods and properties from a parent class
  - Polymorphism: the ability to override and overload methods within a class or inherited classes
  - Abstraction: the process by which a developer hides everything other than the relevant data about an object in order to simplify and increase efficiency
- Namespaces: used to organization and provide high-level separation of code
- Boxing/Unboxing: process of converting a value type to and from an object type
- Data Types:
  - Value Type: variable contains the value
  - Reference Type: variable contains the address to the value being stored
- Mutable: where data can be changed after it is created, without the need to recreate in new memory. (ex: StringBuilder)
- Immutable: where data cannot be changed after it is created. (ex: string)
- Virtual Methods: methods that you can override in child classes.
- Abstract Classes vs. Interfaces:
  - Both provide a building blocks for classes
  - Both abstract classes and interfaces can not be instantiated
  - Abstract classes can contain method decorations, interfaces cannot contain method declarations
  - A class can only inherit from one abstract class, but can implement more than one interface
  - A class can partially implement an abstract class, but must fully implement an interface
- Static: Classes cannot be instanciated or inherited
- Sealed: Classes can be instantiated, but not inherit
- Readonly: Value cannot be modified (like const in JavaScript)
- Access Modifiers:
  - Private: accessible only inside its own class
  - Protected: accessible inside its own class and any classes derived from this class
  - Public: accessible from anywhere
  - Internal: accessible from anywhere within its own assembly
- Benefits of Dependency Injection:
  - Encourages decoupling of code, improving maintainability
  - Improves reuse
  - Improves testability
  - Improves readability
  - Improves extensibility
  - Reduces boilerplate code

## Web Dev

- REST best practices:
  - Use JSON format
  - Use nouns instead of verbs for endpoints
  - Name collections in plural (ex: /posts/1)
  - Use HTTP status codes in error handling
  - Use nesting on endpoints to show relationship
  - Use filtering, sorting, and pagination on data requests (ex: ?tags=1, ?sort=tags, ?page=1&per_page=100)
    - Can use aliases to
  - Use clear versioning
  - Provide accurate documentatation
- Idempotent REST methods (subsequent requests provide same result):
  - GET, PUT, DELETE: Idempotent
  - POST: NOT Idempotent (new object is created with every call)
