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
  const baseAdminUrl = document.querySelector("a.logo").getAttribute('href');
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

  xhr.open("GET", baseAdminUrl + "get-img-rendition/" + id + "/");
  xhr.send();

  return val;
};

document.addEventListener("DOMContentLoaded", function () {
  const setupEvents = function (elem, field, type) {
    const titleMapping = {
      twitter: window.twitter_title_fields,
      facebook: window.facebook_title_fields,
      google: window.google_title_fields,
    };
    const descriptionMapping = {
      twitter: window.twitter_description_fields,
      facebook: window.facebook_description_fields,
      google: window.google_description_fields,
    };

    const titleFields = titleMapping[type].split(",");
    const descriptionFields = descriptionMapping[type].split(",");

    let fields = titleFields;
    if (field === "description") {
      fields = descriptionFields;
    }

    const handleChange = function () {
      let value;
      for (let i = 0; i < fields.length; i++) {
        const field = document.querySelector("#id_" + fields[i]);
        if (field && field.value) {
          value = field.value;
          break;
        }
      }
      elem.querySelector(".meta-preview-box-" + field).innerHTML = value || "";
    };

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
        const imageMapping = {
          twitter: window.twitter_image_fields,
          facebook: window.facebook_image_fields,
          google: window.google_image_fields,
        };
        const imageFields = imageMapping[type].split(",");

        let val;
        const previews = document.querySelectorAll(
          classMappingPreviewImage[type]
        );

        for (let field of imageFields) {
          val = document.querySelector("#id_" + field).value;
          if (val) {
            fetchImage(val, function (img) {
              for (let preview of previews) {
                preview.style =
                  "background-image: url(" +
                  img.src +
                  "); background-position: " +
                  img.focal.x +
                  " " +
                  img.focal.y;
              }
            });
            break;
          }
        }
        if (!val) {
          for (let preview of previews) {
            preview.style = "";
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
