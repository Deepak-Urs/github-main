const encode = (arr) => {
    let string = arr.join(',').replace(/,/g, ':;')
    return string
}

const decode = (encodedData) => {
    let res = encodedData.split(':;')
    return res
}

const encodeDecodeStrings = (strArr) => {
    let encodedData = encode(strArr)
    return decode(encodedData)
}

console.log(encodeDecodeStrings(['leet', 'code', 'practice']))