function solution(n, computers) {
    const visit = Array(n).fill(false);
    let answer = 0;
    
    function dfs(u) {
        for (let v=0; v<n; v++) {
            if (!computers[u][v] || visit[v]) continue;
            visit[v] = true;
            dfs(v);
        }
    }
    
    for (let i=0; i<n; i++) {
        if (visit[i]) continue;
        visit[i] = true;
        answer += 1;
        dfs(i);
    }
    
    
    return answer;
}