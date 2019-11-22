cppcalc: calc.o scanner.o token.o ast.o parser.o calculator.o
	g++ -g -o cppcalc calc.o scanner.o token.o ast.o parser.o calculator.o

calc.o: calc.cpp scanner.h token.h
	g++ -g -c calc.cpp

calculator.o: calculator.cpp calculator.h parser.h ast.h
	g++ -g -c calculator.cpp

scanner.o: scanner.cpp scanner.h token.h
	g++ -g -c scanner.cpp

token.o: token.cpp token.h
	g++ -g -c token.cpp

ast.o: ast.cpp ast.h
	g++ -g -c ast.cpp

parser.o: parser.cpp parser.h
	g++ -g -c parser.cpp

clean:
	rm -f *.o
	rm -f cppcalc
