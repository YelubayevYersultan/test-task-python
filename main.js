// Task 1: Check if number > 7
let number = parseInt(prompt("Enter a number:"));
if (number > 7) {
    console.log("Hello");
}

// Task 2: Check if name is "John"
let name = prompt("Enter a name:");
if (name === "John") {
    console.log("Hello, John");
} else {
    console.log("There is no such name");
}

// Task 3: Numeric array input and print multiples of 3
let input = prompt("Enter numbers separated by spaces:");
let numbers = input.split(" ").map(Number);

console.log("Numbers that are multiples of 3:");
numbers.forEach(n => {
    if (n % 3 === 0) {
        console.log(n);
    }
});
