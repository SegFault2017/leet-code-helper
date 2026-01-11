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

const backTrack =(node:TreeNode | null, targetSum:number, paths:number[][],
				  p:number[]):void =>{
	if(targetSum === 0 && !node.left && !node.right){
		paths.push([...p]);
		return;
	}

	if(node.left){
		p.push(node.left.val);
		backTrack(node.left, targetSum - node.left.val, paths, p);
		p.pop();
	}

	if(node.right){
		p.push(node.right.val);
		backTrack(node.right, targetSum - node.right.val, paths, p);
		p.pop();
	}
	return;
}
const pathSum = (root:TreeNode| null, targetSum:number):number[][] => {
	if(!root){
		return [];
	}
	let paths:number[][] = [];
	backTrack(root, targetSum - root.val, paths, [root.val]);
	return paths;
}
