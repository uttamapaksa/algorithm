function f1() {
    for (let r=0; r<N>>1; r++) {
        [arr[r], arr[N-1-r]] = [arr[N-1-r], arr[r]]
    }
}

function f2() {
    arr.forEach(row => row.reverse())
}

function f3() {
    const newArr = Array.from({length:M}, ()=>Array(N).fill(0))
    for (let r=0; r<M; r++) {
        for (let c=0; c<N; c++) {
            newArr[r][c] = arr[N-1-c][r]
        }
    }
    [N, M] = [M, N]
    arr = newArr
}

function f4() {
    const newArr = Array.from({length:M}, ()=>Array(N).fill(0))
    for (let r=0; r<M; r++) {
        for (let c=0; c<N; c++) {
            newArr[r][c] = arr[c][M-1-r]
        }
    }
    [N, M] = [M, N]
    arr = newArr
}

function f5() {
    const hN = N>>1, hM = M>>1
    for (let r=0; r<hN; r++) {
        for (let c=0; c<hM; c++) {
            const tmp = arr[r][c];
            arr[r][c] = arr[r + hN][c];
            arr[r + hN][c] = arr[r + hN][c + hM];
            arr[r + hN][c + hM] = arr[r][c + hM];
            arr[r][c + hM] = tmp;
        }
    }
}

function f6() {
    const hN = N>>1, hM = M>>1
    for (let r=0; r<hN; r++) {
        for (let c=0; c<hM; c++) {
            const tmp = arr[r][c];
            arr[r][c] = arr[r][c + hM];
            arr[r][c + hM] = arr[r + hN][c + hM];
            arr[r + hN][c + hM] = arr[r + hN][c];
            arr[r + hN][c] = tmp;
        }
    }
}

let [[N, M, _], ...arr] = require('fs').readFileSync(0).toString().trim().split('\n').map((x) => x.split(' ').map(Number))
const fns = [function(){}, f1, f2, f3, f4, f5, f6]
const ops = arr.pop()

ops.forEach(op => fns[op]())
arr.forEach(row => console.log(row.join(' ')))
