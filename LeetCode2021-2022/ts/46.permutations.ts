const swap =(nums: number[], i:number, j:number): void =>{
	const temp:number = nums[i];
	nums[i] = nums[j];
	nums[j] = temp;
	return;
}

const backTrack = (permutes:number[][], nums:number[], idx:number): void => {
	const n: number = nums.length;
	if(n === idx){
		permutes.push([...nums]);
		return;
	}

	for(let i = idx; i < n;i++){
		swap(nums, i, idx);
		backTrack(permutes, nums, idx+1);
		swap(nums, i, idx);
	}
	return;
}
const permute = (nums:number[]) :number[][] =>{
	let permutes:number[][] = [];
	backTrack(permutes, nums, 0);
	return permutes;
}
