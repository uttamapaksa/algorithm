function f1() {
    for (let r=0; r<N>>1; r++) {
        const tmp = [...arr[r]];
        arr[r] = [...arr[N-1-r]];
        arr[N-1-r] = [...tmp];
    }
}

function f2() {
    for (let r=0; r<N; r++) {
        arr[r] = [...arr[r].reverse()]
    }
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
    const newArr = Array.from({length:N}, ()=>Array(M).fill(0))
    for (let r=0; r<hN; r++) {
        for (let c=0; c<hM; c++) {
            newArr[r][c] = arr[r+hN][c]
        }
    }
    for (let r=0; r<hN; r++) {
        for (let c=hM; c<M; c++) {
            newArr[r][c] = arr[r][c-hM]
        }
    }
    for (let r=hN; r<N; r++) {
        for (let c=hM; c<M; c++) {
            newArr[r][c] = arr[r-hN][c]
        }
    }
    for (let r=hN; r<N; r++) {
        for (let c=0; c<hM; c++) {
            newArr[r][c] = arr[r][c+hM]
        }
    }
    arr = newArr
}

function f6() {
    const hN = N>>1, hM = M>>1
    const newArr = Array.from({length:N}, ()=>Array(M).fill(0))
    for (let r=0; r<hN; r++) {
        for (let c=0; c<hM; c++) {
            newArr[r][c] = arr[r][c+hM]
        }
    }
    for (let r=0; r<hN; r++) {
        for (let c=hM; c<M; c++) {
            newArr[r][c] = arr[r+hN][c]
        }
    }
    for (let r=hN; r<N; r++) {
        for (let c=hM; c<M; c++) {
            newArr[r][c] = arr[r][c-hM]
        }
    }
    for (let r=hN; r<N; r++) {
        for (let c=0; c<hM; c++) {
            newArr[r][c] = arr[r-hN][c]
        }
    }
    arr = newArr
}


let [[N, M, _], ...arr] = require('fs').readFileSync(process.platform === 'linux' ? 0 : 'input.txt').toString().trim().split('\n').map((x) => x.split(' ').map(Number))
const fns = [function(){}, f1, f2, f3, f4, f5, f6]
const ops = arr.pop()

ops.forEach(op => fns[op]())
arr.forEach(row => console.log(row.join(' ')))
