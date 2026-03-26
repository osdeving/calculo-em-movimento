document.addEventListener("DOMContentLoaded", () => {
  const isWordChar = (char) => !!char && /[\p{L}\p{N}_]/u.test(char);

  const extractChapterLabel = (title) => {
    if (!title) return null;

    const numericMatch = title.match(/^(\d+)\./);
    if (numericMatch) return numericMatch[1];

    const appendixMatch = title.match(/^Apêndice\s+([A-Z])\./i);
    if (appendixMatch) return appendixMatch[1].toUpperCase();

    return null;
  };

  const applyEditorialMediaLabels = (root) => {
    const heading = root.querySelector("h1");
    const chapterLabel = extractChapterLabel(heading?.textContent?.trim() || "");
    if (!chapterLabel) return;

    let figureCount = 0;
    let videoCount = 0;

    root.querySelectorAll("figure.book-figure").forEach((figure) => {
      const isVideo = !!figure.querySelector("video");
      const count = isVideo ? ++videoCount : ++figureCount;
      const prefix = isVideo ? "Vídeo" : "Figura";
      const editorialLabel = `${prefix} ${chapterLabel}.${count}.`;

      figure.dataset.editorialLabel = editorialLabel;
      figure.dataset.editorialKind = isVideo ? "video" : "figure";

      if (!figure.id) {
        figure.id = `${isVideo ? "video" : "figura"}-${chapterLabel}-${count}`.toLowerCase();
      }

      let caption = figure.querySelector("figcaption");
      if (!caption) {
        caption = document.createElement("figcaption");
        figure.appendChild(caption);
      }

      if (!caption.querySelector(".editorial-label")) {
        const label = document.createElement("span");
        label.className = "editorial-label";
        label.textContent = `${editorialLabel} `;
        caption.prepend(label);
      }
    });
  };

  const autoLinkGlossaryTerms = (root) => {
    if (!Array.isArray(window.BOOK_GLOSSARY) || !window.BOOK_GLOSSARY.length) return;
    const skippedPaths = [
      "/references/",
      "/21-mini-resumo-das-regras-de-calculo-que-realmente-usamos-aqui.html",
      "/22-folha-de-consulta-compacta.html",
      "/23-exercicios-propostos.html",
      "/24-gabarito-dos-exercicios.html",
    ];
    if (skippedPaths.some((path) => window.location.pathname.includes(path))) return;

    const entries = window.BOOK_GLOSSARY.map((entry) => {
      const variants = [entry.term, ...(entry.aliases || [])]
        .filter(Boolean)
        .map((term) => ({
          raw: term,
          regex: new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(/\s+/g, "\\s+"), "iu"),
        }));

      return {
        slug: entry.slug,
        definition: entry.definition,
        variants,
        maxLength: Math.max(...variants.map((variant) => variant.raw.length)),
      };
    }).sort((left, right) => right.maxLength - left.maxLength);

    const linkedTerms = new Set();
    const maxLinks = 12;
    const blockedSelector = [
      "a",
      "code",
      "pre",
      "script",
      "style",
      "h1",
      "h2",
      "h3",
      "h4",
      "h5",
      "h6",
      "figcaption",
      ".inline-math",
      ".display-math",
      ".display-math-inline",
      ".book-lab-footer",
    ].join(", ");

    const findBestMatch = (text) => {
      let best = null;

      entries.forEach((entry) => {
        if (linkedTerms.has(entry.slug)) return;

        entry.variants.forEach((variant) => {
          variant.regex.lastIndex = 0;
          const match = variant.regex.exec(text);
          if (!match) return;

          const start = match.index;
          const end = start + match[0].length;
          if (isWordChar(text[start - 1]) || isWordChar(text[end])) return;

          if (!best || start < best.start || (start === best.start && match[0].length > best.text.length)) {
            best = { entry, start, end, text: match[0] };
          }
        });
      });

      return best;
    };

    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        const text = node.nodeValue || "";
        if (!text.trim()) return NodeFilter.FILTER_REJECT;
        if (!node.parentElement || node.parentElement.closest(blockedSelector)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      },
    });

    const nodes = [];
    while (walker.nextNode()) {
      nodes.push(walker.currentNode);
    }

    nodes.forEach((node) => {
      const original = node.nodeValue || "";
      let cursor = 0;
      let fragment = null;

      while (cursor < original.length) {
        if (linkedTerms.size >= maxLinks) break;
        const slice = original.slice(cursor);
        const match = findBestMatch(slice);
        if (!match) break;

        if (!fragment) fragment = document.createDocumentFragment();
        if (match.start > 0) {
          fragment.appendChild(document.createTextNode(slice.slice(0, match.start)));
        }

        const link = document.createElement("a");
        link.className = "glossary-term";
        link.href = `${path_to_root}references/glossario.html#${match.entry.slug}`;
        link.title = match.entry.definition;
        link.textContent = match.text;
        fragment.appendChild(link);

        linkedTerms.add(match.entry.slug);
        cursor += match.end;
      }

      if (!fragment) return;
      if (cursor < original.length) {
        fragment.appendChild(document.createTextNode(original.slice(cursor)));
      }
      node.parentNode?.replaceChild(fragment, node);
    });
  };

  const stripSidebarChapterNumbers = (root) => {
    if (!root?.querySelectorAll) return;

    root.querySelectorAll(".chapter-item > a").forEach((link) => {
      const autoNumber = link.querySelector("strong[aria-hidden='true']");
      if (!autoNumber) return;

      autoNumber.remove();

      if (link.firstChild?.nodeType === Node.TEXT_NODE) {
        link.firstChild.textContent = link.firstChild.textContent.replace(/^\s+/, "");
      }
    });
  };

  const wireSidebarCleanup = () => {
    stripSidebarChapterNumbers(document);

    const sidebar = document.querySelector("mdbook-sidebar-scrollbox.sidebar-scrollbox");
    if (sidebar) {
      stripSidebarChapterNumbers(sidebar);

      const observer = new MutationObserver(() => {
        stripSidebarChapterNumbers(sidebar);
      });

      observer.observe(sidebar, { childList: true, subtree: true });
    }

    document.querySelectorAll("iframe.sidebar-iframe-outer").forEach((frame) => {
      const cleanupFrame = () => {
        try {
          stripSidebarChapterNumbers(frame.contentDocument);
        } catch (_) {}
      };

      frame.addEventListener("load", cleanupFrame);
      cleanupFrame();
    });
  };

  wireSidebarCleanup();

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

  applyEditorialMediaLabels(main);
  autoLinkGlossaryTerms(main);

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
