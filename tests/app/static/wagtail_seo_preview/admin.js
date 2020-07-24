document.addEventListener("DOMContentLoaded", function () {
  const initPreview = function (elem) {
    // const isTwitter = elem.classList.contains("twitter-preview-panel");
    // const isFacebook = elem.classList.contains("facebook-preview-panel");
    // const isGoogle = !isTwitter && !isFacebook;
    const titleInput = elem.querySelector(".seo-preview-title input");
    elem.querySelector(".seo-preview-box-title").innerHTML = titleInput.value;

    const descriptionInput =
      elem.querySelector(".seo-preview-description input") ||
      elem.querySelector(".seo-preview-description textarea");
    elem.querySelector(".seo-preview-box-description").innerHTML =
      descriptionInput.value;

    titleInput.addEventListener("keyup", function (e) {
      elem.querySelector(".seo-preview-box-title").innerHTML = e.target.value;
    });

    descriptionInput.addEventListener("keyup", function (e) {
      elem.querySelector(".seo-preview-box-description").innerHTML =
        e.target.value;
    });
  };

  document.querySelectorAll(".seo-preview-panel").forEach(function (elem) {
    initPreview(elem);
  });
});
