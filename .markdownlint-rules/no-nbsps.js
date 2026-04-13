module.exports = {
  names: ["no-nbsp"],
  description: "No non-breaking spaces",
  tags: ["whitespace"],
  function: function(params, onError) {
    params.lines.forEach(function(line, i) {
      let col = 0;
      while ((col = line.indexOf("\u00a0", col)) !== -1) {
        onError({
          lineNumber: i + 1,
          detail: `NBSP at column ${col + 1}`,
          range: [col + 1, 1]
        });
        col++;
      }
    });
  }
};