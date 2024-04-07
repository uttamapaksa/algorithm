function solution(players, callings) {
    let RankIdx = {};
    let RankName = {};
    for (let i=0; i < players.length; i++) {
        RankIdx[i] = players[i] // idx : name
        RankName[players[i]] = i // name : idx
    }
    
    let changeIdx = 0;
    let changeName = 0;
    for (calling of callings) {
        // get
        changeIdx = RankName[calling]
        changeName = RankIdx[changeIdx - 1]
        // set
        RankName[calling] -= 1
        RankName[changeName] += 1
        RankIdx[changeIdx-1] = calling
        RankIdx[changeIdx] = changeName
    }
    
    return Object.values(RankIdx);
}