const input = document.getElementById("image");
const img = document.getElementById("detect");
const imgCont = document.getElementById("img-container");



function trackto() {
    const tracker = new tracking.ColorTracker(['magenta', 'cyan', 'yellow']);

    tracker.on('track', function (e) {
        e.data.forEach(rect => {
            window.plot(rect.x, rect.y, rect.width, rect.height, rect.color);
        });
    });

    tracking.track('#detect', tracker);

    window.plot = function (x, y, w, h, color) {
        let rect = document.createElement('div');
        imgCont.appendChild(rect);
        rect.classList.add('rect');
        rect.style.border = `2px solid ${color}`;
        rect.style.width = `${w}px`;
        rect.style.height = `${h}px`;
        rect.style.left = `${img.offsetLeft + x}px`;
        rect.style.top = `${img.offsetTop + y}px`;
    };

    function processUrl(input) {
        if (input.files && input.files[0]) {
            const reader = new FileReader();

            reader.onload = function (e) {
                img.setAttribute('src', e.target.result);
            }

            reader.readAsDataURL(input.files[0]);
        }
    }

    input.addEventListener('change', function () {
        processUrl(this);
    });
};

window.addEventListener("mouseout", trackto);

window.addEventListener('dbclick', function () {
    alert("reload the page!!");
});