document.addEventListener('DOMContentLoaded', () => {
    // Crea el canvas si no existe
    let canvas = document.getElementById('confetti-canvas');
    if (!canvas) {
        canvas = document.createElement('canvas');
        canvas.id = 'confetti-canvas';
        document.body.appendChild(canvas);
    }

    const myConfetti = confetti.create(canvas, {
        resize: true,
        useWorker: true
    });

    const duration = 3 * 1000;
    const end = Date.now() + duration;

    (function frame() {
        myConfetti({
            particleCount: 4,
            angle: 60,
            spread: 70,
            origin: { x: 0 },
        });
        myConfetti({
            particleCount: 4,
            angle: 120,
            spread: 70,
            origin: { x: 1 },
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    })();
});
