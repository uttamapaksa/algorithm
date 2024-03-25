function check() {
  for (let c = 1; c <= N; c++) {
    let nc = c;
    for (let r = 1; r <= H; r++) {
      if (arr[r][nc]) {
        nc++;
      } else if (arr[r][nc-1]) {
        nc--;
      }
    }
    if (nc !== c) {
      return false;
    }
  }
  return true;
}


function dfs(k: number, r: number, c: number) {
  if (k >= ans) return;
  if (check()) {
    ans = k;
    return;
  }
  if (k === 3) return;

  for (let nr = r; nr <= H; nr++) {
    for (let nc = 1; nc < N; nc++) {
      // prev line, curr line, next line already exists
      if (arr[nr][nc-1] || arr[nr][nc] || arr[nr][nc+1]) continue;
      arr[nr][nc] = true;
      dfs(k+1, nr, nc);
      arr[nr][nc] = false;
    }
  }
}


const [[N, _, H], ...lines]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number));
const arr: boolean[][] = Array.from({length: H+2}, ()=>Array(N+2).fill(false));
lines.forEach(([a, b]) => { arr[a][b] = true; });

let ans = 4;
dfs(0, 1, 1)
console.log(ans > 3 ? -1 : ans)