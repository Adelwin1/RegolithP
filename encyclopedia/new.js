import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

const markdownInput = document.getElementById("markdown");
const outputDiv = document.getElementById("output");
const title = document.getElementById("title");
const btnSave = document.querySelector(".btn-save");
const btnExit = document.querySelector(".btn-exit");
const author = document.getElementById("author");

markdownInput.addEventListener("input", function (e) {
  if (title.value === "" || author.value === "") {
    alert("Give a title and author of your entry before the content");
    author.focus();
    e.target.value = "";
    return;
  }
  e.preventDefault();
  const markdownText = e.target.value;
  const htmlText = marked(markdownText);
  outputDiv.innerHTML = htmlText;
});

let entryObj = {};
btnSave.addEventListener("click", (e) => {
  e.preventDefault();

  if (!markdownInput.value || !author.value || !title.value) {
    alert("Give a title, author and content of your entry before saving");
    author.focus();
    title.value = "";
    markdownInput.value = "";
    return;
  }

  entryObj.author = author.value;
  entryObj.title = title.value;
  entryObj.rawBody = markdownInput.value;
  entryObj.htmlBody = marked(markdownInput.value);
  const jsonData = JSON.stringify(entryObj);

  localStorage.setItem("newEntry", jsonData);
  alert("New article has been added successfully! You can now exit.");
});

btnExit.addEventListener("click", (e) => {
  e.preventDefault();
  location.href = "/entry.html";
});
