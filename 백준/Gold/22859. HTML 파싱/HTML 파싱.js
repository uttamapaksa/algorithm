const input = require("fs").readFileSync(process.platform==='linux'?0:'input.txt').toString().trim();
const N = input.length - 7;
let answer = "";

let i = 6;
while (i < N) {
  const start = input.indexOf("<", i);
  const end = input.indexOf(">", i);
  const tag = input.slice(start + 1, end);
  i = end + 1;
  
  if (tag[0] === "/") continue;

  // p tag
  if (tag === "p") {
    let content = "";
    while (i < N) {
      const start = input.indexOf("<", i);
      const end = input.indexOf(">", i);
      const tag = input.slice(start + 1, end);
      content += input.slice(i, start);
      i = end + 1;

      if (tag !== "/p") continue;

      content = content.trim().split(" ").filter(x => x).join(" ");
      answer += content + "\n";
      break;
    }
  } 
  // div tag
  else {
    answer += "title : " + tag.slice(11, tag.length - 1) + "\n";
  }
}

console.log(answer);