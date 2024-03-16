const [_, ...input]: string[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' '));
const queue: string[] = [];
let idx = 0
let ans = ''

for (const x of input) {
  switch (x[0]) {
    case 'push':
      queue.push(x[1]);
      break;
    case 'pop':
      ans += (idx === queue.length) ? '-1\n' : (queue[idx++] + '\n');
      break;
    case 'size':
      ans += `${queue.length - idx}\n`;
      break;
    case 'empty':
      ans += `${queue.length === idx ? 1 : 0}\n`;
      break;
    case 'front':
      ans += `${queue.length === idx ? -1 : queue[idx]}\n`;
      break;
    case 'back':
      ans += `${queue.length === idx ? -1 : queue[queue.length - 1]}\n`;
      break;
  }
}

console.log(ans);