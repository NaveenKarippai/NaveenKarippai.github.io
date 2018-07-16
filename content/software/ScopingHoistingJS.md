Title: Scoping and Hoisting in JavaScript
Tags: javascript, web-development, software
Date: 2016-11-05 10:20
HeaderImage: https://i.imgur.com/lCZe9cs.jpg
HeaderImageCaption: src: pixabay.com
author: Naveen Karippai
Category: Software
Summary: Learn how variable scoping and hoisting works in JS!
Modified: 2018-07-16 19:30

Scope can be defined as the context in which a variable exists. Scope can be local, or global in JavaScript.

Do you know the value logged on JavaScript console when the following code snippet is run?

<script src="https://gist.github.com/NaveenKarippai/743c9395a1159c86a1244785595c99aa.js"></script>

The answer here is "The Flash". This happens due to Function-level scoping in JavaScript on variable declaration (using var keyword). The developers from Java background may find this surprising!

### Function-level Scope

In JavaScript, variables declared (using var keyword) are function-level scoped. The block-level scoping with loops and conditionals ( if,for, while, switch blocks) don't delimit the scope.

<script src="https://gist.github.com/NaveenKarippai/b2bea061ef940a6cceb0ee0f7ebbded3.js"></script>

### Hoisting

In JavaScript, hoisting is a powerful and an expressive feature by which, JavaScript interpreter moves the function and variable declarations to the top of the current referenced scope. The variable declarations and function declarations are hoisted in JavaScript!

<script src="https://gist.github.com/NaveenKarippai/c7e62578e89f12c80113d6496feecb8e.js"></script>

The function body is hoisted along with function declaration. In the code snippet, the function declaration is moved to the top of scope through hoisting (above return statement). The equivalent code interpreted would be:

<script src="https://gist.github.com/NaveenKarippai/74d511727c4b9dce4988b4000fff019c.js"></script>

### An aside:

The assignment part of variable and function expressions are not hoisted, but only the declarations are!

<script src="https://gist.github.com/NaveenKarippai/6103185310c90f12fd0cb04078a35028.js"></script>

The equivalent code interpreted would be:

<script src="https://gist.github.com/NaveenKarippai/ab23d059525b4575ef2ab67e118d2a8b.js"></script>

### What's new in ECMAScript 2015 (ES6)?

ECMAScript 2015 introduced keywords: let and const for block-level scoping in JavaScript.

<script src="https://gist.github.com/NaveenKarippai/2a38642b2c0bf8efcfd853e84db71fa2.js"></script>

The variables declared with let or const keyword have the block in which they are declared, as well as any continued sub-blocks as their scope.

### Hoisting in ES6

In ECMAScript 2015, let and const keyword variable declarations will hoist the variable to top of the block. However, referencing the variable in the block before variable declaration results in ReferenceError . The difference between var/function declarations and let/const declarations is in the initialization portion. The former are initialized with undefined or generator function right when binding is created at top of the scope, while the latter stay uninitialized until let/const statement is run. The variable is called to be in a "temporal dead zone" from start of the block until the declaration is executed.

<script src="https://gist.github.com/NaveenKarippai/bc6a1d0069331e7f5905058e118f2e10.js"></script>

### Variable declaration keywords: 'var' v/s 'let'

<script src="https://gist.github.com/NaveenKarippai/90d6e72090bda590d33280beeca33181.js"></script>

This happens due to block-level scoping of let variable declaration.

#### Summary:

Hoisting is a very powerful feature in JavaScript language. This provides high flexibility to the language, if used necessarily. Also, a strong understanding of scoping in JavaScript can help us to avoid many common mistakes.

#### Reference:

This article was originally posted on [medium](https://medium.com/@naveenkarippai/scoping-and-hoisting-in-javascript-2c2e82107427)

### Bonus:

Are you new to Linux and wants to do Linux Command Line? Get my Udemy course on "Linux Command Line for Beginners" at a discount price (limited offer) by clicking [here](https://www.udemy.com/linux-command-line-for-beginners-42/?couponCode=YELLOW-ELEPHANT).

