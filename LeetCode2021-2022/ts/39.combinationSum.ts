const backTrack = (candidates:number[], target:number,combina:number[], result:number[][], 
				   idx:number): void =>{
	if(target === 0){
		result.push([...combina]);
		return;
	}else if(target < 0){
		return;
	}

	const n:number =  candidates.length;
	for(let i = idx; i < n; i++){
		combina.push(candidates[i]);
		backTrack(candidates, target - candidates[i],combina, result, i);
		combina.pop();
	}
	return;
}
const combinationSum = (candidates:number[], target:number):number[][] =>{
	let result:number[][] = [];
	backTrack(candidates, target,[], result, 0);
	return result;
}
