var alertaCPFExibido = false;

function validarCPF() {
  var cpf = document.getElementById('cpf').value;
  cpf = cpf.replace(/\D/g, ''); // Remove caracteres não numéricos

  if (cpf.length === 11 && verificaSomaCPF(cpf) && !alertaCPFExibido) {
    alertaCPFExibido = false;
  } else if (cpf.length === 0 && !alertaCPFExibido) {
    alert('Insira o CPF!');
    alertaCPFExibido = true;
  } else if (cpf.length < 11 || !verificaSomaCPF(cpf)) {
    alert('CPF inválido!');
    alertaCPFExibido = true; // Redefinir a variável se o CPF for editado
  }
}

function verificaSomaCPF(cpf) {
  cpf = cpf.replace(/\D/g, ''); // Remova caracteres não numéricos novamente

  var soma = 0;
  for (var i = 0; i < 9; i++) {
    soma += parseInt(cpf.charAt(i)) * (10 - i);
  }
  var digitoVerificador1 = soma % 11 < 2 ? 0 : 11 - (soma % 11);

  soma = 0;
  for (var i = 0; i < 10; i++) {
    soma += parseInt(cpf.charAt(i)) * (11 - i);
  }
  var digitoVerificador2 = soma % 11 < 2 ? 0 : 11 - (soma % 11);

  return digitoVerificador1 === parseInt(cpf.charAt(9)) &&
         digitoVerificador2 === parseInt(cpf.charAt(10));
}
