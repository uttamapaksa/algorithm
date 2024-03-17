function solution(tickets) {
    let nodes = new Set();
    for (const ticket of tickets) {
        const [a, b] = ticket;
        nodes.add(a);
        nodes.add(b);
    }
    nodes = Array.from(nodes).sort();
    
    const idx = {};
    let i = 0; 
    for (node of nodes) {
        idx[node] = i++; 
    }
    
    const N = nodes.length;
    const graph = Array.from({ length: N }, () => Array(N).fill(0));
    for (const ticket of tickets) {
        const [a, b] = ticket.map(x => idx[x]);
        graph[a][b]++;
    }
    
    function dfs(u) {
        for (let v=0; v<N; v++) {
            if (graph[u][v]) {
                graph[u][v]--;
                answer.push(v);
                dfs(v);
                if (answer.length === K) {
                    return;
                }
                answer.pop();
                graph[u][v]++;
            }
        }
    }
    
    const K = tickets.length + 1;
    const start = idx["ICN"];
    let answer = [start];
    dfs(start);

    return answer.map(x => nodes[x]);
}