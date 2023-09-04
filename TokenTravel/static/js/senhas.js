function validarSenha() {
    var password = document.getElementById("password").value;
    var confirmarSenha = document.getElementById("confirmar_senha").value;
    if (password != confirmarSenha) {
        alert("As senhas não coincidem!");
        return false;}
        return true;}
var formulario = document.getElementById('cadastro-formulario');
var nome = document.getElementById('nome_completo');
var cpf = document.getElementById('cpf');
var telefone = document.getElementById('telefone');
var email = document.getElementById('email');
var endereco = document.getElementById('logradouro');
var nº = document.getElementById('numero_residencia');
var bairro = document.getElementById('bairro');
var estado = document.getElementById('estado');
var cidade = document.getElementById('cidade');
var cep = document.getElementById('cep');
var password = document.getElementById('password');
var confirmarSenha = document.getElementById('confirmar_senha');
formulario.addEventListener('submit', function(event) {
    if (!nome.value || !cpf.value || !telefone.value || !email.value || !endereco.value || !nº.value || !bairro.value || !estado.value || !cidade.value || !cep.value || !password.value || !confirmarSenha.value) {
        event.preventDefault();
        alert('Por favor, preencha todos os campos obrigatórios.');}});