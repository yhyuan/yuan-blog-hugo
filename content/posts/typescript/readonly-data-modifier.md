---
title: readonly data modifier in TypeScript
date: '2023-07-25'
tags: ['TypeScript']
draft: false
description: The artical descript how to use readonly as data modifier in TypeScript
---

## Question

Recently, I run into a TypeScript problem. Here is the code snippet. 

```Typescript
interface Student {
  readonly ids: number[],
}
const ids: readonly number[] = [1, 2, 3];
let student: Student = { ids: ids };
```

The compiler complains with the following error message:
```
The type 'readonly number[]' is 'readonly' and cannot be assigned to the mutable type 'number[]'.
```

## Solution
The previous code snippet actually define **ids** in **interface Student** as type: **number[]**. So we can add **readonly** in front of **number[]**.

```Typescript
interface Student {
  readonly ids: readonly number[],
}
const ids: readonly number[] = [1, 2, 3];
let student: Student = { ids: ids };
```

The **readonly** in front of **ids** only means that we can not assign ids again after it is initialized. So the last line of the following code snippet will fail. 
```Typescript
interface Student {
  readonly ids: readonly number[],
}
const ids: readonly number[] = [1, 2, 3];
let student: Student = { ids: ids };
student.ids = [1];
```
If you want to fix it, you need to remove the **readonly** in front of **ids**, the following code snipeet will has no error.  
```Typescript
interface Student {
    ids: readonly number[],
}
const ids: readonly number[] = [1, 2, 3];
let student: Student = { ids: ids };
student.ids = [1];
```
