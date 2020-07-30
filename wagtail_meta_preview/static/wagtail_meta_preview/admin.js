document.addEventListener("DOMContentLoaded", function () {
  const setupEvents = function (elem, type) {
    const titleFields = window.twitter_title_fields.split(",");
    const descriptionFields = window.twitter_description_fields.split(",");
    const inputField = elem.querySelector(".meta-preview-" + type + " input");
    const fields = type === "title" ? titleFields : descriptionFields;

    const handleChange = function () {
      let value = inputField.value;
      if (!value) {
        for (let i = 0; i < fields.length; i++) {
          let otherValue = document.querySelector("#id_" + fields[i]).value;
          if (otherValue) {
            value = otherValue;
            break;
          }
        }
      }
      elem.querySelector(".meta-preview-box-" + type).innerHTML = value;
    };

    inputField.addEventListener("keyup", handleChange);
    for (let i = 0; i < fields.length; i++) {
      document
        .querySelector("#id_" + fields[i])
        .addEventListener("keyup", handleChange);
    }
  };

  const initPreview = function (elem) {
    // const isTwitter = elem.classList.contains("twitter-preview-panel");
    // const isFacebook = elem.classList.contains("facebook-preview-panel");
    // const isGoogle = !isTwitter && !isFacebook;

    setupEvents(elem, "title");
    setupEvents(elem, "description");
  };

  document.querySelectorAll(".meta-preview-panel").forEach(function (elem) {
    initPreview(elem);
  });
});
