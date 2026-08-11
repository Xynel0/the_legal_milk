# Álgebra Linear

## Aula 01

A **Álgebra Linear** é, de forma bem simplificada, utilizada para resolver equações que possuem mais de uma incógnita. Como exemplo, seja a equação $5x_1 + 7x_2 - x_3 + 9x_4 = 3$. Nela, as incógnitas $x_1, x_2, x_3$ e $x_4$ são desconhecidas e independentes entre si. O primeiro conteúdo irá lidar com grupos desses tipos de equação e as formas de resolvê-las.

### Sistemas lineares (de equações)

Lembra dos sistemas de equações, em que duas ou mais equações possuíam as mesmas duas variáveis e, analisando elas sozinhas, não era possível encontrar um conjunto solução? Nesse caso, conseguíamos relacionar as duas equações e descobrir a resposta através disso. Vejamos um exemplo simples:

$$
\begin{cases}
2x + y = 7 \quad (I) \\
x - 3y = -5 \quad (II)
\end{cases}
$$

Sistemas lineares são sistemas de equações que possuem $n$ incógnitas. Dito isso, os sistemas estudados na álgebra comum são sistemas lineares básicos, de duas variáveis. Em geral, as equações que os compõem são da forma $a_1x_1 + a_2x_2 + a_3x_3 + \dots + a_nx_n$, sendo essa expressão definida como uma equação linear de $n$ variáveis. Exemplo:

$$
\begin{cases}
5x_1 + 7x_2 - x_3 + 9x_4 = 3 \\
2x_1 + 6x_2 - 4x_3 + 5x_4 = 2
\end{cases}
$$

- Equações lineares podem ser representadas através de um somatório: $\sum_{i=1}^{n} a_ix_i$.

Como se já não fosse o bastante, também existem os **sistemas lineares com $n$ incógnitas e $m$ equações**, dados na forma:

$$
\begin{array}{rcr}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n & = & b_1 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n & = & b_2 \\
\vdots & & \vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n & = & b_m
\end{array}
$$

Uma forma de resolver um sistema como esse é substituí-lo por um **sistema equivalente**, ou seja, um sistema com as mesmas variáveis e mesmo conjunto solução. Claro, queremos encontrar um equivalente que seja mais simples que o original.

### Geração de Sistemas Equivalentes

Os métodos são os seguintes:

1. **Trocar a ordem das equações;**
2. **Multiplicar uma equação por uma constante (diferente de zero);**
3. **Substituir uma equação pela sua soma com um múltiplo de outra equação.**

Veremos como cada procedimento é feito, passo a passo.
