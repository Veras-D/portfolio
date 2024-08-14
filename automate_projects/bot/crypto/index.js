const axios = require("axios");
const crypto = require("crypto");

const SYMBOL = "BTCUSDT";
const URL_API = "https://testnet.binance.vision";  // https://api.binance.com

var historicoDeLucros = [];
let isBuy = false;
let valorCompra = null;


function calcSMA(data){
    if(data.length === 0) return null;
    const close = data.map(candle => parseFloat(candle[4]));
    const sum = close.reduce((a, b) => a + b, 0);
    return sum / data.length;
}


async function start() {
    try {
        // Comandos do bot
        const { data } = await axios.get(URL_API + "/api/v3/klines?limit=21&interval=15m&symbol=" + SYMBOL);
        const cotacaoAtual = data[data.length - 1];  // [time, open, high, low, close, volume, ...]
        const priceClose = parseFloat(cotacaoAtual[4]);

        console.clear();
        console.log(`Preço Atual: ${priceClose}`);

        const sma21 = calcSMA(data);
        const sma13 = calcSMA(data.slice(8));
        console.log("SMA (13): " + sma13);
        console.log("SMA (21): " + sma21);
        console.log("Comprado? " + isBuy);

        if(sma13 > sma21 && !isBuy){
            console.log(`Comprado a: ${priceClose}`);
            isBuy = true;
            valorCompra = priceClose;
        }
        else if(sma13 < sma21 && isBuy){
            console.log(`Vendido a: ${priceClose}`);
            const lucro = (priceClose - valorCompra) / valorCompra * 100;
            console.log(`O lucro foi de: ${lucro}%`);
            isBuy = false;
            historicoDeLucros.push(lucro);
        }
        else{
            console.log("Nenhuma operação realizada");
            console.log(`Histórico de Lucros: ${historicoDeLucros}`);
        }
    }
    catch (error) {
        console.error(`Erro ao acessar a API: ${error}`);
    }
}

setInterval(start, 15 * 60000);
start();
