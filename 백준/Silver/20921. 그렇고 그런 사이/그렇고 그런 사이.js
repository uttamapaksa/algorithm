let [n, k] = require('fs').readFileSync(process.platform === 'linux' ? 0 : 'input.txt').toString().trim().split(' ').map(Number)
let left = 1, right = n

const ans = Array(n).fill(0)
for (let i=n-1; i>0; i--) {
  if (!k) break
  if (k >= i) {
    k -= i
    ans[n-1-i] = right--
  }
}
for (let i=0; i<n; i++) {

  
  if (!ans[i]) {
    ans[i] = left++
  }
}
console.log(ans.join(' '));