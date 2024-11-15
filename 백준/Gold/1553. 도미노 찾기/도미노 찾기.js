const next = (r, c) => {
  if (c < 6) brute(r, c+1)
  else if (r < 7) brute(r+1, 0)
}

const check = (r, c, nr, nc) => {
  if (visit[nr][nc]) return
  a = arr[r][c], b = arr[nr][nc]
  if (a > b) [a, b] = [b, a]
  let domino = (a << 3) + b
  if (!used.has(domino)) {
    used.add((domino))
    visit[r][c] = 1
    visit[nr][nc] = 1
    next(r, c)
    used.delete((domino))
    visit[r][c] = 0
    visit[nr][nc] = 0
  }
}

const brute = (r, c) => {
  if (r === 7 && c === 6) {
    ans++
    return
  }
  if (visit[r][c]) next(r, c)
  else {
    if (c < 6) check(r, c, r, c+1)
    if (r < 7) check(r, c, r+1, c)
  }
}

let arr = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(x=>x.split('').map(Number));
let visit = Array.from({length:8},()=>Array(7).fill(0))
let used = new Set()
let ans = 0

brute(0, 0)
console.log(ans);