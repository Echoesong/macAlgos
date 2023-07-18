

var productExceptSelf = function(nums) {
    let ourArray = nums
    let cache
    let output = []
    for(let i=0; i<nums.length; i++){
        let ignore = i
        cache = ourArray.splice(ignore, 1)
        output.push(ourArray.reduce((a, b) => {
            return a * b
        }))
        ourArray.splice(ignore, 0, cache)
    }
    return output
};
let numbers = [-1,1,0,-3,3]
console.log(productExceptSelf(numbers))