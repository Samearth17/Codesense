const arr = [
 {name: 'John', age: 19},
 {name: 'Mark', age: 22},
 {name: 'Mary', age: 17}
];

let max_age = arr[0].age;

arr.forEach( (item) => {
 if(item.age > max_age){
  max_age = item.age;
 }
});

console.log('The oldest person is ' + max_age + ' years old.');

// Outputs: The oldest person is 22 years old.