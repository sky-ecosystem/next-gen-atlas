module.exports = {
  names: ["no-unicode-list-markers"],
  description: "Disallow unicode characters as list markers (◦ and ▪)",
  tags: ["typography"],
  function: function rule(params, onError) {
    const forbidden = [
      { char: "\u25E6", name: "white bullet (◦)" },
      { char: "\u25AA", name: "black small square (▪)" },
    ];

    params.lines.forEach((line, i) => {
      forbidden.forEach(({ char, name }) => {
        let col = line.indexOf(char);
        while (col !== -1) {
          onError({
            lineNumber: i + 1,
            detail: `Unicode list marker found: ${name}`,
            context: line.trim(),
            range: [col + 1, 1],
          });
          col = line.indexOf(char, col + 1);
        }
      });
    });
  },
};