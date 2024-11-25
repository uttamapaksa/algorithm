const [[N, K], children] = require('fs').readFileSync(process.platform === 'linux' ? 0 : 'input.txt').toString().trim().split('\n').map(x=>x.split(' ').map(Number));
const diff = [];
for (let i=0; i<N-1; i++) {
    diff.push(children[i+1]-children[i]);
}
diff.sort((a,b)=>a-b);
diff.splice(N-K);
console.log(diff.reduce((a,c)=>a+c, 0));