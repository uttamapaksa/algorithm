let[N,B]=require('fs').readFileSync(0).toString().trim().split(' ').map(Number),ans=''
while(N){let r=N%B;ans+=r<10?r:String.fromCharCode(55+r);N=Math.trunc(N/B)}
console.log(ans.split('').reverse().join(''))