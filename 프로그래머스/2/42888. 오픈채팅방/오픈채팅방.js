function solution(records) {
    const ans = []
    const names = {}
    const messages = []
    
    records.forEach(record => {
        const [oper, id, name] = record.split(' ')      
        if (oper == 'Enter') {
            names[id] = name
            messages.push([id, '님이 들어왔습니다.'])
        } else if (oper == 'Change') {
            names[id] = name
        } else {
            messages.push([id, '님이 나갔습니다.'])
        }
    })
    
    messages.forEach(message => {
        const [id, mes] = message
        ans.push(`${names[id]}` + mes)
    })

    return ans;
}