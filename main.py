from pdfrw import PdfReader, PdfWriter, IndirectPdfDict


def concatenate(
    paths: list, output: str, title: str, _subject: str, _creator: str
) -> None:
    writer = PdfWriter()

    for _file in paths:
        reader = PdfReader(_file)
        writer.addpages(reader.pages)

    writer.trailer.Info = IndirectPdfDict(
        Title=title,
        Author="Ahmed ElSheikh",
        Subject=_subject,
        creator=_creator,
    )

    writer.write(output)


if __name__ == "__main__":
    _paths = ["pdf_files/Passport.pdf", "pdf_files/Permesso.pdf"]
    concatenate(
        _paths, "pdf_files/output.pdf", title="New pdf", _subject="personal docs", _creator="ME"
    )
