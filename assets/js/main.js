// Use the saved theme, or follow the operating system preference.
const themeToggle = document.querySelector(".theme-toggle");
const colorPreference = window.matchMedia("(prefers-color-scheme: dark)");

function savedTheme() {
  try {
    return window.localStorage.getItem("theme");
  } catch {
    return null;
  }
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  if (themeToggle) {
    const label = `Switch to ${theme === "dark" ? "light" : "dark"} theme`;
    themeToggle.setAttribute("aria-label", label);
    themeToggle.setAttribute("title", label);
  }
}

function detectOSColorTheme() {
  const saved = savedTheme();
  applyTheme(saved === "light" || saved === "dark"
    ? saved
    : colorPreference.matches ? "dark" : "light");
}

if (themeToggle) {
  themeToggle.addEventListener("click", () => {
    const theme = document.documentElement.getAttribute("data-theme") === "dark"
      ? "light" : "dark";
    try {
      window.localStorage.setItem("theme", theme);
    } catch {
      // The theme can still change when storage is unavailable.
    }
    applyTheme(theme);
  });
}

colorPreference.addEventListener("change", detectOSColorTheme);
detectOSColorTheme();
