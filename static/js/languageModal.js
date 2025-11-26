function setLanguage(langCode) {
  // Store in localStorage
  localStorage.setItem("preferredLanguage", langCode);

  // Set cookie for Django i18n (optional but recommended)
  document.cookie = `django_language=${langCode};path=/`;

  // Call Django view to update session and mark language as selected
  fetch(`/set-language/${langCode}/`)
    .then(response => {
      if (response.ok) {
        // Hide modal and reload to reflect language
        document.getElementById("languageModal").style.display = "none";
        window.location.reload();
      } else {
        console.error("Failed to set language on server.");
      }
    })
    .catch(error => {
      console.error("Language set failed", error);
    });
}

document.addEventListener("DOMContentLoaded", () => {
  const lang = localStorage.getItem("preferredLanguage");
  const modal = document.getElementById("languageModal");
  if (!lang && modal) {
    modal.style.display = "flex";
  } else if (modal) {
    modal.style.display = "none";
  }
});
