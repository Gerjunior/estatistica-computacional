#Estatística Computacional

## ***Array Inicial: [-1, -8,-20, -12, 0, 5, 7, 14, 25]***

### ***Amplitude Total***
 **AT = x(Max) - x(Min)**  
 **AT** -> Amplitude Total  
 **Max** -> Maior Valor do Array  
 **Min** -> Menor Valor do Array  

AT = 25 - (-20)  
AT = 45  

### ***Desvio Quartilico***  

 **Q1** = (n + 1) / 4  
 **Q2** = ((n + 1) * 2) / 4  
 **Q3** = ((n + 1) * 3) / 4  

**n** -> Tamanho do array  
**Q1, Q2, Q3** -> Posições   


**_Ordenar_**: [-20, -12, -8, -1, 0, 5, 7, 14, 25]  

n = 9

Q1 = (9 + 1) / 4 = _2.5_  
Q2 = (9 + 1) * 2 / 4 = _5_  
Q2 = (9 + 1) * 3 / 4 = _7.5_  

<pre>
 [-20, -12, -8, -1, 0, 5, 7, 14, 25]  
           ^                ^ 
       Q1(pos 2,5)      Q3(pos 7,5)
 </pre>
___
<pre>
Q1 = -12-(-8)= 4
	  4/2 = 2
</pre>
>Onde 4 é a diferença entre os elementos das posições 2 e 3  
>Onde 2 é a metade (o "meio" (0,5) de 2,5)  
<pre>Q1 = -12 + 2= -10</pre> 
> Onde -10 é o elemento na posição 2,5  

<pre>Q2 = 0 (pos 5)</pre>
<pre>
Q3 = 14 - 7
7/2 = 3,5
Q3 = 7 + 3,5 = 10,5
</pre>
___
Então, temos:  
```
Q1(2,5) = -10  
Q2(5) = 0  
Q3(7,5) = 10,5  
```

**Desvio interquartílico** = Q3 - Q1  
DIQ = 10,5 - (-10)  
DIQ = 20,5  



