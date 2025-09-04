import json
from pathlib import Path

def generate_tex(data_file: str, template_file: str, output_file: str):
    with open(data_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(template_file, "r", encoding="utf-8") as f:
        tex = f.read()

    exp_tex = ""
    for exp in data.get("experiences", []):
        exp_tex += f"\\textbf{{{exp['title']}, {exp['company']}}} \\hfill {exp['period']} \\\\\n"
        exp_tex += "\\begin{itemize}[leftmargin=1.5em]\n"
        for act in exp["activities"]:
            exp_tex += f"  \\item {act}\n"
        exp_tex += "\\end{itemize}\n\n"

    edu_tex = ""
    for edu in data.get("education", []):
        edu_tex += f"\\textbf{{{edu['degree']}}} \\hfill {edu['period']} \\\\\n"
        edu_tex += f"{edu['institution']} \\\\\n\n"

    proj_tex = ""
    for proj in data.get("projects", []):
        proj_tex += f"\\textbf{{{proj['name']}}} \\\\ \n"
        proj_tex += f"{proj['description']} \\\\ \n"
        proj_tex += f"\\textit{{{proj['url']}}} \\\\\n\n"

    lang_tex = ""
    for lang in data.get("languages", []):
        lang_tex += f"{lang['language']} — {lang['level']} \\\\\n"
    
    ach_tex = ""
    for ach in data.get("achievements", []):
        ach_tex += f"\\item {ach}\n"

    skills_tex = ", ".join(data.get("skills", []))

    replacements = {
        "__NAME__": data["name"],
        "__ROLE__": data["role"],
        "__EMAIL__": data["email"],
        "__PHONE__": data["phone"],
        "__LOCATION__": data["location"],
        "__LINKEDIN__": data.get("linkedin", ""),
        "__GITHUB__": data.get("github", ""),
        "__PROFILE__": data["profile"],
        "__EXPERIENCES__": exp_tex,
        "__EDUCATION__": edu_tex,
        "__PROJECTS__": proj_tex,
        "__SKILLS__": skills_tex,
        "__LANGUAGES__": lang_tex,
        "__ACHIEVEMENTS__": f"\\begin{{itemize}}[leftmargin=1.5em]\n{ach_tex}\\end{{itemize}}",
    }

    for key, value in replacements.items():
        tex = tex.replace(key, value)

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tex)

    print(f"✅ LaTeX file generated at: {output_file}")
