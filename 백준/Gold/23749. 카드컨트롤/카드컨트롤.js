const check = (card) => {
  let res = 0
  for (let i=0; i<N; i+=2) {
    if (card[i] === '1' && card[i+1] === '0') res++
    else if (card[i] === '0' && card[i+1] === '1') res--
  }
  if (res > 0) return true
  return false
}

let [[N], card] = require('fs').readFileSync(process.platform === 'linux' ? 0 : 'input.txt').toString().trim().split('\n').map(x=>x.split(' '))
N <<= 1
card = card.reduce((a, c) => a + (c==='X'?'0':'1'), '')
const visit = new Map()
visit.set(card, 0)
const queue = [card]
let front = 0

while (front < queue.length) {
  const card = queue[front++]
  const cnt = visit.get(card)
  if (check(card)) {
    console.log(cnt);
    break
  }
  for (let i=1; i<N; i++) {
    const newCard = card[i] + card.slice(0,i) + card.slice(i+1)
    if (visit.has(newCard)) continue
    visit.set(newCard, cnt+1)
    queue.push(newCard)
  }
}
