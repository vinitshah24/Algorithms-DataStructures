package data_structures.tree.avl;

class AVLTree {

	Node root;

	int height(Node N) {
		return N == null ? 0 : N.height;
	}

	int max(int a, int b) {
		return (a > b) ? a : b;
	}

	Node leftRotate(Node z) {
		Node y = z.right;
		Node T2 = y.left;

		// Perform rotation
		y.left = z;
		z.right = T2;

		// Update heights
		z.height = max(height(z.left), height(z.right)) + 1;
		y.height = max(height(y.left), height(y.right)) + 1;

		// Return new root
		return y;
	}

	Node rightRotate(Node z) {
		Node y = z.left;
		Node T3 = y.right;

		// Perform rotation
		y.right = z;
		z.left = T3;

		// Update heights
		z.height = max(height(z.left), height(z.right)) + 1;
		y.height = max(height(y.left), height(y.right)) + 1;

		// Return new root
		return y;
	}

	int getBalance(Node N) {
		return (N == null) ? 0 : height(N.left) - height(N.right);
	}

	Node insert(Node node, int key) {

		// Perform the normal BST insertion
		if (node == null)
			return (new Node(key));

		if (key < node.key)
			node.left = insert(node.left, key);
		else if (key > node.key)
			node.right = insert(node.right, key);
		else // Duplicate keys not allowed
			return node;

		// Update height of this ancestor node
		node.height = 1 + max(height(node.left), height(node.right));

		// Check whether the node became unbalanced
		int balance = getBalance(node);

		// Case 1 - Left Left
		if (balance > 1 && key < node.left.key)
			return rightRotate(node);

		// Right Right Case
		if (balance < -1 && key > node.right.key)
			return leftRotate(node);

		// Left Right Case
		if (balance > 1 && key > node.left.key) {
			node.left = leftRotate(node.left);
			return rightRotate(node);
		}

		// Right Left Case
		if (balance < -1 && key < node.right.key) {
			node.right = rightRotate(node.right);
			return leftRotate(node);
		}

		return node;
	}

	// Given a non-empty binary search tree, return the node with minimum key value
	// found in that tree. Note that the entire tree does not need to be searched.
	Node minValueNode(Node node) {
		Node current = node;

		/* loop down to find the leftmost leaf */
		while (current.left != null)
			current = current.left;

		return current;
	}

	Node deleteNode(Node root, int key) {
		if (root == null)
			return root;

		// If the key to be deleted is smaller than the root's key, then it lies in left
		// subtree
		if (key < root.key)
			root.left = deleteNode(root.left, key);

		// If the key to be deleted is greater than the root's key, then it lies in
		// right subtree
		else if (key > root.key)
			root.right = deleteNode(root.right, key);

		// if key is same as root's key, then this is the node to be deleted
		else {

			// node with only one child or no child
			if ((root.left == null) || (root.right == null)) {
				Node temp = null;
				if (temp == root.left)
					temp = root.right;
				else
					temp = root.left;

				// No child case
				if (temp == null) {
					temp = root;
					root = null;
				} else // One child case
					root = temp; // Copy the contents of the non-empty child
			} else {

				// node with 2 child: Get the inorder successor (smallest in the right subtree)
				Node temp = minValueNode(root.right);

				// Copy the inorder successor's data to this node
				root.key = temp.key;

				// Delete the inorder successor
				root.right = deleteNode(root.right, temp.key);
			}
		}

		// If the tree had only one node then return
		if (root == null)
			return root;

		// STEP 2: UPDATE HEIGHT OF THE CURRENT NODE
		root.height = max(height(root.left), height(root.right)) + 1;

		// STEP 3: GET THE BALANCE FACTOR OF THIS NODE (to check whether
		// this node became unbalanced)
		int balance = getBalance(root);

		// If this node becomes unbalanced, then there are 4 cases
		// Left Left Case
		if (balance > 1 && getBalance(root.left) >= 0)
			return rightRotate(root);

		// Left Right Case
		if (balance > 1 && getBalance(root.left) < 0) {
			root.left = leftRotate(root.left);
			return rightRotate(root);
		}

		// Right Right Case
		if (balance < -1 && getBalance(root.right) <= 0)
			return leftRotate(root);

		// Right Left Case
		if (balance < -1 && getBalance(root.right) > 0) {
			root.right = rightRotate(root.right);
			return leftRotate(root);
		}

		return root;
	}

	// Print Preorder traversal of the tree.
	void preOrder(Node node) {
		if (node != null) {
			System.out.print(node.key + " ");
			preOrder(node.left);
			preOrder(node.right);
		}
	}

	public static void main(String[] args) {
		AVLTree tree = new AVLTree();
		tree.root = tree.insert(tree.root, 10);
		tree.root = tree.insert(tree.root, 20);
		tree.root = tree.insert(tree.root, 30);
		tree.root = tree.insert(tree.root, 40);
		tree.root = tree.insert(tree.root, 50);
		tree.root = tree.insert(tree.root, 25);
		tree.preOrder(tree.root);
		tree.root = tree.deleteNode(tree.root, 10);
		System.out.println("");
		tree.preOrder(tree.root);

	}
}