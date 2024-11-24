function sol() {
    const visit = new Set([T]);
    const stack = [T];
    while (stack.length) {
        const curr = stack.pop()
        if (curr === S) return 1;
        if (curr.length === S.length) continue;
        if (curr[curr.length-1] === 'A') {
            const tmp = curr.slice(0, curr.length-1)
            if (!visit.has(tmp)) {
                visit.add(tmp);
                stack.push(tmp);
            }   
        }
        if (curr[0] === 'B') {
            const tmp = curr.slice(1).split("").reverse().join("");
            if (!visit.has(tmp)) {
                visit.add(tmp);
                stack.push(tmp);
            }
        }
    }
    return 0;
}

const [S, T] = require('fs').readFileSync(0).toString().trim().split('\n').map(x=>x.trim());
console.log(sol());
