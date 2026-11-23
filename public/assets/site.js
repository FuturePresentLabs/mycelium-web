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


  const api = "https://m.fpl.dev";
  const setStatus = (node, message, tone = "") => {
    if (!node) return;
    node.textContent = message;
    node.dataset.tone = tone;
  };

  const signup = document.querySelector("#hosted-signup");
  if (signup) {
    signup.addEventListener("submit", async (event) => {
      event.preventDefault();
      const email = signup.querySelector("#signup-email")?.value.trim() || "";
      const plan = signup.querySelector("#signup-plan")?.value || "starter";
      const status = signup.querySelector("#signup-status");
      const button = signup.querySelector("button[type=submit]");
      if (!email) return setStatus(status, "Enter the email you want to use.", "error");
      if (button) { button.disabled = true; button.textContent = "Opening Stripe…"; }
      setStatus(status, "Creating your checkout…");
      try {
        const response = await fetch(`${api}/v1/checkout`, {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ email, plan }),
        });
        const value = await response.json().catch(() => ({}));
        if (!response.ok || !value.url) throw new Error(value.error || "Checkout is not available yet.");
        window.location.assign(value.url);
      } catch (error) {
        if (button) { button.disabled = false; button.textContent = "Start 7-day trial →"; }
        setStatus(status, `${error.message} Email hello@fpl.dev if this keeps happening.`, "error");
      }
    });
  }

  const login = document.querySelector("#magic-login");
  if (login) {
    login.addEventListener("submit", async (event) => {
      event.preventDefault();
      const email = login.querySelector("#login-email")?.value.trim() || "";
      const status = login.querySelector("#login-status");
      const button = login.querySelector("button[type=submit]");
      if (!email) return setStatus(status, "Enter the email on your workspace.", "error");
      if (button) { button.disabled = true; button.textContent = "Sending…"; }
      try {
        const response = await fetch(`${api}/v1/login`, {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ email }),
        });
        if (!response.ok) throw new Error("Could not request a link.");
        setStatus(status, "Check your inbox. The link expires in 20 minutes.");
        if (button) button.textContent = "Sent";
      } catch (error) {
        if (button) { button.disabled = false; button.textContent = "Email me a sign-in link →"; }
        setStatus(status, error.message, "error");
      }
    });
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
