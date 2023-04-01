
# Algorithms

Algorithms é um projeto que aborda sobre algoritmos e suas complexidades, com o objetivo de resolver situações que não possui uma otimização de tempo. 
Foi desenvolvido utilizando a linguagem de programação `Python`.

## Rodando localmente

<details>
    <summary>Clique aqui para expandir</summary>
    <br>

- Clone o projeto

```bash
  git clone git@github.com:Joaogustavo789/Algorithms.git
```

- Entre no diretório do projeto

```bash
  cd Algorithms
```

- Crie o Ambiente Virtual

```bash
  python3 -m venv .venv
```
    
- Ative o Ambiente Virtual
    
```bash
  source .venv/bin/activate
```

- Instale as dependências dentro do Ambiente Virtual

```bash
  python3 -m pip install -r dev-requirements.txt
```

##### OBSERVAÇÃO

- Para sair do Ambiente Virtual, basta rodar o comando `deactivate`.
    
</details>

## Rodando os testes

<details>
  <summary>Clique aqui para expandir</summary>
  <br>

- Para rodar os testes, rode o seguinte comando dentro do Ambiente Virtual

```bash
  python3 -m pytest
```

</details>

## Stack utilizada

<table width="320px" align="center">
  <tbody>
    <tr valign="top">
      <td width="80px" align="center">
        <span><strong>Python</strong></span>
        <img height="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
      </td>
      <td width="80px" align="center">
        <span><strong>Pytest</strong></span>
        <img height="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" />
      </td>
    </tr>
  </tbody>
</table>

## Funcionalidades

- Busca Linear (Algoritmo de busca)
- Merge Sort (Algoritmo de ordenação)
- Iteratividade
- Recursividade
- Teste

## Aprendizados

Nesse projeto, eu aprendi sobre algoritmos, incluindo o entendimento de suas complexidades e notações, tais como `O(1)`, `O(n)`, `O(log n)`, `O(n^2)`, 
`O(n^3)` e `O(n!)`. Além disso, eu fui capaz de definir e entender melhor os conceitos de `melhor caso`, `caso médio` e `pior caso` em relação à ordem de 
complexidade. Aprendi a encontrar a quantidade de estudantes que estavam estudando em um horário específico utilizando a `Busca Linear`, na qual irá 
percorrer item por item. Aprendi a identificar palíndromos usando algoritmos tanto de `Recursividade` quanto de `Iteratividade`. Aprendi a  utilizar o 
algoritmo de ordenação `Merge Sort` para identificar anagramas, o qual se baseia na estratégia de dividir e conquistar. Aprendi a encontrar numéros 
repetidos em uma lista também utilizando a `Busca Linear`, porém foi necessário ordenar essa lista para depois percorrer item por item. E por fim, 
implementei um teste em uma função de criptografia de  mensagem para garantir que ela retorne a resposta esperada quando chamada com os devidos 
parâmetros.

## Documentação

- [Python](https://www.python.org/)
- [Pytest](https://docs.pytest.org/)

## Feedback

Se você tiver algum feedback, por favor nos deixe saber por meio de jgustavomendonca@gmail.com
