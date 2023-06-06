
function changeImage() {
    let img = document.getElementById("myImage");
    let currentImage = img.getAttribute("src");
    let imageList = [
      "img/image1.jpg",
      "img/image2.jpg",
      "img/image3.jpg"
    ];
  
    let currentIndex = imageList.indexOf(currentImage);
    let nextIndex = (currentIndex + 1) % imageList.length;
    let nextImage = imageList[nextIndex];
  
    img.src = nextImage;
  }
  setInterval(changeImage, 3000);
  function showImage() {
    let overlay = document.getElementById("overlay");
    let overlayImage = document.getElementById("overlayImg");
    let thumbnailImage = document.getElementById("myImage");
    let flag = document.querySelectorAll(".flag-icon");
    overlay.style.display = "flex";
    flag.forEach(function(icon) {
        icon.classList.add("fade");
      });
    overlayImage.src = thumbnailImage.src;
  }
  
  function hideImage() {
    let overlay = document.getElementById("overlay");
    let flag = document.querySelectorAll(".flag-icon");
    overlay.style.display = "none";
    flag.forEach(function(icon) {
        icon.classList.remove("fade");
      });
  }

  function savePageAsPDF() {
    const originalMediaType = window.matchMedia('screen').media;
    window.matchMedia('screen').media = 'print';
    window.print();
    window.matchMedia('screen').media = originalMediaType;
  }

    