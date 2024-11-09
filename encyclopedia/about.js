const spans = document.querySelectorAll("span");

document.addEventListener("DOMContentLoaded", function (e) {
  e.preventDefault();

  let name;
  let preferName;
  spans.forEach((span, i) => {
    name = span.textContent.split(" ");
    if (name.length > 0) {
      name[name.length - 1] = name[name.length - 1].toUpperCase();
    }
    preferName = name.join(" ");

    span.innerHTML = preferName;
  });
});
