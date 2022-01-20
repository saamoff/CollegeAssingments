let salvarbtn = document.querySelector('#salvarCadastro');

salvarbtn.addEventListener('click', mostrarData);

var linha = 1;

var lista = 0;

function mostrarData(){
    var nome = document.getElementById('nomeCadastro').value;
    var nota = document.getElementById('notaCadastro').value;

    if(!nome || !nota) {
        alert("Por favor preencha todos os campos.");
        return;
    }

    if(nota > 4){

        var aprovados = document.querySelector('.tabelaAprovados')

        var novaLinha = document.createElement('tr');
        var coluna1 = document.createElement('td');
        var coluna2 = document.createElement('td');
        var coluna3 = document.createElement('td');

        novaLinha.appendChild(coluna1)
        novaLinha.appendChild(coluna2)
        novaLinha.appendChild(coluna3)

        aprovados.appendChild(novaLinha)

        coluna1.innerHTML = nome
        coluna2.innerHTML = nota
        coluna3.innerHTML = "APROVADO"
    }else{
        var aprovados = document.querySelector('.tabelaReprovados')

        var novaLinha = document.createElement('tr');
        var coluna1 = document.createElement('td');
        var coluna2 = document.createElement('td');
        var coluna3 = document.createElement('td');

        novaLinha.appendChild(coluna1)
        novaLinha.appendChild(coluna2)
        novaLinha.appendChild(coluna3)

        aprovados.appendChild(novaLinha)

        coluna1.innerHTML = nome
        coluna2.innerHTML = nota
        coluna3.innerHTML = "REPROVADO"
    }

    lista++;
    if(lista != 0){
        document.querySelector('.painelAtualizado h1').innerHTML = "Painel: " + lista + " aluno(s) cadastrados."
    }
}
