const [[N], _, ...arr] = require('fs').readFileSync(0).toString().trim().split('\n').map(x => x.split(' ').map(Number));
const graph = Array.from({length: N+1}, ()=>[])
for (const [u, v] of arr) {
  graph[u].push(v)
}
const res = Array.from({length: N+1}, ()=>Array.from({length: N+1},()=>0))

let queue = []
let front = 0
let visit = []
for (let s=1; s<N+1; s++) {
  visit = Array(N+1).fill(0)
  visit[s] = 1
  queue = [s]
  front = 0
  while (front < queue.length) {
    const u = queue[front++]
    for (const v of graph[u]) {
      if (visit[v]) continue
      res[s][v] = 1
      res[v][s] = 1
      visit[v] = 1
      queue.push(v)
    }
  }
}

for (let i=1; i<N+1; i++) {
  console.log(N-1-res[i].reduce((a,c)=>a+c,0));
}
