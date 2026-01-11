const dfs = (graph:number[][], combina:number[][], node:number, target:number, 
			 path:number[] ):void =>{
	if(node === target){
		combina.push([...path]);
		return;
	}

	for(let neigh of graph[node]){
		path.push(neigh);
		dfs(graph,combina, neigh, target, path);
		path.pop();
	}

	return;
}
function allPathsSourceTarget(graph: number[][]): number[][] {
   if(!graph){
	   return [];
   }

   let combina:number[][] = [];
   const n:number = graph.length;
   dfs(graph,combina, 0, n-1, [0]);
   return combina;
};
