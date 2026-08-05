# Capítulo 2

<div class="definicoes" id="1">
  <h2 id="Sistemas numéricos">
    Sistemas numéricos
  </h2>

&emsp; **Sistemas numéricos** são formas padronizadas de representar quantidades utilizando uma base e um conjunto de símbolos. Em sistemas posicionais, o valor de cada algarismo depende da sua posição e da base utilizada.

- **Decimal:** sistema posicional de base 10 usado no cotidiano. Os algarismos utilizados são de 0 a 9, os dígitos da representação indo-arábica.

- **Binário:** sistema posicional de base 2 compreendido pelo computador. Os algarismos utilizados são 0 e 1, que representam falso e verdadeiro, respectivamente, definidos individualmente por uma faixa de tensão específica.

- **Hexadecimal:** sistema posicional de base 16 usado como compactação de códigos binários; ou seja, uma codificação taquigráfica. Os algarismos utilizados são de 0 a 9 da representação indo-arábica e de A a F do alfabeto latino, onde A representa o número decimal 10, B representa o número decimal 11, F representa o número decimal 15, etc. Um dígito hexadecimal representa 4 bits binários.

- **Octal:** sistema posicional de base 8 que foi utilizado como alternativa compacta em relação ao binário, tendo sido posteriormente substituído. Um dígito octal pode representar 3 bits binários.

</div>

<div class="definicoes" id="2">
  <h2 id="Representações de código">
    Representações de código
  </h2>

&emsp; **Representações de código** são formas de codificar informações para facilitar seu armazenamento, transmissão ou processamento, sem alterar o valor representado.

- **Binary-Coded Decimal (BCD):** cada dígito de um número decimal é convertido em seu equivalente binário de quatro bits. Apesar de ocupar mais bits para representar um número em relação ao binário puro, é mais fácil de converter, já que são utilizados apenas os valores binários correspondentes aos algarismos decimais de 0 a 9. Perceba que o código BCD precisa de mais bits que o binário porque sempre serão quatro bits, independente do valor a ser representado.
  - _Exemplos_: o número 3 (decimal) é 11 em binário e 0011 em BCD. 1 (decimal) é 

- **Código de Gray:** utilizado para minimizar erros. Em sistemas digitais, quando a quantidade de bits de um número binário muda (quando passa de três bits para 4 bits, por exemplo), todos os bits mudam de valor, e isso pode gerar erros no processo. Para corrigir esse problema, o código de Gray permite que apenas um bit seja alterado por vez, utilizando os mesmos dígitos do sistema binário.

</div>

<div class="conversao" markdown="1">
<p>

### Conversão

- **Decimal para binário**<br>
  $\quad$ Existem duas formas de converter um número da base decimal para a base binária:
  1. expressar o número como uma soma de potências de 2.<br>
    Exemplo: $235$ <br>
              &emsp;&emsp;&emsp; $= 128 + 64 + 32 + 8 + 2 + 1$ <br>
              &emsp;&emsp;&emsp; $= 2^7 + 2^6 + 2^5 + 2^3 + 2^1 + 2^0$ <br>
              &emsp;&emsp;&emsp; $= 2^7 + 2^6 + 2^5 + 0 \times 2^4 + 2^3 + 0 \times 2^2 + 2^1 + 2^0$
     

</p>
</div>

---

Para a conversão de binário para Gray:

> Seja o número binário $B = 100$ e o código Gray $= x_2x_1x_0$.
>
> 1. Repete-se o *most significant bit* (MSB) do binário como o MSB do código Gray.  
>    $G = 1x_1x_0$
>
> 2. Compara-se o MSB binário com o seu sucessor utilizando a operação lógica **ou exclusivo (XOR)**. Se $b_2 \neq b_1$, então $x_1=1$; caso contrário, $x_1=0$.  
>    $G = 11x_0$
>
> 3. Compara-se o dígito binário equivalente ao último dígito Gray determinado com o seu sucessor binário, seguindo o mesmo processo XOR do passo anterior.  
>    $G = 110$

&emsp; A conversão de Gray para binário ocorre de forma semelhante. Repete-se o MSB em Gray e, em seguida, compara-se o dígito $G_n$ com o dígito $B_{n+1}$, realizando a operação lógica **ou exclusivo (XOR)** entre eles.

---

<div>
  <table border="1" width="100">
  <tr>
    <th><b>Alguns termos:</b></th>
    <td>
      <p><b>- Byte:</b> conjunto de 8 bits. A maioria dos microcomputadores armazena dados binários e informações em grupos de 8 bits.</p>
      <p><b>- Nibble:</b> conjunto de 4 bits.</p>
      <p><b>- Word:</b> quantidade de bits tratados como uma unidade de informação. Se uma transmissão envia 4 bytes por vez, então sua <i>word</i> tem tamanho de 32 bits.</p>
      <p><b>- Código alfanumérico ASCII:</b> além de números, representa também caracteres não numéricos, como letras do alfabeto e outros símbolos, além de funções como <i>RETURN</i> e <i>LINE FEED</i>. O ASCII original possui 7 bits, totalizando 128 representações possíveis, mas o ASCII extendido é mais utilizado hoje, tendo 8 bits, ou seja, 265 representações possíveis.</p>
    </td>
  </tr>
</table>
  
</div>

---

<div class="definicioes" id="4">
  <h2 id="Método de Paridade">
    Método de Paridade
  </h2>
  
&emsp; Utilizado para detectar erros na transmissão quando a probabilidade de ocorrência de apenas um bit incorreto é pequena, porém possível. No caso de haver erro em dois ou mais bits, o método de paridade é ineficaz.


- **Paridade Par:** adiciona-se um bit à esquerda, de modo que a quantidade de dígitos 1 do código seja um número natural par.
- **Paridade Ímpar:** adiciona-se um bit à esquerda, de modo que a quantidade de dígitos 1 do código seja um número natural ímpar.

</div>

