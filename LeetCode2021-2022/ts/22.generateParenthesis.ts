const backTrack = (l:number, r:number, parenthesis:string[], p:string, 
				  n:number):void =>{
	const m:number = p.length;
	if(m === 2*n){
		parenthesis.push(p);
		return;
	}

	if(l < n){
		backTrack(l+1, r, parenthesis, p + "(", n);
	}
	if(r < l){
		backTrack(l, r+1, parenthesis, p + ")", n);
	}
	return;
}
const generateParenthesis = (n:number):string[] =>{
	let parenthesis:string[] =[];
	backTrack(0,0, parenthesis, "", n);
	return parenthesis;
}
