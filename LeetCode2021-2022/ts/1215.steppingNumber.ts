const backTrack = (low:number, high:number, num:string, numbers:number[], 
				   end:number):void =>{
	const n:number = num.length;
	const stepNum:number = Number(num);
	if(stepNum >= low && stepNum <= high){
		numbers.push(stepNum);
	}

	if(n >= end){
		return;
	}

	const m1:number = Number(num[n-1])-1;
	const p1:number = Number(num[n-1])+1;
	if(m1 >= 0){
		backTrack(low, high, (num+m1).toString(), numbers,end);
	}
	
	if(p1 < 10){
		backTrack(low, high, (num+p1).toString(), numbers,end);
	}
	return;
}
const countSteppingNumbers =(low:number, high:number):number[] =>{
	const n:number = high.toString().length;
	let numbers:number[] = low === 0 ? [0] : [];
	
	for(let i = 1; i< 10; i++){
		backTrack(low, high,i.toString(), numbers, n);
	}
	return numbers.sort((x:number, y:number) => x- y);
}
