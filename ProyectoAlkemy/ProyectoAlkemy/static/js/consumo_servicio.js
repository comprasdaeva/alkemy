let serviciosAPI= null;
let botonseleccionServicio=document.getElementById("id_boton_servicio");
async function listadoDeServicios(){
  try{
     if(serviciosAPI==null){
        let respuesta= await fetch('http://127.0.0.1:8000/api/servicios/')
        serviciosAPI= await respuesta.json();
     }        
     return serviciosAPI
  }
  catch(error){
    console.log("Ocurrio un error al querer consumir la api")
  } 
}
async function servicioPorId(id){
  let listado = await listadoDeServicios();
  let servicio = listado.find(servicio=> servicio.id===Number(id));

  return servicio;
}
botonseleccionServicio.addEventListener("click",async ()=>{
    let radioServicio=document.getElementsByName("opcion")    
    let seleccionado
    for(let i=0;i<radioServicio.length;i++){
        if(radioServicio[i].checked){
            seleccionado=radioServicio[i].value;
            break
        }
    }
    console.log(seleccionado)
    await modificarInputYBoton(seleccionado)
})
async function modificarInputYBoton(servicioSeleccionado){
    let servicio = await servicioPorId(servicioSeleccionado)
    modificarInputPrecio(servicio.precio)
    modificarBotonServicio(servicio.nombre)
} 

const modificarInputPrecio=valor=>{
    let inputPrecio=document.getElementById("id_precio")
    inputPrecio.value=valor
}

const modificarBotonServicio=valor=>{
  let botonServicio=document.getElementById("id_span_servicio_boton")  
  botonServicio.textContent=valor
}

