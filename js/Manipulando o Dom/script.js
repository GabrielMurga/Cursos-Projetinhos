const botao=document.querySelector('#calcular');
botao.addEventListener("click",(evento)=>{
    console.log(evento);
    botao.innerHTML="Ja fui Clicado"
    console.log("Eu fui clicado");
})