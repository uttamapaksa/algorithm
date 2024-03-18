const [_, ...arr]: string[][] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim().split(' '));
const front: string[] = [], rear: string[] = [];
let fi = 0, ri = 0;
let ans = '';

for (const [oper, num] of arr) {
  switch (oper) {
    case '1':
      front.push(num);
      break;
    case '2':
      rear.push(num);
      break;
    case '3':
      ans += (fi < front.length ? front.pop() : ri < rear.length ? rear[ri++] : '-1') + '\n';
      break;
    case '4':
      ans += (ri < rear.length ? rear.pop() : fi < front.length ? front[fi++] : '-1') + '\n';
      break;
    case '5':
      ans += `${front.length - fi + rear.length - ri}\n`;
      break;
    case '6':
      ans += (front.length - fi + rear.length - ri ? '0' : '1') + '\n';
      break;
    case '7':
      ans += (fi < front.length ? front[front.length-1] : ri < rear.length ? rear[ri] : '-1') + '\n';
      break;
    case '8':
      ans += (ri < rear.length ? rear[rear.length-1] : fi < front.length ? front[fi] : '-1') + '\n';
      break;
  }
}

console.log(ans);