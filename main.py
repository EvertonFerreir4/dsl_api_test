from antlr4 import FileStream, CommonTokenStream
from ApiTestLexer import ApiTestLexer
from ApiTestParser import ApiTestParser
from ApiTestCustomVisitor import ApiTestCustomVisitor
from generator import generate_test_code

def compile_apitest(filename: str, out_filename: str = "test_api_generated.py"):
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = ApiTestLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ApiTestParser(stream)
    tree = parser.spec()

    visitor = ApiTestCustomVisitor()
    spec = visitor.visit(tree)

    code = generate_test_code(spec)

    with open(out_filename, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Arquivo de teste gerado: {out_filename}")

def main():
    compile_apitest("exemplo.apitest")

if __name__ == "__main__":
    main()
