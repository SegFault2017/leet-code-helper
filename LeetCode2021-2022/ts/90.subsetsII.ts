const backTrack = (nums:number[], subsets:number[][], subset:number[],
				   idx:number, k:number): void =>{
	const m = subset.length;
	if(k === m){
		subsets.push([...subset]);
		return;
	}
	
	const n:number = nums.length;
	for(let i = idx; i < n;i++){
		if(i > idx && nums[i] === nums[i-1]){
			continue;
		}

		subset.push(nums[i]);
		backTrack(nums, subsets, subset, i +1, k);
		subset.pop();
	}
	return;
}
const subsetsWithDup = (nums:number[]):number[][] =>{
	const n:number = nums.length;
	const sorted:number[]= nums.sort((x:number, y:number) => x - y);
	let subsets:number[][] = [];
	for(let k = 0; k <= n; k++){
		backTrack(nums,subsets, [], 0, k);
	}
	return subsets;
}
