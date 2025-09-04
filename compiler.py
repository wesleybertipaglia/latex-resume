import subprocess
from pathlib import Path

def compile_tex(tex_file: str, output_dir: str = "output"):
    tex_path = Path(tex_file)
    if not tex_path.exists():
        raise FileNotFoundError(f"File {tex_file} not found.")

    cmd = [
        "xelatex",
        "-interaction=nonstopmode",
        f"-output-directory={output_dir}",
        str(tex_path)
    ]

    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"📄 PDF generated at: {output_dir}/{tex_path.stem}.pdf")
    except subprocess.CalledProcessError as e:
        print("❌ Error compiling LaTeX:")
        print(e.stdout.decode())
        print(e.stderr.decode())
