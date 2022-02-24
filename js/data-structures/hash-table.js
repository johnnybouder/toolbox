class HashTable {
    constructor() {
        this.collection = new Map();
    }
    add(key, value) {
        this.collection.set(key, value);
    }
    remove(key) {
        this.collection.delete(key);
    }
}

const coll = new HashTable();
coll.add('a', 1);
coll.add('b', 2);
coll.add('c', 3);
coll.add('d', 4);
coll.add('e', 5);
console.log(coll);

coll.remove('d');
console.log(coll);