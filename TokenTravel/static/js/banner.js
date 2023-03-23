function resizeBanner() {
    var banner = document.getElementById('banner');
    var windowHeight = window.innerHeight;
    banner.style.height = windowHeight + 'px';
}
window.onload = function() {
    resizeBanner();
};
window.onresize = function() {
    resizeBanner();
};