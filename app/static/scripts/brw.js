$(document).ready(()=>{
    var Id_Seleccionado = 0;
    var obj_seleccionado;

    function limpiaSeleccion() {
        if (Id_Seleccionado > 0) {
            obj_seleccionado.children().eq(0).text("*")
            Id_Seleccionado = 0
            obj_seleccionado = undefined
        }
    }


    function limpiaForm(){
        for (var i = 0; i < $("#formDatos").children().length; i++) {
            $("#formDatos").children().eq(i).children().eq(1).val("")
        }
    }

    $("#dataGrid tbody tr").click((e) => {
        var seleccion = $(e.currentTarget);
        console.log(seleccion.children().eq(1).text(), seleccion.children().eq(0).text())
        var id = seleccion.children().eq(1).text()
        if (Id_Seleccionado == 0) {
            seleccion.children().eq(0).text("!")
            Id_Seleccionado = seleccion.children().eq(1).text()
            obj_seleccionado = seleccion
        } else {
            if (id == Id_Seleccionado) {
                limpiaSeleccion()
            } else {
                obj_seleccionado.children().eq(0).text("*")
                seleccion.children().eq(0).text("!")
                Id_Seleccionado = seleccion.children().eq(1).text()
                obj_seleccionado = seleccion
            }
        }
    })

    $("#btnAgregar").click(() =>{
        limpiaSeleccion();
        limpiaForm();
    })

    $("#btnGuardar").click(() =>{
        //TODO validate??
        var datos = {}
        if (Id_Seleccionado > 0) {
            datos[obj_seleccionado.children().eq(1).attr("class")] = Id_Seleccionado
            // console.log(obj_seleccionado.children().eq(1).attr("class"));
        }

        for (var i = 0; i < $("#formDatos").children().length; i++) {
            datos[$("#formDatos").children().eq(i).children().eq(1).attr("name")] = $("#formDatos").children().eq(i).children().eq(1).val()
        }

        console.log(datos);
        $.ajax({
            type: "POST",
            contentType: 'application/json; charset=utf-8',
            url: location.pathname.replace("/app/", "")+'/guardar',
            data: JSON.stringify(datos),
            success: (result) => {
                console.log(result);
                limpiaForm();
                limpiaSeleccion();
                location.reload();
            },
            error: (d, f, g) => {
                console.error(d, f, g);
            }
        })
    })

    $("#btnCambiar").click(()=>{
        if (Id_Seleccionado > 0) {
            datos = { id: Id_Seleccionado}
            $.ajax({
                type: "POST",
                contentType: 'application/json; charset=utf-8',
                url: location.pathname.replace("/app/", "")+'/seleccionar',
                data: JSON.stringify(datos),
                success: (result) => {
                    console.log(result);
                    var Datos = result.data

                    for (var i = 0; i < $("#formDatos").children().length; i++) {
                        var obj = $("#formDatos").children().eq(i).children().eq(1)
                        obj.val(Datos[obj.attr("name")])
                        console.log(Datos[obj.attr("name")]);
                    }
                },
                error: (d, f, g) => {
                    console.error(d, f, g);
                }
            })
        }
    })

    $("#btnBorrar").click(() => {
        if (Id_Seleccionado > 0) {
            datos = { id: Id_Seleccionado}
            $.ajax({
                type: "POST",
                contentType: 'application/json; charset=utf-8',
                url: location.pathname.replace("/app/", "")+'/borrar',
                data: JSON.stringify(datos),
                success: (result) => {
                    console.log(result);
                    limpiaForm();
                    limpiaSeleccion();
                    location.reload();
                },
                error: (d, f, g) => {
                    console.error(d, f, g);
                }
            })
        }
    })
})
