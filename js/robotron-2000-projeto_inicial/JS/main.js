const controle= document.querySelectorAll(".controle-ajuste")
const braco=document.querySelector("#braco")
controle.forEach((elemento)=>{
    elemento.addEventListener("click",((evento)=>{
        manipulaDados(evento.target.textContent)
    }))
})
 function manipulaDados(operacao){
    if(operacao==="-"){
        braco.value=parseInt(braco.value)-1
    }else{
        braco.value=parseInt(braco.value)+1

    }
}