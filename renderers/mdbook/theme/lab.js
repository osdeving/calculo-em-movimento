document.addEventListener("DOMContentLoaded", () => {
  const main = document.querySelector(".content main");
  if (!main) return;

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
});
