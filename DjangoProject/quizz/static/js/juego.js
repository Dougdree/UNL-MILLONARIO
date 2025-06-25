document.addEventListener('DOMContentLoaded', () => {
    const botones = document.querySelectorAll('.opcion');
    const form = document.querySelector('#form-respuesta');
    let seleccionado = false;

    botones.forEach(boton => {
        boton.addEventListener('click', () => {
            if (seleccionado) return;
            seleccionado = true;

            const esCorrecta = boton.dataset.correcta === 'True';

            if (esCorrecta) {
                boton.classList.add('correcta');
            } else {
                boton.classList.add('incorrecta');
            }

            // Desactiva todos los botones para evitar múltiples clics
            botones.forEach(btn => btn.disabled = true);

            // Crear input oculto para enviar el ID de la respuesta seleccionada
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'respuesta_id';
            input.value = boton.dataset.id;
            form.appendChild(input);

            // Espera 1 segundo antes de enviar
            setTimeout(() => {
                form.submit();
            }, 1000);
        });
    });
});
