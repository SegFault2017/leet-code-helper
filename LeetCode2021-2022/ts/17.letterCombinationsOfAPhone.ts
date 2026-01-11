type dict = {[key:string]:string[]};
const backTrack = (digits:string, d2l: dict,combina:string[], x:number,
				   p:string):void =>{
	const n:number = digits.length;
	if(x === n){
		combina.push(p);
		return;
	}

	for(let alpha of d2l[digits[x]]){
		backTrack(digits, d2l, combina, x+1, p + alpha);
	}
	return;
}
const letterCombinations = (digits:string):string[] =>{
	const d2l:dict = {
        "2":  ["a","b","c"],
        "3":  ["d", "e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
         "9":["w","x","y","z"]
    };
	let combina:string[] = [];
	backTrack(digits,d2l, combina, 0, "");
	return combina;
}
