const getMinSum = (sec_val, msg) => {
    let list = []

    for(let i =0; i < msg.length; i++){
        let idx = parseInt(msg[i].charCodeAt(0) - 'a'.charCodeAt(0))
        let val = sec_val[idx]
        list.push(val)
    }
    
    list.sort((a,b) => a - b)
    console.log('list seen', list)
    
    let res = []
    for(let j = 0; j < list.length-1; j++) {
        res = res + list[j+1] - list[j]
    }
    return res
}

console.log(getMinSum([1,2,1,3,1,3,5,7,1,1], 'afeb'))