def solution(fees, records):
    times = {}
    parking = {}
    
    for record in records:
        time, num, inout = record.split()
        if inout == 'IN':
            parking[num] = int(time[:2]) * 60 + int(time[3:])
        else:
            diff = int(time[:2]) * 60 + int(time[3:]) - parking[num]
            times[num] = times.get(num, 0) + diff
            del parking[num]
    
    for num, time in parking.items():
        times[num] = times.get(num, 0) + (24 * 60 -1 - time)
    
    ans = []
    a, b, c, d = fees
    for num, time in sorted(times.items()): 
        ans.append(b)
        if time > a:
            ans[-1] += ((time - a - 1) // c + 1) * d
        
    return ans