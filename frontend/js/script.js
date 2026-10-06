const API_URL = "http://localhost:8030/livros";

const listaLivros = document.getElementById("listaLivros");
const formLivro = document.getElementById("formLivro");

async function carregarLivros() {

    const resposta = await fetch(API_URL);

    const livros = await resposta.json();

    listaLivros.innerHTML = "";

    livros.forEach(livro => {

        listaLivros.innerHTML += `
            <div class="livro">

                <div>
                    <strong>${livro.titulo}</strong>
                    <br>
                    ${livro.autor}
                </div>

                <div class="acoes">

                    <button
                        class="btn-excluir"
                        onclick="removerLivro(${livro.id})"
                    >
                        Excluir
                    </button>

                </div>

            </div>
        `;
    });
}

async function removerLivro(id) {

    await fetch(
        `${API_URL}/${id}`,
        {
            method: "DELETE"
        }
    );

    carregarLivros();
}

formLivro.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();

        const titulo =
            document.getElementById("titulo").value;

        const autor =
            document.getElementById("autor").value;


        const ano_publicacao =
            Number(document.getElementById("ano_publicacao").value);

        await fetch(
            API_URL,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    titulo,
                    autor,
                    ano_publicacao
                })
            }
        );

        formLivro.reset();

        carregarLivros();
    }
);

carregarLivros();