function solution(n, works) {
    if (works.reduce((a, c) => a + c, 0) <= n) return 0;
        
    const L = works.length;
    works = works.sort((a, b) => b - a)
    
    for (let i=1; i<L; i++) {
        const diff = works[i-1] - works[i]
        if (diff) {
            if (i * diff <= n) {
                n -= i * diff
                for (let j=0; j<i; j++) {
                    works[j] -= diff
                }
            } else {
                const div = Math.trunc(n / i)
                const mod = n - div * i
                n = 0
                for (let j=0; j<i; j++) {
                    works[j] -= div
                }
                for (let j=0; j<mod; j++) {
                    works[j] -= 1
                }
                break
            }
        }
    }
    
    if (n) {
        const div = Math.trunc(n / L)
        const mod = n - div * L
        for (let j=0; j<L; j++) {
            works[j] -= div
        }
        for (let j=0; j<mod; j++) {
            works[j] -= 1
        }
    }
    
    return works.reduce((a, c) => a + c ** 2, 0)
}
