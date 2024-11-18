function sol() {
  for (let t=1; t<=1000; t++) {
    for (let i=1; i<=K; i++) {
      let [r, c, d] = chessMap[i]
      let nr = r+dr[d]
      let nc = c+dc[d]
      if (nr < 0 || nr >= N || nc < 0 || nc >= N || arr[nr][nc] === 2) {
        chessMap[i][2] = [0, 2, 1, 4, 3][d]
        nr = r-dr[d]
        nc = c-dc[d]
      }
      if (0 <= nr && nr < N && 0 <= nc && nc < N && arr[nr][nc] !== 2) {
        let tmp = chessArr[r][c].splice(chessArr[r][c].indexOf(i))
        for (let n of tmp) {
          chessMap[n][0] = nr
          chessMap[n][1] = nc
        }
        if (arr[nr][nc] === 1) {
          chessArr[nr][nc] = chessArr[nr][nc].concat(tmp.reverse())
        } else {
          chessArr[nr][nc] = chessArr[nr][nc].concat(tmp)
        }
        if (chessArr[nr][nc].length >= 4) {
          return t
        }
      }
    }
  }
  return -1
}

const [[N, K], ...ipt] = require('fs').readFileSync(0).toString().trim().split('\n').map(x=>x.split(' ').map(Number));
const dr = [0, 0, 0, -1, 1]
const dc = [0, 1, -1, 0, 0]
const arr = []
for (let i=0; i<N; i++) {
  arr.push(ipt[i])
}
const chessArr = Array.from({length: N}, ()=>Array.from({length: N}, ()=>[]))
const chessMap = {}
for (let i=N; i<N+K; i++) {
  const [r, c, d] = ipt[i]
  chessArr[r-1][c-1].push(i-N+1)
  chessMap[i-N+1] = [r-1, c-1, d]
}

console.log(sol())