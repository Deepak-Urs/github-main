//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

const maxProfit = (prices) => {
    let maxP = 0
    let l = 0
    let r = 1

    while(r <= (prices.length - 1)) {
        if(prices[l] <= prices[r]) {
            maxP = Math.max(maxP, (prices[r] - prices[l]))
            console.log('maxP seen', maxP)
            r++;
        }
        else if(prices[l] > prices[r]){
            l = r;
            r++
        }
    }

    return maxP
}

console.log(maxProfit([7,1,5,3,6,4]))
console.log(maxProfit([7,6,4,3,1]))