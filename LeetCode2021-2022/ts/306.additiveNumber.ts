const backTrack = (num:string, path:number[], idx:number):boolean =>{
	const n:number = num.length;
	const m:number = path.length;
	
	if(idx === n && m > 2){
		return true;
	}

	for(let i =idx; i <n;i++){
		if(i > idx && num[idx] === '0'){
			continue;
		}
		const prev:number = Number(path[m-1]);
		const prev2:number = Number(path[m-2]);
		const curr:number = Number(num.substring(idx,i+1));
		if(m < 2 || (m >=2 && prev + prev2 === curr)){
			path.push(curr);
			if(backTrack(num, path, i+1)){
				return true;
			}
			path.pop();
		}
	}
	return false;
}
const isAdditiveNumber = (num:string):boolean =>{
	return backTrack(num, [], 0);	
}
