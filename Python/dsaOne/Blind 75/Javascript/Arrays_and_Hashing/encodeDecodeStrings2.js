const encode = (arr) => {
    let string = ''
    for(let i = 0; i < arr.length; i++) {
        string += `${arr.length}#${arr[i]}`
    }
    return string
}

const decode = (str) => {
    console.log('encoded string', str);
    let res = []
    let i = 0
    while(i < str.length){
        len = parseInt(str[i])
        if(len !== NaN && str[i+1] == '#') {
            idx = i + 2
            res.push(str.slice(idx, idx+len))
        }
        i = idx + len
    }
    return res
}

function main(data) {
    let encodeString = encode(data)
    let res = decode(encodeString)
    console.log(res)
}

main(['leet', 'code', 'love', 'you'])