class Queue {
    constructor() {
        this.collection = [];
    }
    add(item) {
        this.collection.push(item);
    }
    remove() {
        this.collection.shift();
    }
}

const coll = new Queue();
coll.add(1);
coll.add(2);
coll.add(3);
coll.add(4);
coll.add(5);
coll.remove();

console.log(coll);