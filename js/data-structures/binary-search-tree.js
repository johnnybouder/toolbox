class Node
{
    constructor(data)
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree
{
    constructor() {
        this.root = null;
    }
    insert(data) {
        var newNode = new Node(data);

        if(this.root === null) {
            this.root = newNode;
        }
        else {
            this.insertNode(this.root, newNode);
        }
    }
    insertNode(node, newNode) {
        if(newNode.data < node.data) {
            // if left is null insert node here
            if(node.left === null) {
                node.left = newNode;
            } else {
                this.insertNode(node.left, newNode);
            }
        } else {
            // if right is null insert node here
            if(node.right === null)
                node.right = newNode;
            else {
                this.insertNode(node.right,newNode);
            }
        }
    }
    remove(data) {
        this.root = this.removeNode(this.root, data);
    }
    removeNode(node, key) {
        if(node === null) {
            return null;
        } else if(key < node.data) {
            node.left = this.removeNode(node.left, key);
            return node;
        } else if(key > node.data) {
            node.right = this.removeNode(node.right, key);
            return node;
        } else {
            // deleting node with no children
            if(node.left === null && node.right === null) {
                node = null;
                return node;
            }
    
            // deleting node with one children
            if(node.left === null) {
                node = node.right;
                return node;
            } else if(node.right === null) {
                node = node.left;
                return node;
            }

            var aux = this.findMinNode(node.right);
            node.data = aux.data;
    
            node.right = this.removeNode(node.right, aux.data);
            return node;
        }
    }

    // Performs inorder traversal of a tree
    inorder(node) {
        if(node !== null) {
            this.inorder(node.left);
            console.log(node.data);
            this.inorder(node.right);
        }
    }
    // Performs preorder traversal of a tree   
    preorder(node) {
        if(node !== null) {
            console.log(node.data);
            this.preorder(node.left);
            this.preorder(node.right);
        }
    }
    // Performs postorder traversal of a tree
    postorder(node) {
        if(node !== null) {
            this.postorder(node.left);
            this.postorder(node.right);
            console.log(node.data);
        }
    }
    // finds the minimum node in tree, searching starts from given node
    findMinNode(node) {
        // if left of a node is null, then it must be minimum node
        if(node.left === null) {
            return node;
        } else {
            return this.findMinNode(node.left);
        }
    }
    // returns root of the tree
    getRootNode() {
        return this.root;
    }
    // search for a node with given data
    search(node, data) {
        if(node === null) {
            return null;
        } else if(data < node.data) { // if data is less than node's data, move left
            return this.search(node.left, data);
        } else if(data > node.data) { // if data is less than node's data, move left
            return this.search(node.right, data);
        } else { // if data is equal to the node data, return node
            return node;
        }
    }
}

const BST = new BinarySearchTree();
BST.insert(15);
BST.insert(25);
BST.insert(10);
BST.insert(7);
BST.insert(22);
BST.insert(17);
BST.insert(13);
BST.insert(5);
BST.insert(9);
BST.insert(27);
 
let root = BST.getRootNode();
BST.inorder(root);
BST.remove(5);

root = BST.getRootNode();
BST.inorder(root);
BST.remove(7);
                    
root = BST.getRootNode();
BST.inorder(root);
BST.remove(15);

root = BST.getRootNode();
BST.inorder(root);
BST.postorder(root);
BST.preorder(root);