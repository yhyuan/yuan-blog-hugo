---
title: "Rust Smart Pointer Study Notes"
date: 2023-11-09T17:09:00-05:00
tags: ['rust']
draft: false
---

## Rust Smart Point
### Concepts
Ownership, Borrowing (`&String`, `&mut String`), Lifetimes (`&'a str`)
```
struct Person<'a> {
    name: &a' str,
}
```
### Why use Smart Points
* Automatic memory management
* Prevent data races
* Add super powers to pointers: Additional functionality, e.g. shared ownership/reference counting.  
* Simplify code

### Box`<T>`
allocates memory on the heap and allows to move the ownership of value from the stack to the heap. 
#### Use cases
* Storing large data structure, which may cause stack overflows. 
* Transferring ownership between different parts of code. 
* Making enum representations more uniform
* Creating recursive data structure, such as linked list and trees. 
#### Linked List
```rust
#[derive(Debug)]
struct List(Option<Box<Item>>);

#[derive(Debug)]
struct Item(i32, Option<Box<Item>>);

impl List {
    fn append(&mut self, value: i32) {
        let mut current = &mut self.0;

        while let Some(ref mut next_item) = current {
            current = &mut next_item.1;
        }

        let item = Item(value, None);
        *curent = Some(Box::new(item));
    }
}

fn main () {
    let mut l = List(None);
    l.append(1);
    l.append(2);

    println!("{l:?}");
}
```

### Rc`<T>`
reference counting. enable shared ownership of a value, allowing multiple parts of your code to have read-only access to the same data without cloning. 

#### Example
```rust
use std::rc::Rc;

struct Node {
    value: i32,
    next: Option<Rc<Node>>,
}

fn main() {
    let node1 = Rc::new(Node {value: 1, next: None });
    let node2 = Rc::new(Node {value: 2, next: Some(Rc::clone(&node1)) });
    let node3 = Rc::new(Node {value: 3, next: Some(Rc::clone(&node2)) });

    println!("Node 1: {:?}", node1);
    println!("Node 2: {:?}", node2);
    println!("Node 3: {:?}", node3);
}
```

#### Use cases
* Implementing tree-like structures. 
* Storing shared configuration data
* Sharing large imutable data structures, such as lookup tables or dictionaries. 

#### Limitations
* Rc<T> is not thread-safe. Use Arc<T> instead. 
* Rc<T> does not support interior mutability out of the box. You will need RefCell<T> with Rc<T> to get mutable access to the underlying data. 

### Arc`<T>` 
share the data structures between threads, at cost of performance. 
### Example
```rust
use std::sync::Arc;
use std::thread;

fn main() {
    let data = Arc::new("Hello World");
    let mut handles = vec![];

    for _ in 0..3 {
        let data_clone = Arc::clone(&data);
        let handle = thread::spawn(move || {
            println!("Data in thread: {}", data_clone);
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
}
```
### Other
Mutex<T> and RwLock<T>

### RefCell`<T>`
interior mutability means that you can mutate the dat astored in a RefCell<T> even if the RefCell<T> itself is not mutable. 
It moves the borrowing rules enforcement from compile-time to run time. 
#### Example
```rust
use std::cell::RefCell;

fn main() {
    let data = RefCell::new(42);
    {
        let mut data_ref_mut = data.borrow_mut();
        *data_ref_mut += 1;
    }

    let data_ref = data.borrow();
    println!("data: {}", data_ref);
}
```

### Mutex`<T>`
provides exclusive, mutable access to data in a multi-threaded environment. mutual exclusion and is used to protect the shared data from data races. Only one writable lock. 
#### Example
```rust
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let coutner_clone = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter_clone.lock().unwrap();
            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("counter: {}", *counter.lock().unwrap());
}
```

### RwLock`<T>`
#### Mutex`<T>` vs RwLock`<T>`
* Mutex: only one thread can access the data in a time, whether it is for reading or writing. The data is frequently updated and there is no need to separate the write and read locks.
* RwLock allows multiple threads to read the data in the same time, but requires esxclusive access for writing. The data is more frequently read than it is updated. Allowing multiple concurrent readers can improve the performance. 

### Drop, Deref, DerefMut trait
