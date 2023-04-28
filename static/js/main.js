const BotonesCancelar = document.querySelectorAll('.btnCancelar');
if(BotonesCancelar){
    const btnArray = Array.from(BotonesCancelar);
    //alert(btnArray.length);
    btnArray.forEach((btn) => {
        //alert(btn.id);
        btn.addEventListener('click', (e) => {            
            var TextoModal = "";
            if(!jsModal(btn.id)){
                e.preventDefault();
            }else{
                alert("true");
            }
        });
    });
}

function jsModal(id){
    $(".modal-title").html("¿Cancelar el usuario # <b>"+id+"?</b>");
    $(".modal-header").addClass("bg-warning");
    var myModal = new bootstrap.Modal(document.getElementById("VentanaModal"), {});
    myModal.show(function(e){
        alert(e);
        return true;
    });
}