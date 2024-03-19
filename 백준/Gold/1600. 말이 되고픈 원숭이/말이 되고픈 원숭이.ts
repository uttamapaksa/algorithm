const [[K], [C, R], ...arr]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number));
const pawn = [[-1, 0], [0, -1], [1, 0], [0, 1]];
const knight = [[-2, -1], [-1, -2], [2, -1], [1, -2], [2, 1], [1, 2], [-2, 1], [-1, 2]];
const visit = Array.from({length: R}, ()=>Array.from({length: C}, ()=>Array(K+1).fill(0)));
visit[0][0][K] = 1;
const queue: number[][] = [[0, 0, K]];
queue.push([0, 0, K]);
let front = 0;

while (front < queue.length) {
  const [r, c, t] = queue[front++] as number[];

  if (r === R && c === C) break;

  for (const [dr, dc] of pawn) {
    const [nr, nc] = [r + dr, c + dc];
    if (nr < 0 || nr >= R || nc < 0 || nc >= C || arr[nr][nc] || visit[nr][nc][t]) continue;
    visit[nr][nc][t] = visit[r][c][t] + 1;
    queue.push([nr, nc, t]);
  }

  if (!t) continue;

  for (const [dr, dc] of knight) {
    const [nr, nc] = [r + dr, c + dc];
    if (nr < 0 || nr >= R || nc < 0 || nc >= C || arr[nr][nc] || visit[nr][nc][t-1]) continue;
    visit[nr][nc][t-1] = visit[r][c][t] + 1;
    queue.push([nr, nc, t-1]);
  }
}

const arrive = visit[R-1][C-1].filter((x: number) => x > 0);
console.log(arrive.length ? Math.min(...arrive) - 1 : -1);