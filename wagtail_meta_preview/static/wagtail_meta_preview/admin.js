const classMappingPreviewImage = {
  twitter: ".meta-twitter-preview-image",
  facebook: ".meta-facebook-preview-image",
  google: ".meta-google-preview-image",
};

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

const fetchImage = function (id, cb) {
  const xhr = new XMLHttpRequest();
  let val;
  xhr.onreadystatechange = function () {
    // Only run if the request is complete
    if (xhr.readyState !== 4) return;

    // Process our return data
    if (xhr.status >= 200 && xhr.status < 300) {
      // What do when the request is successful
      cb(JSON.parse(xhr.responseText));
    }
  };

  // TODO: Don't hardcode /admin/
  xhr.open("GET", "/admin/get-img-rendition/" + id + "/");
  xhr.send();

  return val;
};

document.addEventListener("DOMContentLoaded", function () {
  const setupEvents = function (elem, field, type) {
    const titleFields = window[type + "_title_fields"].split(",");
    const descriptionFields = window[type + "_description_fields"].split(",");
    const inputField = elem.querySelector(".meta-preview-" + field + " input");
    const fields = field === "title" ? titleFields : descriptionFields;

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
      elem.querySelector(".meta-preview-box-" + field).innerHTML = value;
    };

    inputField && inputField.addEventListener("keyup", handleChange);
    for (let i = 0; i < fields.length; i++) {
      document
        .querySelector("#id_" + fields[i])
        .addEventListener("keyup", handleChange);
    }
  };

  const setupImageEvents = function (elem, type) {
    const choosers = document.querySelectorAll(".image-chooser + input");
    for (let chooser of choosers) {
      ChangeTracker(chooser);
      chooser.addEventListener("change", function (e) {
        const imageInput = elem.querySelector("input[type=hidden]");
        const imageFields = window[type + "_image_fields"].split(",");

        if (imageInput.id === e.target.id) {
          fetchImage(imageInput.value, function (img) {
            document.querySelector(classMappingPreviewImage[type]).style =
              'background-image: url("' + img.src + '")';
          });
          return;
        }

        if (!imageInput.value) {
          for (let field of imageFields) {
            const val = document.querySelector("#id_" + field).value;
            if (val) {
              fetchImage(imageInput.value, function (img) {
                document.querySelector(
                    classMappingPreviewImage[type]
                ).style =
                  "background-image: url(" +
                  img.src +
                  "); background-position: " +
                  img.focal.x +
                  " " +
                  img.focal.y;
              });
              break;
            }
          }
        }
      });
    }
  };

  const initPreview = function (elem) {
    const isTwitter = elem.classList.contains("twitter-preview-panel");
    const isFacebook = elem.classList.contains("facebook-preview-panel");
    const isGoogle = !isTwitter && !isFacebook;

    let type;
    if (isTwitter) {
      type = "twitter";
    } else if (isFacebook) {
      type = "facebook";
    } else if (isGoogle) {
      type = "google";
    }

    setupEvents(elem, "title", type);
    setupEvents(elem, "description", type);
    if (!isGoogle) {
      setupImageEvents(elem, type);
    }
  };

  document.querySelectorAll(".meta-preview-panel").forEach(function (elem) {
    initPreview(elem);
  });
});
