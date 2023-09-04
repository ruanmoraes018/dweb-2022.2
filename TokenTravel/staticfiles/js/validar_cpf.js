function validar_cpf(cpf) {
    cpf = cpf.split('').filter(char => /\d/.test(char)).join('');
    if (cpf.length != 11) {return false;}
    if (cpf == cpf[0].repeat(11)) {return false;}
    soma = 0
    for (var i = 0; i < 9; i++) {soma += parseInt(cpf[i]) * (10 - i);}
    resto = (soma * 10) % 11
    if (resto == 10 || resto == parseInt(cpf[9])) {
    } else {return false;}
    soma = 0
    for (var i = 0; i < 10; i++) {soma += parseInt(cpf[i]) * (11 - i);}
    resto = (soma * 10) % 11
    if (resto == 10 || resto == parseInt(cpf[10])) {
    } else {return false;}
    cpf_formatado = cpf.slice(0, 3) + '.' + cpf.slice(3, 6) + '.' + cpf.slice(6, 9) + '-' + cpf.slice(9, 11);
    return cpf_formatado;}
function verificarCPF(event) {
    var cpf = document.getElementById("cpf").value;
    var cpf_validado = validar_cpf(cpf)
    if (!cpf_validado) {
        alert("CPF inválido!");
        event.preventDefault();
    } else {document.getElementById("cpf").value = cpf_validado;}}