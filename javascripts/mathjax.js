window.MathJax = {
  tex: {
    inlineMath: [["$", "$"], ["\\(", "\\)"]],
    displayMath: [["$$", "$$"], ["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  // Scale MathJax output to match the surrounding body text.
  // Without this, symbols like ∈, ℝ, ≠ render at their natural size
  // and visually overflow the paragraph line-height.
  startup: {
    ready: () => {
      MathJax.startup.defaultReady();
      // Force a uniform scale on inline math so it matches the body font size
      // (mkdocs-material sets .md-typeset { font-size: .8rem } for desktop).
      MathJax.config?.scale || (MathJax.config.scale = 1);
    }
  }
};
