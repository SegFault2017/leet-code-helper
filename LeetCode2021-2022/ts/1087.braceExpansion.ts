const backTrack = (s:string, combina:string[], p:string, idx:number):void =>{
 const n:number = s.length;
	if(idx === n){
		combina.push(p);
		return;
	}
	const curr:string = s[idx];
	if(curr !== '{'){
		return backTrack(s, combina, p + curr, idx+1);
	}
	let j:number = idx;
	let choices:string[] = [];
	while(s[j] !== '}'){
		if(s[j] !== ','){
			choices.push(s[j]);
		}
		j++;
	}

	for(let choice of choices){
		backTrack(s, combina, p + choice, j+1);
	}
	return;
}
const expand = (s:string):string[] =>{
	let combina:string[] = [];
	backTrack(s, combina, "", 0);
	return combina.sort();
}
