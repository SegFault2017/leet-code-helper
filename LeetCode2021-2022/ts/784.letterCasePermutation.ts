const backTrack = (s:string, str:string, result:string[], idx:number): void =>{
	const n:number = s.length;
	if(idx === n){
		result.push(str);
		return;
	}

	const c:string = s[idx];
	if(isNaN(Number(c))){
		backTrack(s, str+c.toLowerCase(), result, idx+1);
		backTrack(s, str+c.toUpperCase(), result, idx+1);
	}else{
		backTrack(s, str+c, result, idx+1);
	}
	return;
}
	
const letterCasePermutation = (s:string): string[] => {
	let result:string[] = [];
	backTrack(s, "", result, 0);
	return result;
}
