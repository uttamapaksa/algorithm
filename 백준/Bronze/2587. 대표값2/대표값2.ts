let nums: number[] = require("fs").readFileSync(process.platform==="linux"?0:"input.txt").toString().trim().split("\n").map(Number)
nums = nums.sort((a,b)=>a-b)
console.log(nums.reduce((a,c)=>a+c, 0) / 5)
console.log(nums[2])