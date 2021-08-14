const fs = require("fs");

const dir = fs.readdirSync("./");

dir.map((d) => {
  if (fs.lstatSync(`${__dirname}/${d}`).isDirectory() && !d.startsWith(".")) {
    try {
      const files = fs.readFileSync(`${__dirname}/${d}/index.md`).toString();
      try {
        const cont = fs.readFileSync("");
      } catch (err) {}
    } catch (err) {}
  }
});
