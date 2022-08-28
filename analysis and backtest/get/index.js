var CryptoJS = require("crypto-js");
var fs = require("fs");
const { promisify } = require("util");
const writeFileAsync = promisify(fs.appendFile);

var game_hash_input =
  "bdbdf909aadd399c54b9c4abff1f9ec52a1e0d27be4121294b593ebe8bc7e376";
var game_salt_input =
  "0000000000000000000e3a66df611d6935b30632f352e4934c21059696117f28";
var game_amount_input = 1000000;

var isVerifying = false;

async function getData() {
  if (isVerifying) return;
  isVerifying = true;

  data = "";
  let prevHash = null;
  for (let i = 0; i < game_amount_input; i++) {
    let hash = String(
      prevHash ? CryptoJS.SHA256(String(prevHash)) : game_hash_input
    );
    let bust = gameResult(hash, game_salt_input);
    //   addTableRow(hash, bust, i);
    console.log(hash, "---", bust);
    await writeFileAsync("mynewfile3.txt", bust + "\n", function (err) {
      if (err) throw err;
    });
    prevHash = hash;
  }
}

const gameResult = (seed, salt) => {
  const nBits = 52; // number of most significant bits to use

  // 1. HMAC_SHA256(message=seed, key=salt)
  if (salt) {
    const hmac = CryptoJS.HmacSHA256(CryptoJS.enc.Hex.parse(seed), salt);
    seed = hmac.toString(CryptoJS.enc.Hex);
  }

  // 2. r = 52 most significant bits
  seed = seed.slice(0, nBits / 4);
  const r = parseInt(seed, 16);

  // 3. X = r / 2^52
  let X = r / Math.pow(2, nBits); // uniformly distributed in [0; 1)
  X = parseFloat(X.toPrecision(9));

  // 4. X = 99 / (1-X)
  X = 99 / (1 - X);

  // 5. return max(trunc(X), 100)
  const result = Math.floor(X);
  return Math.max(1, result / 100);
};

getData();
