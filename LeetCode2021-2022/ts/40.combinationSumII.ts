const backTrack = (candidates:number[], target:number, combina:number[], 
				   result:number[][], idx:number): void =>{
	if(target ===  0){
		result.push([...combina]);
		return;
	}else if(target < 0){
		return;
	}

	const n:number = candidates.length;
	for(let i = idx;i < n; i++){
		if(i > idx && candidates[i] ===  candidates[i-1]){
			continue;
		}
		combina.push(candidates[i]);
		backTrack(candidates, target - candidates[i], combina, result, i+1);
		combina.pop();
	}
	return;
}
const combinationSum2 = (candidates:number[], target:number):number[][] =>{
	let result:number[][] = [];
	const sorted:number[] = candidates.sort((x:number, y:number) => x - y);
	backTrack(sorted, target, [], result, 0);
	return result;
}
