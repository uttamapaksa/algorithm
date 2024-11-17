var [[N, M, K], ...arr] = require('fs').readFileSync(0).toString().trim().split('\n').map(x=>x.split(' ').map(Number));
var cnt = 0;
for (var i=0; i<N; i++) {
  for (var j=0; j<N; j++) {
    if (arr[i][j]) continue;
    var stack = [[i, j]];
    cnt = 1;
    arr[i][j] = 1;
    while (stack.length) {
      var [r, c] = stack.pop()
      for (var [nr, nc] of [[r+1,c], [r-1,c], [r,c+1], [r,c-1]]) {
        if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
        if (!arr[nr][nc]) {
          stack.push([nr, nc]);
          cnt++;
          arr[nr][nc] = 1;
        }
      }
    }
    M -= Math.ceil(cnt / K);
    if (M < 0) break;
  }
  if (M < 0) break;
}

console.log(M < 0 || !cnt ? 'IMPOSSIBLE' : `POSSIBLE\n${M}`);
