const [[N], ...input]: number[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.split(' ').map(Number));
const delta = [[1, 0], [0, -1], [-1, 0], [0, 1]];
const dragons: boolean[][] = Array.from({ length: 101 }, () => Array(101).fill(false));

for (let [x, y, d, g] of input) {
  const directs: number[] = [];
  // 방향들 저장. 전 단계 방향들을 각각 90 회전시킨 것을 다시 스택에 추가
  directs.push(d)
  for (let _ = 0; _ < g; _++) {
    for (let i = directs.length - 1; i > -1; i--) {
      d = directs[i] === 3 ? 0 : directs[i] + 1;
      directs.push(d);
    } 
  }
  // 드래곤 커브 점들 갱신
  dragons[x][y] = true;
  for (const d of directs) {
    x += delta[d][0], y += delta[d][1];
    dragons[x][y] = true;
  }
}  

let answer = 0;
for (let i = 0; i < 100; i++) {
  for (let j = 0; j < 100; j++) {
    if (dragons[i][j] && dragons[i+1][j] && dragons[i][j+1] && dragons[i+1][j+1]) {
      answer++;
    }
  }
}

console.log(answer);