const backTrack =(n:number, combina:string[], p:string, x:number):void =>{
	if(x === n){
		combina.push(p);
		return;
	}
	
	for(let i = 0; i< 2;i++){
		backTrack(n, combina, p + i.toString(), x+1);
	}
	return;
}

function findDifferentBinaryString(nums: string[]): string {
	let unique = new Set<string>(nums);
	let combina:string[] = [];
	const n:number = nums.length;
	backTrack(n, combina, "",0);
	for(let com of combina){
		if(!unique.has(com)){
			return com;
		}
	}
	return "";
};

console.log(findDifferentBinaryString(["00", "01"]));
