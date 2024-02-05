function sol() {
  let nxy1 = "";
  let nxy2 = "";
  let prev: Record<string, number> = {[`1025 ${N*1024 + N}`]: 0}; // idx1, idx2 : minv
  let curr: Record<string, number> = {};
  let prevpath: Record<string, string> = {[`1025 ${N*1024 + N}`]: ""};
  let currpath: Record<string, string> = {};

  for (const [x, y] of arr) {
    curr = {};
    currpath = {};
    for (const idx in prev) {
      const [car1, car2] = idx.split(" ").map(Number);
     const [r1, c1] = [car1 >> 10, car1 & 1023];
      const [r2, c2] = [car2 >> 10, car2 & 1023];
      nxy1 = `${1024*x+y} ${car2}`  
      nxy2 = `${car1} ${1024*x+y}`  
      
      // car 1
      if (!curr[`${nxy1}`]) {
        curr[`${nxy1}`] = prev[idx] + Math.abs(r1-x) + Math.abs(c1-y);
        currpath[`${nxy1}`] = prevpath[idx] + "1";
      } else {
        if (curr[`${nxy1}`] > prev[idx] + Math.abs(r1-x) + Math.abs(c1-y)) {
          curr[`${nxy1}`] = prev[idx] + Math.abs(r1-x) + Math.abs(c1-y);
          currpath[`${nxy1}`] = prevpath[idx] + "1";
        }
      }
      // car 2
      if (!curr[`${nxy2}`]) {
        curr[`${nxy2}`] = prev[idx] + Math.abs(r2-x) + Math.abs(c2-y);
        currpath[`${nxy2}`] = prevpath[idx] + "2";
      } else {
        if (curr[`${nxy2}`] > prev[idx] + Math.abs(r2-x) + Math.abs(c2-y)) {
          curr[`${nxy2}`] = prev[idx] + Math.abs(r2-x) + Math.abs(c2-y);
          currpath[`${nxy2}`] = prevpath[idx] + "2";
        }
      }
    }
    prev = curr;
    prevpath = currpath;
  }
  
  let maxv = 2000000;
  let maxi = "";
  for (const idx in prev) {
    if (maxv > prev[idx]) {
      maxv = prev[idx];
      maxi = idx;
    }
  }
  const ans = `${prev[maxi]}\n${prevpath[maxi].split("").join("\n")}`
  return ans
}


let [N, W, ...arr] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n");
N = parseInt(N);
W = parseInt(W);
arr = arr.map((x:string)=>x.trim().split(" ").map(Number));
console.log(sol());