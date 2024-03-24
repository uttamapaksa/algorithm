function solution(n, costs) {
    function find(x) {
        if (P[x] !== x) {
            P[x] = find(P[x]);
        }
        return P[x];
    }
    
    function union(x, y) {
        const a = find(x), b = find(y);
        if (a === b) {
            return false;
        }
        if (a < b) {
            P[b] = a;
        } else {
            P[a] = b;
        }
        return true;
    }
    
    const P = Array.from({length: n}, (_, i) => i)
    costs = costs.sort((a, b) => a[2] - b[2]);
    let answer = 0;
    
    for (const [u, v, w] of costs) {
        if (union(u, v)) {
            answer += w;    
        }
    }
    
    return answer;
}