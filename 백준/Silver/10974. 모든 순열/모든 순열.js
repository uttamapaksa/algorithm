function perm(k) {
  if (k === N) {
    ans.push(res.join(' '))
    return
  }
  for (let i=1; i<=N; i++) {
    if (visit[i]) continue
    visit[i] = 1
    res.push(i)
    perm(k+1)
    visit[i] = 0
    res.pop(i)
  }
}

const N = +require('fs').readFileSync(0).toString().trim().split(' ').map(Number);
const visit = Array(N).fill(0)
const res = []
const ans = []
perm(0)
console.log(ans.join('\n'));