// input
const [n, ino, posto]: number[][] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map((x:string)=>x.split(" ").map(Number));
const N: number = n[0];
const L: number[] = Array(N+1).fill(0);
const R: number[] = Array(N+1).fill(0);
const root = posto[N-1];

// create a tree
function subTree(si: number, ei: number) {
    if (si > ei) return 0;
    let p = posto.pop() as number;
    if (si == ei) return p;
    
    let mi = ei;
    while (ino[mi]!== p) {
        mi -= 1;
    }
    
    R[p] = subTree(mi+1, ei) as number; // rigth tree
    L[p] = subTree(si, mi-1) as number; // left tree
    return p;
}
subTree(0, N-1)

// preorder traversal
let ans: string = "";
function preo(x: number) {
    if (x) {
        ans += `${x} `
        preo(L[x])
        preo(R[x])
    }
}
preo(root)

// output
console.log(ans);