var btc = document.getElementById("bitcoin");
var ltc = document.getElementById("litecoin");
var eth = document.getElementById("ethereum");
var doge = document.getElementById("dogecoin");
var btc01=document.getElementById("bitcoin01");
var ltc01 = document.getElementById("litecoin01");
var eth01 = document.getElementById("ethereum01");
var doge01 = document.getElementById("dogecoin01");

var liveprice = {
    "async": true,
    "scroosDomain": true,
    "url": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Cethereum%2Cdogecoin&vs_currencies=usd%2Cinr",

    "method": "GET",
    "headers": {}
}

$.ajax(liveprice).done(function (response){
  //  console.log(response);
   

    
    btc.innerHTML = response.bitcoin.usd;
    ltc.innerHTML = response.litecoin.usd;
    eth.innerHTML = response.ethereum.usd;
    doge.innerHTML = response.dogecoin.usd;
    btc01.innerHTML = response.bitcoin.inr;
    ltc01.innerHTML = response.litecoin.inr;
    eth01.innerHTML = response.ethereum.inr;
    doge01.innerHTML = response.dogecoin.inr;
    

});