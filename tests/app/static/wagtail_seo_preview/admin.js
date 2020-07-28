document.addEventListener("DOMContentLoaded", function () {
  const initPreview = function (elem) {
    // const isTwitter = elem.classList.contains("twitter-preview-panel");
    // const isFacebook = elem.classList.contains("facebook-preview-panel");
    // const isGoogle = !isTwitter && !isFacebook;
    const titleInput = elem.querySelector(".meta-preview-title input");

    const descriptionInput =
      elem.querySelector(".meta-preview-description input") ||
      elem.querySelector(".meta-preview-description textarea");

    titleInput.addEventListener("keyup", function (e) {
      let value = e.target.value;
      if (!value) {
        value = document.querySelector("#id_title").value;
      }
      elem.querySelector(".meta-preview-box-title").innerHTML = value;
    });

    descriptionInput.addEventListener("keyup", function (e) {
      elem.querySelector(".meta-preview-box-description").innerHTML =
        e.target.value;
    });
  };

  document.querySelectorAll(".meta-preview-panel").forEach(function (elem) {
    initPreview(elem);
  });
});
