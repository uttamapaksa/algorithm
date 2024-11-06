const input = require('fs').readFileSync(0).toString().trim().split('\n')
for (let tc=0; tc<Math.trunc(input.length/7); tc++){
  
  function comb(k, res, b) {
    if (k === 5) {
      if (b === init) {
        ans = Math.max(ans, res)
      }
      return
    }
    
    for (let i=1; i<6; i++) {
      if (visit[i]) continue
      for (const [aa, bb, cc] of [[arr[i][0],arr[i][1],arr[i][2]],[arr[i][1],arr[i][2],arr[i][0]],[arr[i][2],arr[i][0],arr[i][1]]]) {
        if (b === cc) {
          visit[i] = 1
          comb(k+1, res+aa, bb)
          visit[i] = 0
        }
      }
    }
  }
  
  const arr = []
  for (let i=0; i<6; i++) {
    arr.push(input[tc*7+i].split(' ').map(Number))
  }

  let ans = 0
  const visit = Array(6).fill(0)
  visit[0] = 1
  let init = 0
  for (const [a, b, c] of [[arr[0][0],arr[0][1],arr[0][2]],[arr[0][1],arr[0][2],arr[0][0]],[arr[0][2],arr[0][0],arr[0][1]]]) {
    init = c
    comb(0, a, b)
  }

  console.log(ans ? ans : 'none');
}