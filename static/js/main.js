const BotonesCancelar = document.querySelectorAll('.btnCancelar');
if (BotonesCancelar) {
    const btnArray = Array.from(BotonesCancelar);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            jsModal(btn.id);
        });
    });
}

async function jsModal(id) {
    $(".modal-title").html("Usuarios");
    $(".modal-header").addClass("bg-warning");
    $(".modal-body").html("¿Desea cancelar el usuario # <b>" + id + "?</b>");
    var myModal = new bootstrap.Modal(document.getElementById("VentanaModal"), {});
    myModal.show();
    $("#VentanaModal").find('.btn-Cancelar').attr('href', 'CancelarUsuario/'+id);
}