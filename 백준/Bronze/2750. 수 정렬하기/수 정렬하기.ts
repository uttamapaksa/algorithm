const [N, ...arr] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split(/\s+/).map(Number);
console.log(arr.sort((a: number, b:  number) => a - b).join("\n"))