function solution(triangle) {
    const N = triangle.length
    
    for (let i=1; i<N; i++) {
        triangle[i][0] += triangle[i-1][0]
        triangle[i][i] += triangle[i-1][i-1]
    }
    
    for (let i=1; i<N; i++) {
        for (let j=1; j<i; j++) {
            triangle[i][j] += Math.max(triangle[i-1][j-1], triangle[i-1][j])   
        }
    }
    
    answer = Math.max(...triangle[N-1])
    return answer
}