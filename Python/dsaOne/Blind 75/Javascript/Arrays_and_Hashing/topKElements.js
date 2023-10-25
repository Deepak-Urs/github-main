const topKElements = (ele, k) => {
    let hm = new Map()
    let arr = []
    let res = []

    for (let i = 0; i < ele.length; i++) {
        if(hm.has(ele[i])) {
            let val = hm.get(ele[i])
            hm.set(ele[i], val+1)
        }
        else {
            hm.set(ele[i], 1)
        }
    }

    hm.forEach((v,k) => {
        arr.push([v, k])
    })
    arr.sort((a,b) => b[0] - a[0])

    for(let j = 0; j < k; j++) {
        res.push(arr[j][1])
    }

    return res
}

console.log(topKElements([5,5,5,10,10,15],2))
console.log(topKElements([3,0,1,0],1))