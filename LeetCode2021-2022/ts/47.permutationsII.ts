type dict={[key:string]:number[]}
const swap = (nums:number[], i:number, j:number):void => {
	const temp:number = nums[i];
	nums[i] = nums[j];
	nums[j] = temp;
	return;
}
const backTrack = (nums:number[], unique:dict, idx:number):void =>{
	const n:number = nums.length;
	if(n === idx){
		const dCopy:number[] = [...nums];
		const key:string = dCopy.toString();
		unique[key] = dCopy;
		return;
	}

	for(let i = idx; i < n;i++){
		swap(nums, idx, i);
		backTrack(nums, unique, idx+1);
		swap(nums, idx, i);
	}
	return;
}
const permuteUnique = (nums:number[]):number[][]=>{
	let unique:dict = {};
	let permutes:number[][]=[];
	backTrack(nums, unique, 0);
	for(const [key,val] of Object.entries(unique)){
		permutes.push(val);		
	}
	return permutes;
}
