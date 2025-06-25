document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card-prueba');

    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.boxShadow = '0 0 20px #cc00ff';
        });

        card.addEventListener('mouseleave', () => {
            card.style.boxShadow = 'none';
        });

        card.addEventListener('click', () => {
            const pruebaId = card.dataset.id;
            window.location.href = `/iniciar/${pruebaId}/`;
        });
    });
});
