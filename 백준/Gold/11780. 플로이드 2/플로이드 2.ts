let [N, W, ...input] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x:string)=>x.trim().split(" ").map(Number))
N = N[0], W = W[0]
const INF = 10000000;
const cost = Array.from({length: N+1}, () => Array(N+1).fill(INF))
const path = Array.from({length: N+1}, () => Array.from({length: N+1}, ()=>[] as number[]))
// initailization
for (let i=1; i<N+1; i++) {
  cost[i][i] = 0
}
for (const [u, v, w] of input) {
  if (cost[u][v] > w) {
    cost[u][v] = w
    path[u][v] = [v]
  }
}
// FW
for (let k=1; k<N+1; k++) {
  for (let i=1; i<N+1; i++) {
    for (let j=1; j<N+1; j++) {
      if (cost[i][j] > cost[i][k] + cost[k][j]) {
        cost[i][j] = cost[i][k] + cost[k][j]
        path[i][j] = [...path[i][k], ...path[k][j]]  
      }
    }
  }
}

let ans: string = ""
// cost
for (let i=1; i<N+1; i++) {
  for (let j=1; j<N+1; j++) {
    ans += `${cost[i][j] === INF ? 0 : cost[i][j]} `
  }
  ans += "\n"
}
// path
for (let i=1; i<N+1; i++) {
  for (let j=1; j<N+1; j++) {
    if (!path[i][j].length) {
      ans += "0 "
    } else {
      ans += `${path[i][j].length + 1} ${i} ${path[i][j].join(" ")}`
    }
    ans += "\n"
  }
}
// output
console.log(ans)
