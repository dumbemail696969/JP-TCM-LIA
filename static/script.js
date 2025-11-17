// static/script.js
function perguntar() {
    const cep = document.getElementById("cep").value;
    const resultado = document.getElementById("resultado");
    fetch(`https://viacep.com.br/ws/${cep}/json/`)
      .then(response => response.json())
      .then(data => {
        if (data.erro) {
          resultado.innerHTML = "CEP não encontrado.";
        } else {
          resultado.innerHTML = `
            <p><strong>Rua:</strong> ${data.logradouro}</p>
            <p><strong>Bairro:</strong> ${data.bairro}</p>
            <p><strong>Cidade:</strong> ${data.localidade} - ${data.uf}</p>
          `;
        }
      })
      .catch(error => {
        resultado.innerHTML = "Erro ao buscar o CEP.";
        console.error(error);
      });
  }
  