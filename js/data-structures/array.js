class MyArray {
    constructor() {
        this.collection = [];
    }
    addStart(item) {
        this.collection.unshift(item);
    }
    addEnd(item) {
        this.collection.push(item);
    }
    removeFirst() {
        this.collection.shift();
    }
    removeLast() {
        this.collection.pop();
    }
    sortAsc() {
        this.collection.sort(
            (a, b) => {
                if (a > b)
                    return 1;
                if (a < b)
                    return -1;
                return 0;
            }
        );
    }
    sortDesc() {
        this.collection.sort(
            (a, b) => {
                if (a > b)
                    return -1;
                if (a < b)
                    return 1;
                return 0;
            }
        );
    }
}

const coll = new MyArray();
coll.addEnd(5);
coll.addEnd(4);
coll.addEnd(3);
coll.addEnd(2);
coll.addEnd(1);
coll.sortAsc();

console.log(coll);