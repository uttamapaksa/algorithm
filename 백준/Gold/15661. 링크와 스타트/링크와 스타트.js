function calc(team) {
    let total = 0;
    for (let i=0; i<team.length-1; i++) {
        for (let j=i+1; j<team.length; j++) {
            total += score[team[i]][team[j]];
            total += score[team[j]][team[i]];
        }
    }
    return total;
}

function comb(c) {
    if (c > N || team.length === N) return;
    if (team[0] >= N/2) return;
    if (team.length) {
        const as = calc(team);
        const bs = calc(total.filter(x => !visit[x]));
        ans = Math.min(ans, Math.abs(as - bs));
        if (as >= bs) return;
    }
    for (let i=c; i<N; i++) {
        if (visit[i]) continue;
        visit[i] = 1;
        team.push(i)
        comb(i+1)
        if (team[0] >= N/2) return;
        team.pop()
        visit[i] = 0;
    }
}

const [[N], ...score] = require('fs').readFileSync(0).toString().trim().split('\n').map(x=>x.split(' ').map(Number));
const total = Array.from({length: N},(_,i)=>i);
const visit = Array(N).fill(0);
let ans = Infinity;
const team = []
comb(0)
console.log(ans);
