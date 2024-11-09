import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";

const markdownInput = document.getElementById("markdown");
const outputDiv = document.getElementById("output");
const title = document.getElementById("title");
const btnSave = document.querySelector(".btn-save");
const btnDelete = document.querySelector(".btn-delete");
const btnExit = document.querySelector(".btn-exit");
const author = document.getElementById("author");

document.addEventListener("DOMContentLoaded", (e) => {
  e.preventDefault();
  const localStorageData = localStorage.getItem("newEntry");
  if (localStorageData) {
    const jsonData = JSON.parse(localStorageData);
    const jsonDataAuthor = jsonData.author;
    const jsonDataTitle = jsonData.title;
    const jsonRawDataBody = jsonData.rawBody;
    author.value = jsonDataAuthor;
    title.value = jsonDataTitle;
    markdownInput.textContent = jsonRawDataBody;

    markdownInput.focus();
    return;
  }
  alert("You have no encyclopedia entry yet");
  window.history.back();
});
markdownInput.addEventListener("input", function (e) {
  if (title.value === "" || author.value === "") {
    alert("Give a title and author of your entry before the content");
    title.focus();
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
  alert("Article has been updated successfully! You can now exit.");
});

btnExit.addEventListener("click", (e) => {
  e.preventDefault();
  location.href = "/entry.html";
});

btnDelete.addEventListener("click", (e) => {
  e.preventDefault();

  let userInput;

  userInput = prompt("Do you want to delete the article 'yes' or 'no':");
  userInput = userInput ? userInput.toLowerCase() : "";

  if (userInput === "yes" || userInput === "no") {
    if (userInput === "yes") {
      markdownInput.textContent = "";
      outputDiv.value = "";
      title.value = "";
      author.value = "";
      localStorage.removeItem("newEntry");
      alert("Article had been deleted successfully!");
      location.reload();
    } else {
      alert("Deletion declined!");
    }
  } else {
    alert("Invalid response, deletion declined!");
  }
});
