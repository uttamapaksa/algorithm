const [[N], ...arr]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' ').map(Number));
const visit = Array.from({length: N}, ()=>Array(N).fill(-1));
const delta = [[-1, 0], [0, -1], [1, 0], [0, 1]];
let ans = 0;

function dfs(r: number, c: number) {
  if (visit[r][c] !== -1) {
    return visit[r][c];
  }
  visit[r][c] = 1;
  
  let value = 0;
  for (const [dr, dc] of delta) {
    const [nr, nc] = [r + dr, c + dc];
    if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
    if (arr[r][c] > arr[nr][nc]) {
      value = Math.max(value, dfs(nr, nc));
    }
  }

  visit[r][c] += value;
  ans = Math.max(ans, visit[r][c]);
  return visit[r][c];
}

for (let r=0; r<N; r++) {
  for (let c=0; c<N; c++) {
    dfs(r, c);
  }
}

console.log(ans);