function validarSenha() {
    var senha = document.getElementById("cadastro-senha").value;
    var confirmarSenha = document.getElementById("cadastro-confirmar-senha").value;
    if (senha != confirmarSenha) {
        alert("As senhas não coincidem!");
        return false;
    }
        return true;
}

var formulario = document.getElementById('cadastro-formulario');
var nome = document.getElementById('cadastro-nome-completo');
var cpf = document.getElementById('cadastro-cpf');
var telefone = document.getElementById('cadastro-telefone');
var email = document.getElementById('cadastro-email');
var endereco = document.getElementById('cadastro-logradouro');
var nº = document.getElementById('cadastro-numero-residencia');
var bairro = document.getElementById('cadastro-bairro');
var estado = document.getElementById('cadastro-estado');
var cidade = document.getElementById('cadastro-cidade');
var cep = document.getElementById('cadastro-cep');
var senha = document.getElementById('cadastro-senha');
var confirmarSenha = document.getElementById('cadastro-confirmar-senha');

formulario.addEventListener('submit', function(event) {
    if (!nome.value || !cpf.value || !telefone.value || !email.value || !endereco.value || !nº.value || !bairro.value || !estado.value || !cidade.value || !cep.value || !senha.value || !confirmarSenha.value) {
        event.preventDefault();
        alert('Por favor, preencha todos os campos obrigatórios.');
    }
});