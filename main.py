import sys
from generator import generate_tex
from compiler import compile_tex

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <data_file.json> <template_file.tex>")
        sys.exit(1)

    data_file = sys.argv[1]
    template_file = sys.argv[2]
    output_tex = "output/output.tex"

    generate_tex(data_file, template_file, output_tex)
    compile_tex(output_tex, output_dir="output")

if __name__ == "__main__":
    main()
