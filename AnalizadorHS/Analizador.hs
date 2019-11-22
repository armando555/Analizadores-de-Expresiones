import Data.Char

--type Analizador = String -> Tree
--type Analizador = String -> (Tree,String)
--type Analizador = String -> [(Tree,String)]
type Analizador a = String ->[(a,String)]

analiza :: Analizador a -> String -> [(a,String)]
analiza a cs = a cs

resultado ::a -> Analizador a
resultado v = \xs -> [(v,xs)]

fallo :: Analizador a
fallo = \xs -> []

elemento :: Analizador Char
elemento = \xs -> case xs of
                    [] -> []
                    (x:xs) -> [(x , xs)]

infixr 5 >*>
(>*>) :: Analizador a -> (a -> Analizador b) -> Analizador b
p >*> f = \ent -> case analiza p ent of
                    []        -> []      
                    [(v,sal)] -> analiza (f v) sal

primeroTercero :: Analizador (Char,Char)
primeroTercero =
    elemento >*> \x ->
    elemento >*> \_ ->
    elemento >*> \y ->
    resultado (x,y)
    

(+++) :: Analizador a -> Analizador a -> Analizador a
p +++ q = \ent -> case analiza p ent of
                    []        -> analiza q ent
                    [(v,sal)] -> [(v,sal)]

sat :: (Char -> Bool) -> Analizador Char
sat p = elemento >*> \x -> 
        if p x then resultado x else fallo


digito :: Analizador Char
digito = sat isDigit


minuscula :: Analizador Char
minuscula = sat isLower

mayuscula :: Analizador Char
mayuscula = sat isUpper

letra :: Analizador Char
letra = sat isAlpha


alfanumerico :: Analizador Char
alfanumerico = sat isAlphaNum

caracter :: Char -> Analizador Char
caracter x = sat (==x) 

cadena :: String -> Analizador String 
cadena []     = resultado []
cadena (x:xs) = caracter x >*> \x ->
                cadena xs >*> \xs ->
                resultado (x:xs)

varios :: Analizador a -> Analizador [a]
varios p = varios1 p +++ resultado []

varios1 :: Analizador a -> Analizador [a]
varios1 p = p        >*> \v  ->
            varios p >*> \vs ->
            resultado (v:vs)


ident :: Analizador String 
ident = minuscula           >*> \x  ->
        varios alfanumerico >*> \xs ->
        resultado (x:xs)

nat :: Analizador Float
nat = varios1 digito >*> \xs ->
      resultado (read xs)

espacio :: Analizador ()
espacio = varios (sat isSpace) >*> \_ ->
          resultado ()

unidad :: Analizador a -> Analizador a
unidad p = espacio >*> \_ ->
           p       >*> \v ->
           espacio >*> \_ ->
           resultado v

identificador :: Analizador String
identificador = unidad ident

natural :: Analizador Float
natural = unidad nat

simbolo :: String -> Analizador String
simbolo xs = unidad (cadena xs)


listaNat :: Analizador [Float]
listaNat = simbolo "["          >*> \_ ->
           natural              >*> \n -> 
           varios (simbolo ","  >*> \_ ->
                   natural)     >*> \ns ->
           simbolo "]"          >*> \_ ->
           resultado (n:ns)

expr :: Analizador Float
expr = term             >*> \t ->
       (simbolo "+"     >*> \_ ->
       expr             >*> \e ->
       resultado (t+e))
       +++ resultado t

expr1 :: Analizador Float
expr1 = term1             >*> \t ->
       (simbolo "-"     >*> \_ ->
       expr1             >*> \e ->
       resultado (t-e))
       +++ resultado t


term :: Analizador Float
term = factor             >*> \f ->
       (simbolo "*"        >*> \_ ->
       term                >*> \t ->
       resultado (f*t))
       +++ resultado f

term1 :: Analizador Float
term1 = factor1              >*> \f ->
       (simbolo "/"         >*> \_ ->
       term1                >*> \t ->
       resultado (f/t))
       +++ resultado f

factor :: Analizador Float
factor = (simbolo "("      >*> \_ ->
         expr              >*> \e ->
         simbolo ")"       >*> \_ ->
         resultado e)
         +++ natural


factor1 :: Analizador Float
factor1 = (simbolo "("      >*> \_ ->
         expr1              >*> \e ->
         simbolo ")"       >*> \_ ->
         resultado e)
         +++ natural

valor :: String -> Float
valor xs = case (analiza expr xs) of
            [(n,[])]    -> n
            [(_,sal)]   ->error ("sin usar "++sal)
            []          ->error "entrada no válida"

valor1 :: String -> Float
valor1 xs = case (analiza expr1 xs) of
            [(n,[])]    -> n
            [(_,sal)]   ->error ("sin usar "++sal)
            []          ->error "entrada no válida"
    