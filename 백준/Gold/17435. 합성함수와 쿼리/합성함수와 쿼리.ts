const [[m], nums, [Q], ...qeuries]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number))
const LOG = 20
const par: number[][] = Array.from({length: LOG}, ()=>Array(m+1).fill(0))

for (let i=0; i<m; i++) {
  par[0][i+1] = nums[i]
}
for (let i=1; i<LOG; i++) {
  for (let j=1; j<m+1; j++) {
    par[i][j] = par[i-1][par[i-1][j]]
  }
}

let ans = ''
qeuries.forEach(([n, x]) => {
  for (let i=LOG-1; i>-1; i--) {
    if (n >= (1 << i)) {
      x = par[i][x]
      n -= 1 << i
    }
  }
  ans += `${x}\n`
})

console.log(ans)