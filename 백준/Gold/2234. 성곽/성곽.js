const [[M, N], ...arr] = require('fs').readFileSync(0).toString().trim().split('\n').map(x=>x.split(' ').map(Number));
const roomIdAndArea = [[0, 0]];
const visit = Array.from({length: N}, ()=>Array(M).fill(0));

for (let i=0; i<N; i++) {
    for (let j=0; j<M; j++) {
        if (visit[i][j]) continue;
        const roomId = roomIdAndArea.length;
        roomIdAndArea.push([roomId, 1]);
        visit[i][j] = roomId;
        const stack = [[i, j]];
        while (stack.length) {
            const [r, c] = stack.pop();
            const val = arr[r][c];
            for (let [w, nr, nc] of [[1,r,c-1],[2,r-1,c],[4,r,c+1],[8,r+1,c]]) {
                if (!(val & w)) {
                    if (0 <= nr && nr < N && 0 <= nc && nc < M && !visit[nr][nc]) {
                        roomIdAndArea[roomId][1]++;
                        visit[nr][nc] = roomId;
                        stack.push([nr, nc]);
                    }
                }
            }
        }
    }
}

const graph = []
for (let i=0; i<roomIdAndArea.length; i++) {
    graph.push(new Set());
}
for (let r=0; r<N; r++) {
    for (let c=0; c<M; c++) {
        const roomId = visit[r][c];
        for (let [nr, nc] of [[r,c-1],[r-1,c],[r,c+1],[r+1,c]]) {
            if (0 <= nr && nr < N && 0 <= nc && nc < M && roomId !== visit[nr][nc]) {
                graph[roomId].add(visit[nr][nc]);
            }
        }
    }
}

console.log(roomIdAndArea.length-1);
console.log(Math.max(...roomIdAndArea.map(x=>x[1])));
let maxTwoRoom = 0;
for (let i=1; i<roomIdAndArea.length; i++) {
    maxTwoRoom = Math.max(maxTwoRoom, Math.max(...[...graph[i]].map(j => roomIdAndArea[i][1] + roomIdAndArea[j][1])));
}
console.log(maxTwoRoom);
