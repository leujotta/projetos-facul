triangulo <- function(B, L1, L2){
  
  P <- B + L1 + L2
  p <- P / 2
  a <- sqrt(p * (p - B) * (p - L1) * (p - L2))
  tri <- B < L1 + L2 && L1 < L2 + B && L2 < L1 + B
  
  
  if (tri && B == L1 && L1 == L2 && L2 == B) {
    cat('o triangulo é equilatero e seu perimetro é:' , P , 'e sua area é:' , a)
  } else if (tri && B == L1 || L1 == L2 || L2 == B) {
    cat('o triangulo é isoceles e seu perimetro é:' , P , 'e sua area é:' , a)
  } else if (tri && B != L1 && L1 != L2 && L2 != B) {
    cat('o triangulo é escaleno e seu perimetro é:' , P , 'e sua area é:' , a)
  } else{
    cat('nao é um triangulo')}
  
  
}

