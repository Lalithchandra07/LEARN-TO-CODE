window.addEventListener("scroll", function() {
    const wallpaper = document.getElementById("wallpaper");
    if (window.scrollY > 50) { // Adjust the scroll value to control when wallpaper disappears
        wallpaper.style.opacity = 0;
    } else {
        wallpaper.style.opacity = 1;
    }
});
