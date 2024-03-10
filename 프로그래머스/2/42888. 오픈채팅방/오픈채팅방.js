function solution(records) {
    const user = {}
    let ans = []
    
    records.forEach(record => {
        const [oper, id, name] = record.split(' ')      
        if (oper == 'Enter' || oper == 'Change') {
            user[id] = name
        }
    })
    
    records.forEach(record => {
        const [oper, id, name] = record.split(' ')      
        if (oper == 'Enter') {
            ans.push(`${user[id]}님이 들어왔습니다.`)
        } else if (oper == 'Leave') {
            ans.push(`${user[id]}님이 나갔습니다.`)
        }
    })

    return ans;
}