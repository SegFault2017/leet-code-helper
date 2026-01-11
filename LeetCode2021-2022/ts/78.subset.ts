const backTrack = (nums:number[], subsets:number[][], subset:number[],
				   idx:number, k:number) : void =>{
	const m:number =  subset.length;
	if(k === m){
		subsets.push([...subset]);
		return;
	}
	
	const n:number = nums.length;
	for(let i = idx; i < n;i++){
		subset.push(nums[i]);
		backTrack(nums, subsets, subset, i+1,k);
		subset.pop();
	}
	return;
}
const subsets = (nums:number[]):number[][] => {
	const n:number = nums.length;
	let subsets:number[][] = [];
	for(let k = 0; k <= n;k++){
		backTrack(nums, subsets, [], 0, k);
	}
	return subsets;
}
