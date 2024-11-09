let[_,a]=require('fs').readFileSync(0).toString().split('\n').map(x=>x.split(' ').map(x=>+x));r=[];s=e=m=0
a.map(v=>{
  s=0;e=r.length
  while(s<e){
    m=parseInt((s+e)/2)
    if(v>r[m])s=m+1
    else e=m
  }
  if(s==r.length)r.push(v)
  else r[s]=v 
})
console.log(r.length)