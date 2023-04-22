'''Inserir três valores, “B”, “L1”, “L2”, verificar se é um triangulo ou não. Se for,
classifique em equilátero, escaleno ou isósceles, e forneça o perímetro e sua área.
Se não for triangulo, retornar alguma mensagem ao usuário.'''

#inserir os valores
B <- as.numeric (readline ('digite o valor da base do triangulo:'))
L1 <- as.numeric (readline ('digite o valor do lado do triangulo:'))
L2 <- as.numeric (readline ('digite o valor do outro lado do triangulo:'))

#verificar se é triangulo
{
if (B < L1 + L2 && L1 < L2 + B && L2 < L1 + B){
  triangulo <- TRUE
  print('é um triangulo')}
  else{
    triangulo <- FALSE
    print('não é um triangulo, a operação acabou')}}
  
#se for triangulo, classificar em equilátero, isóceles ou escaleno
{
if (B == L1 && L1 == L2 && L2 == B){
  print('o triangulo é equílatero')}}
  
{
if (B == L1 || L1 == L2 || L2 == B){
  print('o triangulo é isóceles')}}

{
  if (B != L1 && L1 != L2 && L2 != B){
    print('o triangulo é escaleno')}}

#fornecer perímetro e área
P <- (B + L1 + L2)
p <- P / 2
{
  if (triangulo <- TRUE){
    print(paste('o perímetro do seu triangulo é:', P))
    print(paste('a área do seu triangulo é:', (sqrt(p * (p - B) * (p - L1) * (p - L2)))))}
  }