function gcdfunc(a: number, b: number): number {
    if (b === 0) return a
    return gcdfunc(b, a % b)
}

function mod(s: string): number {
    let remainder = 0;
    for (let i=0; i<s.length; i++) {
        remainder = (remainder * 10 + parseInt(s[i])) % K
    }
    return remainder
}

const [_, ...__] = require('fs').readFileSync(process.platform==='linux'?0:'input.txt').toString().trim().split('\n').map((x:string)=>x.trim())
const N = parseInt(_)
const K = parseInt(__.pop())
const digit: number[] = [1, 1]; for (let i=2; i<=51; i++) {digit.push((digit[i-1] * 10) % K)} // digit[i] = (10 ** (i - 1)) % K
const nums: number[][] = __.map((x: string) => [mod(x), x.length]) // nums[i] = [Number(__[i]) % K, __[i].length]
const rest: number[][] = Array.from({length: K}, (_, r) => Array.from({length: N}, (_, i) => (r * digit[nums[i][1]+1] + nums[i][0]) % K)) // rest[r][i] = Number(`${r}{nums[i][0]}`) % K
const dp: number[][] = Array.from({ length: 1 << N }, () => Array(K).fill(0)) // dp[visit][remain] = count
dp[0][0] = 1

for (let visit = 0; visit < (1 << N); visit++) {
    for (let i = 0; i < N; i++) {
        if (visit & (1 << i)) continue;
        for (let r = 0; r < K; r++) {
            dp[visit | (1 << i)][rest[r][i]] += dp[visit][r];
        }
    }
}

const p = dp[(1 << N) - 1][0]
const q = dp[(1 << N) - 1].reduce((acc, val) => acc + val);
const gcd = gcdfunc(p, q);
console.log(`${p / gcd}/${q / gcd}`);