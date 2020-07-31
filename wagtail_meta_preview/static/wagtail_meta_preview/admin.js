// We need to be able to track hidden inputs changing, hence the MutationObserver
const MutationObserver =
  window.MutationObserver || window.WebKitMutationObserver;

var ChangeTracker = function (elem) {
  var observer = new MutationObserver(function (mutations) {
    if (mutations[0].attributeName === "value") {
      elem.dispatchEvent(new Event("change"));
    }
  });
  observer.observe(elem, {
    attributes: true,
  });
};

// TODO: Don't hardcode /admin/
const fetchImage = async function (id) {
  const resp = await fetch("/admin/get-img-rendition/" + id + "/");
  const json = await resp.json();
  return json;
};

document.addEventListener("DOMContentLoaded", function () {
  const setupEvents = function (elem, type) {
    const titleFields = window.twitter_title_fields.split(",");
    const descriptionFields = window.twitter_description_fields.split(",");
    const inputField = elem.querySelector(".meta-preview-" + type + " input");
    const fields = type === "title" ? titleFields : descriptionFields;

    const handleChange = function () {
      let value = inputField && inputField.value;
      if (!value) {
        for (let i = 0; i < fields.length; i++) {
          let otherField = document.querySelector("#id_" + fields[i]);
          if (otherField && otherField.value) {
            value = otherField.value;
            break;
          }
        }
      }
      elem.querySelector(".meta-preview-box-" + type).innerHTML = value;
    };

    inputField && inputField.addEventListener("keyup", handleChange);
    for (let i = 0; i < fields.length; i++) {
      document
        .querySelector("#id_" + fields[i])
        .addEventListener("keyup", handleChange);
    }
  };

  const setupImageEvents = function (elem) {
    const choosers = document.querySelectorAll(".image-chooser + input");
    for (let chooser of choosers) {
      ChangeTracker(chooser);
      chooser.addEventListener("change", async function () {
        const twitterImage = elem.querySelector("input[type=hidden]");
        const imageFields = window.twitter_image_fields.split(",");

        if (!twitterImage.value) {
          for (let field of imageFields) {
            const val = document.querySelector("#id_" + field).value;
            if (val) {
              const img = await fetchImage(val);
              document.querySelector(".meta-twitter-preview-image").style =
                `background-image: url('${img.src}'); background-position: ${img.focal.x} ${img.focal.y}`;
              break;
            }
          }
        } else {
          document.querySelector(".meta-twitter-preview-image").style =
            'background-image: url("' +
            (await fetchImage(twitterImage.value)) +
            '")';
        }
      });
    }
  };

  const initPreview = function (elem) {
    // const isTwitter = elem.classList.contains("twitter-preview-panel");
    // const isFacebook = elem.classList.contains("facebook-preview-panel");
    // const isGoogle = !isTwitter && !isFacebook;

    setupEvents(elem, "title");
    setupEvents(elem, "description");
    setupImageEvents(elem);
  };

  document.querySelectorAll(".meta-preview-panel").forEach(function (elem) {
    initPreview(elem);
  });
});
