function validar_cpf(cpf) {
  // Remover caracteres não numéricos
    cpf = cpf.split('').filter(char => /\d/.test(char)).join('');

    // Verificar se CPF tem 11 dígitos
    if (cpf.length != 11) {
        return false;
    }

    // Verificar se CPF tem todos os dígitos iguais
    if (cpf == cpf[0].repeat(11)) {
        return false;
    }

    // Verificar primeiro dígito verificador
    soma = 0
    for (var i = 0; i < 9; i++) {
        soma += parseInt(cpf[i]) * (10 - i);
    }
    resto = (soma * 10) % 11
    if (resto == 10 || resto == parseInt(cpf[9])) {
        // pass
    } else {
        return false;
    }

    // Verificar segundo dígito verificador
    soma = 0
    for (var i = 0; i < 10; i++) {
        soma += parseInt(cpf[i]) * (11 - i);
    }
    resto = (soma * 10) % 11
    if (resto == 10 || resto == parseInt(cpf[10])) {
        // pass
    } else {
        return false;
    }

    // Formatar CPF
    cpf_formatado = cpf.slice(0, 3) + '.' + cpf.slice(3, 6) + '.' + cpf.slice(6, 9) + '-' + cpf.slice(9, 11);

    // CPF válido
    return cpf_formatado;
}


function verificarCPF(event) {
    var cpf = document.getElementById("cpf").value;
    var cpf_validado = validar_cpf(cpf)
    if (!cpf_validado) {
        alert("CPF inválido!");
        event.preventDefault(); // impede que o formulário seja enviado
    } else {
        document.getElementById("cpf").value = cpf_validado;
    }
}