type dict = {[key:string]:number};
const isDup = (s:string, counter:dict):boolean =>{
	for(let c of s){
		if(c in counter){
			return true;
		}
		counter[c] = 1;
	}
	return false;
}
const backTrack = (arr:string[], p:string, x:number): number =>{
	const n:number = arr.length;
	let maxLen:number = p.length;
	let counter:dict = {};
	if(isDup(p, counter)){
		return maxLen;
	}

	for(let i =idx; i < n;i++){
		counter = {}
		isDup(p, counter);
		if(!isDup(arr[i], counter)){
			maxLen = Math.max(backTrack(arr, p + arr[i], i+1), maxLen);
		}
	}
	return maxLen;
}
const maxLength = (arr:string[]):number =>{
	return backTrack(arr, "", 0);
}
