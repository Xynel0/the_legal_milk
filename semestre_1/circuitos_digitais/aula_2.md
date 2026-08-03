## Capítulo 2

<div class="definicoes" id="1">
  <h3 id="Sistemas numéricos">
    Sistemas numéricos
  </h3>

&emsp; **Sistemas numéricos** são formas padronizadas de representar quantidades utilizando uma base e um conjunto de símbolos. Em sistemas posicionais, o valor de cada algarismo depende da sua posição e da base utilizada.

- **Decimal:** sistema posicional de base 10 usado no cotidiano. Os algarismos utilizados são de 0 a 9 da representação indo-arábica.

- **Binário:** sistema posicional de base 2 compreendido pelo computador. Os algarismos utilizados são 0 e 1, que representam falso e verdadeiro, respectivamente, definidos individualmente por uma faixa de tensão específica.

- **Hexadecimal:** sistema posicional de base 16 usado como compactação de códigos binários; ou seja, uma codificação taquigráfica. Os algarismos utilizados são de 0 a 9 da representação indo-arábica e de A a F do alfabeto latino, onde A representa o número decimal 10, B representa o número decimal 11, F representa o número decimal 15, etc. Um dígito hexadecimal representa 4 bits binários.

- **Octal:** sistema posicional de base 8 que foi utilizado como alternativa compacta em relação ao binário, tendo sido posteriormente substituído. Um dígito octal pode representar 3 bits binários.

</div>

<div class="definicoes" id="2">
  <h3 id="Representações de código">
    Representações de código
  </h3>

&emsp; **Representações de código** são formas de codificar informações para facilitar seu armazenamento, transmissão ou processamento, sem alterar o valor representado.

- **Binary-Coded Decimal (BCD):** cada dígito de um número decimal é convertido em seu equivalente binário de 4 bits. Apesar de consumir mais bits para representar um número em relação ao binário puro, é mais fácil de converter, já que são utilizados apenas os valores binários correspondentes aos algarismos decimais de 0 a 9.

- **Código de Gray:** utilizado para minimizar erros. Em sistemas digitais, quando um número binário passa de 3 para 4, todos os bits mudam de valor, e isso pode gerar erros no processo. Para corrigir esse problema, o código de Gray permite que apenas um bit seja alterado por vez, utilizando os mesmos dígitos do sistema binário.

</div>

---

Para a conversão de binário para Gray:

> Seja o número binário $B = 100$ e o código Gray $= x_2x_1x_0$.
>
> 1. Repete-se o *most significant bit* (MSB) do binário como o MSB do código Gray.  
>    $G = 1x_1x_0$
>
> 2. Compara-se o MSB binário com o seu sucessor utilizando a operação lógica **ou exclusivo (XOR)**. Se $b_2=b_1$, então $x_1=0$; caso contrário, $x_1=1$.  
>    $G = 11x_0$
>
> 3. Compara-se o dígito binário equivalente ao último dígito Gray determinado com o seu sucessor binário, seguindo o mesmo processo XOR do passo anterior.  
>    $G = 110$

&emsp; A conversão de Gray para binário ocorre de forma semelhante. Repete-se o MSB em Gray e, em seguida, compara-se o dígito $G_n$ com o dígito $B_{n+1}$, realizando a operação lógica **ou exclusivo (XOR)** entre eles.

---

### Alguns termos:

<div style="border:1px solid gray; padding:12px; border-radius:8px;" class="definicoes" id="3">

- **Byte:** conjunto de 8 bits. A maioria dos microcomputadores armazena dados binários e informações em grupos de 8 bits.
- **Nibble:** conjunto de 4 bits.
- **Word:** quantidade de bits tratados como uma unidade de informação. Se uma transmissão envia 4 bytes por vez, então sua *word* tem tamanho de 32 bits.
- **Código alfanumérico ASCII:** além de números, representa também caracteres não numéricos, como letras do alfabeto e outros símbolos, além de funções como **RETURN** e **LINE FEED**. Possui 7 bits, totalizando 128 representações possíveis.

</div>

---

<div class="definicioes" id="4">
  <h3 id="Método de Paridade">
    Método de Paridade
  </h3>
  
&emsp; Utilizado para detectar erros na transmissão quando a probabilidade de ocorrência de apenas um bit incorreto é pequena, porém possível. No caso de haver erro em dois ou mais bits, o método de paridade é ineficaz.


- **Paridade Par:** adiciona-se um bit à esquerda, de modo que a quantidade de dígitos 1 do código seja um número natural par.
- **Paridade Ímpar:** adiciona-se um bit à esquerda, de modo que a quantidade de dígitos 1 do código seja um número natural ímpar.

</div>
