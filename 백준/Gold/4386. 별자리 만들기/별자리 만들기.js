function find(x) {
    if (P[x] !== x) {
        P[x] = find(P[x]);
    }
    return P[x];
}

function union(w, x, y) {
    const a = find(x), b = find(y);
    if (a === b) {
        return;
    }
    if (a < b) {
        P[b] = a;
    } else {
        P[a] = b;
    }
    answer += w;
}

const [[N], ...I] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map(x=>x.split(' ').map(Number));
const P = Array.from({length: N}, (_, i) => i);
let answer = 0;

const G = [];
for (let u = 0; u < N - 1; u++) {
    const [x1, y1] = I[u];
    for (let v = u + 1; v < N; v++) {
        const [x2, y2] = I[v];
        const w = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        G.push([w, u, v]);
    }
}
G.sort((a, b) => a[0] - b[0]);

for (const edge of G) {
    const [_, u, v] = edge;
    union(edge[0], u, v);
}

console.log(Math.round(answer * 100) / 100);