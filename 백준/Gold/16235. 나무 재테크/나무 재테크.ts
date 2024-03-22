const input = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number));
const [N, M, K]: number[] = input[0];
const robot: number[][] = input.slice(1, N+1);
const trees: number[][][] = Array.from({length: N}, ()=>Array.from({length: N}, ()=>[]));
input.slice(N+1).forEach(([x, y, d]: number[]) => trees[x-1][y-1].push(d));
const land: number[][] = Array.from({length: N}, ()=>Array(N).fill(5));
const delta = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]];

for (let _=0; _<K; _++) {
  const deltaTrees: number[][][] = Array.from({length: N}, ()=>Array.from({length: N}, ()=>[]));
  const deltaLand: number[][] = Array.from({length: N}, ()=>Array(N).fill(0));
  for (let i=0; i<N; i++) {
    for (let j=0; j<N; j++) {
      if (!trees[i][j].length) continue;
      
      // spring
      trees[i][j] = trees[i][j].sort((a,b) => a-b);
      const alive: number[] = [];
      const dead: number[] = [];
      for (const tree of trees[i][j]) {
        if (tree <= land[i][j]) {
          land[i][j] -= tree;
          alive.push(tree+1);
        } else {
          dead.push(tree);
        }
      }
      trees[i][j] = alive;
      // summer
      for (const tree of dead) {
        deltaLand[i][j] += Math.trunc(tree / 2);
      }
      // autumn
      for (const tree of alive) {
        if (tree / 5 !== Math.trunc(tree / 5)) continue;
        for (const [dr, dc] of delta) {
          const nr = i + dr, nc = j + dc;
          if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
          deltaTrees[nr][nc].push(1);
        }
      }
    }
  }
  // winter
  for (let i=0; i<N; i++) {
    for (let j=0; j<N; j++) {
      land[i][j] += deltaLand[i][j];
      land[i][j] += robot[i][j];
      trees[i][j] = trees[i][j].concat(deltaTrees[i][j]);
    }
  }
}

// count
let count = 0;
for (let i=0; i<N; i++) {
  for (let j=0; j<N; j++) {
    count += trees[i][j].length;
  }
}
console.log(count);