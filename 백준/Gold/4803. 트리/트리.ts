const input: number[][] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x:string)=>x.split(" ").map(Number));
let i: number = 0;
let treeNum: number;
let caseNum: number = 0;

while (input[i][0] !== 0) {
    // create graph
    const [n, m] = input[i];
    const graph: Record<number, number[]> = {};
    const visit: number[] = Array(n+1).fill(0);
    for (let j=1; j<n+1; j++) {
        graph[j] = [];
    }
    for (let j=i+1; j<i+m+1; j++) {
        const [u, v] = input[j];
        graph[u].push(v); 
        graph[v].push(u); 
    }
    i += m+1;
    treeNum = 0;
    caseNum += 1;

    // dfs for treeNum
    function bfs(u: number) {
        const stack: number[] = [u];
        let flag = 1;
        visit[u] = 1;
        while (stack.length) {
            const u = stack.pop() as number;
            for (const v of graph[u]) {
                if (visit[v]) {
                    if (visit[v] === visit[u] - 1) continue; // prev node
                    else flag = 0; continue // cycle
                }
                stack.push(v);
                visit[v] = visit[u] + 1;
            }
        }
        return flag;
    }
    for (let u=1; u<n+1; u++) {
        if (visit[u]) continue;
        treeNum += bfs(u)
    }

    // output   
    if (treeNum === 0) console.log(`Case ${caseNum}: No trees.`);
    else if (treeNum == 1) console.log(`Case ${caseNum}: There is one tree.`);
    else console.log(`Case ${caseNum}: A forest of ${treeNum} trees.`);
}