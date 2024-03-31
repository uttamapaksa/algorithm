function solution(data, col, row_begin, row_end) {
    // ORDER BY col, 1 DESC
    data = data.sort((a, b) => a[col-1] < b[col-1] ? -1 : a[col-1] === b[col-1] ? a[0] > b[0] ? -1 : 1 : 1);
    
    // S_i
    let answer = 0;
    for (let i = row_begin-1; i <= row_end-1; i++) {
        let tmp = 0
        for (const col of data[i]) {
            tmp += col % (i+1);
        }
        answer ^= tmp;
    }
    
    return answer;
}