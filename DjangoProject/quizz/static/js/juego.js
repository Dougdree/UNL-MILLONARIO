document.addEventListener('DOMContentLoaded', () => {
    const botones = document.querySelectorAll('.opcion');
    const form = document.querySelector('#form-respuesta');
    const temporizador = document.getElementById('temporizador');
    const barra = document.getElementById('barra');
    let tiempo = parseInt(temporizador.getAttribute('data-tiempo')) || 30;
    const tiempoInicial = tiempo;
    let seleccionado = false;

    function actualizarTemporizador() {
        let minutos = Math.floor(tiempo / 60);
        let segundos = tiempo % 60;

        temporizador.textContent =
            (minutos < 10 ? '0' : '') + minutos + ':' + (segundos < 10 ? '0' : '') + segundos;

        let porcentaje = (tiempo / tiempoInicial) * 100;
        barra.style.width = porcentaje + '%';

        if (tiempo > 0) {
            tiempo--;
            setTimeout(actualizarTemporizador, 1000);
        } else {
            temporizador.textContent = "⏰ ¡Tiempo agotado!";
            // Desactivar botones
            botones.forEach(btn => btn.disabled = true);

            // Enviar formulario sin respuesta seleccionada (se podría ajustar según tu lógica)
            setTimeout(() => {
                form.submit();
            }, 1000);
        }
    }

    actualizarTemporizador();

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

            // Desactiva todos los botones
            botones.forEach(btn => btn.disabled = true);

            // Crear input oculto para enviar el ID
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
