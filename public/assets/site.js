// Mycelium marketing site — minimal progressive enhancement.
(() => {
  const header = document.querySelector(".site-header");
  const menu = document.querySelector(".menu-button");
  if (header && menu) {
    menu.addEventListener("click", () => {
      const open = header.classList.toggle("nav-open");
      menu.setAttribute("aria-expanded", String(open));
    });
    header.querySelectorAll(".nav a").forEach((link) => {
      link.addEventListener("click", () => {
        header.classList.remove("nav-open");
        menu.setAttribute("aria-expanded", "false");
      });
    });
  }

  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", async () => {
      const value = button.getAttribute("data-copy") || "";
      try {
        await navigator.clipboard.writeText(value);
        const old = button.textContent;
        button.textContent = "Copied";
        setTimeout(() => { button.textContent = old; }, 1400);
      } catch {
        button.textContent = "Select";
      }
    });
  });

  const billingButtons = Array.from(document.querySelectorAll("[data-billing]"));
  const priceNodes = Array.from(document.querySelectorAll("[data-monthly]"));
  if (billingButtons.length && priceNodes.length) {
    const setBilling = (mode) => {
      billingButtons.forEach((button) => {
        button.classList.toggle("is-active", button.dataset.billing === mode);
      });
      priceNodes.forEach((node) => {
        node.textContent = mode === "annual" ? node.dataset.annual : node.dataset.monthly;
      });
      document.querySelectorAll("[data-annual-note]").forEach((node) => {
        node.textContent = mode === "annual" ? "2 months free · billed yearly" : "billed monthly";
      });
    };
    billingButtons.forEach((button) => {
      button.addEventListener("click", () => setBilling(button.dataset.billing));
    });
    setBilling("monthly");
  }

  const reveals = Array.from(document.querySelectorAll(".reveal"));
  if (reveals.length) {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) {
      reveals.forEach((node) => node.classList.add("is-visible"));
    } else {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: .12 });
      reveals.forEach((node) => observer.observe(node));
    }
  }

  const year = document.querySelector("[data-year]");
  if (year) year.textContent = new Date().getFullYear();
})();
