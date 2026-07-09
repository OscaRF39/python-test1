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

function jsPrueba(){
    var urlHref = "../../ajax";
    $.ajax({
        url:urlHref,
        dataType:"json",
        cache:false,
        success: function(cJSON){
            alert(cJSON.Param1);
            $("#Prueba").html(cJSON.Param1);
        },
        error: function (obj,tipeError,Error){
            alert("Error "+Error);
        }
    });
}

const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
});

async function jsColocarImagen() {
    const file = document.querySelector('#Imagen').files[0];
    let CajaImagen = document.getElementById("ImagenUsuario");
    let Imagen64 = await toBase64(file);
    CajaImagen.src = Imagen64;
}