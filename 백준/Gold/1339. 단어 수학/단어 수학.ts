const [_, ...words]: string[][] = require("fs").readFileSync(process.platform==="linux"?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(''));
const chars: Record<string, number> = {};

for (const word of words) {
    const len = word.length;
    for (let i = 0; i < len; i++) {
        const char = word[i];
        if (!chars[char]) {
            chars[char] = 10 ** (len - i - 1);
        } else {
            chars[char] += 10 ** (len - i - 1);
        }
    }
}

let answer = 0;
let num = 9

const arr = Object.entries(chars).sort((a, b) => b[1] - a[1]);
for (const [_, val] of arr) {
    answer += num-- * val;
}

console.log(answer);