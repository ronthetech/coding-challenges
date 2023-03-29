/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let str = s.replace(/[^a-zA-Z0-9]/g,"").toLowerCase();
    let reverse = str.split("").reverse().join("");
    return str === reverse; 
};