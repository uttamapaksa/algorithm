const [_, arr]: string[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' '));
const cnt: Record<string, number> = {'0':0, '1':0, '2':0, '3':0};
arr.forEach((v: string) => { cnt[v]++; });

let ans = 0;
while (cnt['0'] && cnt['3']) {
  ans += 3; cnt['0']--; cnt['3']--;
}
while (cnt['1'] && cnt['2']) {
  ans += 3; cnt['1']--; cnt['2']--;
}
while (cnt['0'] && cnt['2']) {
  ans += 2; cnt['0']--; cnt['2']--;
}
while (cnt['1'] && cnt['3']) {
  ans += 2; cnt['1']--; cnt['3']--;
}
while (cnt['0'] && cnt['1']) {
  ans += 1; cnt['0']--; cnt['1']--;
}
while (cnt['2'] && cnt['3']) {
  ans += 1; cnt['2']--; cnt['3']--;
}
console.log(ans);