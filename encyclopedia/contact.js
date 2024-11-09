const submit = document.querySelector('input[type="submit"]');

submit.addEventListener("click", (e) => {
  e.preventDefault();
  window.location.href = "/entry.html";
});
