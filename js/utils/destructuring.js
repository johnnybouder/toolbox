const myObject = {
  name: "Hello world",
  data: [
    { id: 1, name: "John" },
    { id: 2, name: "Jane" },
    { id: 3, name: "Joe" },
  ],
};

const { name, data } = myObject;
const filteredData = data
  .filter((elem) => elem.id > 1)
  .filter((elem) => elem.name === "Joe");

console.log(name);
console.log(data);
console.log(filteredData);
