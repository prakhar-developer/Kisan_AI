
function setLanguage(lang) {
  fetch(`/set-language/${lang}/`)
    .then(response => {
      if (response.ok) {
        // Save language choice in localStorage
        localStorage.setItem('languageSelected', 'true');
        document.getElementById('languageModal').style.display = 'none';
        location.reload();
      }
    });
}

window.addEventListener('DOMContentLoaded', () => {
  const languageSelected = localStorage.getItem('languageSelected');
  if (languageSelected === 'true') {
    document.getElementById('languageModal').style.display = 'none';
  }
});
document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('languageModal');

  // check if language already selected
  const selected = localStorage.getItem('languageSelected');
  if (selected) {
    modal.style.display = 'none';
  }

  window.setLanguage = function(lang) {
    fetch(`/set-language/${lang}/`)
      .then(() => {
        localStorage.setItem('languageSelected', 'true');
        modal.style.display = 'none';
        location.reload();
      });
  };
});
