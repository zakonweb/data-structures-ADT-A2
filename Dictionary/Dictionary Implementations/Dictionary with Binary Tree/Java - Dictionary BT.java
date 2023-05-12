class Node {
    int key;
    String value;
    Node left, right;

    public Node(int item, String value) {
        key = item;
        this.value = value;
        left = right = null;
    }
}

class BinaryTree {
    Node root;

    void insert(int key, String value) {
        root = insertRec(root, key, value);
    }

    Node insertRec(Node root, int key, String value) {
        if (root == null) {
            root = new Node(key, value);
            return root;
        }
        if (key < root.key)
            root.left = insertRec(root.left, key, value);
        else if (key > root.key)
            root.right = insertRec(root.right, key, value);
        else
            root.value = value;  // If the key already exists, update the value
        return root;
    }

    Node search(int key) {
        return searchRec(root, key);
    }

    Node searchRec(Node root, int key) {
        if (root==null || root.key==key)
            return root;
        if (root.key > key)
            return searchRec(root.left, key);
        return searchRec(root.right, key);
    }
}
