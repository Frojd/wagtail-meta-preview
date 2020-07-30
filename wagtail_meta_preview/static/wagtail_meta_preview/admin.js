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

// Just pass an element to the function to start tracking

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

  const setupImageEvents = function (elem) {
    // const clearers = document.querySelectorAll(".image-chooser .action-clear");
    // for (let clearer of clearers) {
    //   clearer.addEventListener("click", function (e) {
    //     const currentId =
    //       e.target.parentElement.parentElement.parentElement.parentElement.id;
    //     // const img = findClosestDefaultImage()
    //     // changeImage(img)
    //   });
    // }

    const choosers = document.querySelectorAll(".image-chooser + input");
    for (let chooser of choosers) {
      ChangeTracker(chooser);
      chooser.addEventListener("change", function (e) {
        // TODO: This should ideally fetch the image via API to get the correct rendition.
        const twitterImage = elem.querySelector("input[type=hidden]");
        const imageFields = window.twitter_image_fields.split(",");

        if (!twitterImage.value) {
          for (let field of imageFields) {
            const val = document.querySelector("#id_" + field).value;
            if (val) {
              const img = document.querySelector(
                "#id_" + field + "-chooser .preview-image img"
              ).src;
              document.querySelector(".meta-twitter-preview-image").style =
                'background-image: url("' + img + '")';
              break;
            }
          }
        } else {
          document.querySelector(".meta-twitter-preview-image").style =
            'background-image: url("' +
            elem.querySelector(".preview-image img").src +
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
