/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

const dfs = (root: TreeNode | null, combina:string[], path:string):void =>{
	if(!root.left && !root.right){
		combina.push(path);
		return;
	}

	if(root.left){
		const leftP:string = path + "->" + root.left.val.toString();
		dfs(root.left, combina, leftP);
	}

	if(root.right){
		const rightP:string = path + "->" + root.right.val.toString();
		dfs(root.right, combina, rightP);
	}

	return;
}
const binaryTreePaths = (root: TreeNode | null) :string[] =>{
	if(!root){
		return [];
	}
	
	let combina:string = [];
	dfs(root, combina, root.val.toString()); 
	return;
}

