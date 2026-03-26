document.addEventListener("DOMContentLoaded", () => {
  const main = document.querySelector(".content main");
  if (!main) return;

  const mathTargets = [];
  main.querySelectorAll("[data-math-inline]").forEach((node) => {
    const expr = node.getAttribute("data-math-inline");
    if (!expr) return;
    node.textContent = `\\(${expr}\\)`;
    mathTargets.push(node);
  });

  main.querySelectorAll("[data-math-display]").forEach((node) => {
    const expr = node.getAttribute("data-math-display");
    if (!expr) return;
    node.textContent = `\\[${expr}\\]`;
    mathTargets.push(node);
  });

  const standaloneImages = main.querySelectorAll("p > img:only-child");
  standaloneImages.forEach((img) => {
    const parent = img.parentElement;
    if (!parent || parent.parentElement?.classList.contains("book-figure")) return;

    const figure = document.createElement("figure");
    figure.className = "book-figure";

    parent.replaceWith(figure);
    figure.appendChild(img);

    const captionText = (img.getAttribute("alt") || "").trim();
    if (captionText) {
      const caption = document.createElement("figcaption");
      caption.textContent = captionText;
      figure.appendChild(caption);
    }
  });

  if (!main.querySelector(".book-lab-footer")) {
    const footer = document.createElement("footer");
    footer.className = "book-lab-footer";
    footer.innerHTML = [
      "<span>Cálculo em Movimento</span>",
      "<span>Conteúdo em Markdown, renderização via mdBook</span>",
      "<span>Laboratório editorial</span>",
    ].join("");
    main.appendChild(footer);
  }

  const videos = main.querySelectorAll("video[data-autoplay-when-visible]");
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const video = entry.target;
          if (!(video instanceof HTMLVideoElement)) return;

          if (entry.isIntersecting) {
            video.play().catch(() => {});
          } else {
            video.pause();
          }
        });
      },
      { threshold: 0.65 }
    );

    videos.forEach((video) => observer.observe(video));
  }

  const typesetMath = () => {
    if (!mathTargets.length || !window.MathJax?.typesetPromise) return;
    window.MathJax.typesetPromise(mathTargets).catch(() => {});
  };

  if (window.MathJax?.typesetPromise) {
    typesetMath();
  } else if (mathTargets.length) {
    window.addEventListener("load", typesetMath, { once: true });
  }
});
