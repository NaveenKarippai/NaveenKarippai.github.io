Title: Learning how references work in JavaScript
Tags: javascript, software
Date: 2016-11-13 10:20
HeaderImage: https://i.imgur.com/KCxRUwM.jpg
HeaderImageCaption: src: pixabay.com
author: Naveen Karippai
Category: Software
Summary: Quick dive into references in JavaScript

### TL;DR:

There are NO pointers in JavaScript and references work different from what we would normally see in most other popular programming languages. In JavaScript, it's just NOT possible to have a reference from one variable to another variable. And, only compound values (Object, Array) can be assigned by reference.

![memegenerator](https://i.imgur.com/wd35HwV.jpg)
{.adjust-width}

src: memegenerator
{.caption}

### Bottom line:

* The typeof value assigned to a variable decides whether the value is stored with assign-by-value or assign-by-reference

* On variable assignment, the scalar primitive values (Number, String, Boolean, undefined, null, Symbol) are assigned-by-value and compound values (Object, Array) are assigned-by-reference

* The references in JavaScript only point at contained values and NOT at other variables, or references

* In JavaScript, scalar primitive values (Number, String, Boolean, undefined, null, Symbol) are immutable and compound values (Object, Array) are mutable

### Quick example on assign-by-value:

In the code snippet below, we are assigning scalar primitive value (number) to a variable and thus assign-by-value applies here. Firstly, the variable batman is initialized and when the variable superman is assigned with the value stored in variable batman, it creates a new copy of the value and stores it. When the variable superman is modified, variable batman is left unaffected as they point to distinct values.

<script src="https://gist.github.com/NaveenKarippai/170a15479ed69ffcc2851c18b6c7022e.js"></script>

![UML](https://cdn-images-1.medium.com/max/800/1*QsD4yzqkNYgA40-m4mAgpg.png)
{.adjust-width}

Tool: UMLet (GNU Linux client)
{.caption}

### Quick example on assign-by-reference:

In the code snippet below, we are assigning a compound value (array) in a variable and thus assign-by-reference applies here. The variables flash and quicksilver are references to the same value (aka shared value). The references will point to the updated value when the shared value is modified .

<script src="https://gist.github.com/NaveenKarippai/92745155e8b565286b297907aecea7a3.js"></script>

![UML](https://cdn-images-1.medium.com/max/800/1*jsPkapD8J8q022ev6NVsHw.png)
{.adjust-width}

Tool: UMLet (GNU Linux client)
{.caption}

### How to create a new reference?

When the compound value in a variable is reassigned, a new reference is created. In JavaScript, unlike in most other popular programming languages, the references are pointers to value stored in variables and NOT pointers to other variables, or references.

<script src="https://gist.github.com/NaveenKarippai/8c8c8bd36c4d47f97ef8caaa08426743.js"></script>

![UML](https://cdn-images-1.medium.com/max/800/1*D3uCMwUX6xvZNSY4azfhLg.png)
{.adjust-width}

Tool: UMLet (GNU Linux client)
{.caption}

### How references work when values are passed as function parameters?

In the code snippet below, variable magneto is a compound value (Array object), thus it is assigned in variable (function argument) x with assign-by-reference. The Array.prototype.push method invoked inside IIFE mutates the value in variable magneto through JavaScript reference. But, the reassignment of variable x creates a new reference, and further modifications on it does NOT affect the reference to variable magneto.

<script src="https://gist.github.com/NaveenKarippai/4f187369a0ba3c3aa34a08937ea7d5c8.js"></script>

### How to change the original value in a compound variable passed as function argument through JavaScript reference?

The solution here would be to modify the existing compound value where the reference is pointing to. In the code snippet below, variable wolverine is a compound value (Array object) and on IIFE invocation, variable (function argument) x is assigned by reference. The Array.prototype.length property can be used to create an empty array by setting its value to 0. Thus, variable wolverine is changed to the new value set in variable x through JavaScript reference.

<script src="https://gist.github.com/NaveenKarippai/e5bd70413782da568c9d7159e800403d.js"></script>

### How to store a compound value through assign-by-value?

The solution here would be to make a manual copy of the compound value and then assign the copied value to a variable. Therefore, the reference of assigned value does NOT point back to the original value. The recommended approach to create a (shallow) copy of the compound value (Array object) is to invoke Array.prototype.slice method on it with no arguments passed.

<script src="https://gist.github.com/NaveenKarippai/2683e61649786928524dcb5f7caef725.js"></script>

![UML](https://cdn-images-1.medium.com/max/800/1*2ADFn3r1_AH0CbW1YmFzlw.png)
{.adjust-width}

Tool: UMLet (GNU Linux client)
{.caption}

### How to store a scalar primitive value through assign-by-reference?

The solution here would be to wrap scalar primitive value in a compound value (Object, Array) as its property value. Thus, it can be assigned-by-reference. In the code snippet below, scalar primitive value in variable speed is set as a property on object flash. Therefore, it is assigned-by-reference on IIFE invocation to variable (function argument) x.

<script src="https://gist.github.com/NaveenKarippai/8cf73227fd4b01ab8205bde010397f4b.js"></script>

### An aside:

In JavaScript, the scalar primitive values are immutable while compound values are mutable.

<script src="https://gist.github.com/NaveenKarippai/22a0c9aaf6f2fe3d7d09d9f9e116fe01.js"></script>

![memegenerator](https://cdn-images-1.medium.com/max/800/1*G9y7ExBwqWnSEqAH4nov9Q.jpeg)
{.adjust-width}

src: memegenerator
{.caption}

### Summary:

A good understanding of references in JavaScript can help developers to avoid many common mistakes and write better code.

Happy coding!!

#### Reference: 

This article was originally published on [medium](https://medium.com/@naveenkarippai/learning-how-references-work-in-javascript-a066a4e15600)

### Bonus:

Are you new to Linux and wants to do Linux Command Line? Get my Udemy course on "Linux Command Line for Beginners" at a discount price (limited offer) by clicking [here](https://www.udemy.com/linux-command-line-for-beginners-42/learn/v4/?couponCode=YELLOW-ELEPHANT).
