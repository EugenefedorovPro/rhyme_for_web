import markdown2
from django.shortcuts import render
from pathlib import Path


def get_about(request):
    # import about rhyme md
    path = Path("__file__").parent.parent
    path_rhyme = path / "readme_rhyme.md"
    with open(path_rhyme, "r", encoding="utf-8") as file:
        about_md = file.read()
    rhyme_html = markdown2.markdown(about_md)

    # import about author md
    path_author = path / "readme_author.md"
    with open(path_author, "r", encoding="utf-8") as file:
        author_md = file.read()
        author_html = markdown2.markdown(author_md)

    # import about stress md
    path_stress = path / "readme_stress.md"
    with open(path_stress, "r", encoding="utf-8") as file:
        stress_md = file.read()
        stress_html = markdown2.markdown(stress_md)

    # import about stress md
    path_transcribe = path / "readme_transcribe.md"
    with open(path_transcribe, "r", encoding="utf-8") as file:
        transcribe_md = file.read()
        transcribe_html = markdown2.markdown(transcribe_md)

    context = {
        "rhyme_html": rhyme_html,
        "author_html": author_html,
        "stress_html": stress_html,
        "transcribe_html": transcribe_html,
    }

    return render(request, "about.html", context)
