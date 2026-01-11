const backTrack =(n:number, x:number, combina:number[][], f:number[]):void =>{
	const m:number = f.length;
	if(m > 0){
		const factors:number[] = [...f, n];
		combina.push(factors);
	}

	for(let i =x; i < Math.floor(Math.sqrt(n))+1;i++){
		if(n % i === 0){
			const divisor:number = n / i;
			f.push(i);
			backTrack(divisor, i, combina, f);
			f.pop();
		}
	}
	return;
}
const getFactors = (n:number):number[][] =>{
	let combina:number[][] =[];
	backTrack(n, 2, combina, []);
	return combina;
}
