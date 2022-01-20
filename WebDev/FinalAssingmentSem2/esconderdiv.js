let home = document.querySelector('#home');
let cadastro = document.querySelector('#cadastro');
let aprovados = document.querySelector('#aprovados');
let reprovados = document.querySelector('#reprovados');

let home2 = document.querySelector('#home2');
let cadastro2 = document.querySelector('#cadastro2');
let aprovados2 = document.querySelector('#aprovados2');
let reprovados2 = document.querySelector('#reprovados2');

let divCadastro = document.querySelector('.cadastroAluno');
let divAprovados = document.querySelector('.aprovadoAluno')
let divReprovados = document.querySelector('.reprovadoAluno')

home.addEventListener('click', ()=>{
    divAprovados.style.display = 'none'
    divReprovados.style.display = 'none'
    divCadastro.style.display = 'none'
})

cadastro.addEventListener('click', ()=>{
    divAprovados.style.display = 'none'
    divReprovados.style.display = 'none'
    divCadastro.style.display = 'block'
})

aprovados.addEventListener('click', ()=>{
    divAprovados.style.display = 'block'
    divReprovados.style.display = 'none'
    divCadastro.style.display = 'none'
})

reprovados.addEventListener('click', ()=>{
    divAprovados.style.display = 'none'
    divReprovados.style.display = 'block'
    divCadastro.style.display = 'none'
})

home2.addEventListener('click', ()=>{
    divAprovados.style.display = 'none'
    divReprovados.style.display = 'none'
    divCadastro.style.display = 'none'
})

cadastro2.addEventListener('click', ()=>{
    divAprovados.style.display = 'none'
    divReprovados.style.display = 'none'
    divCadastro.style.display = 'block'
})

aprovados2.addEventListener('click', ()=>{
    divAprovados.style.display = 'block'
    divReprovados.style.display = 'none'
    divCadastro.style.display = 'none'
})

reprovados2.addEventListener('click', ()=>{
    divAprovados.style.display = 'none'
    divReprovados.style.display = 'block'
    divCadastro.style.display = 'none'
})