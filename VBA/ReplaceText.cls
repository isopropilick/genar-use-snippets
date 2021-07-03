Sub ReplaceText()
Dim wApp As Word.Application
Dim wDoc As Word.Document
Path = GetDesktop()
Dim folderPath As String

folderPath = Application.ActiveWorkbook.Path
Set wApp = CreateObject("Word.Application")
wApp.Visible = True
FinalRow = Range("A9999").End(xlUp).Row
    For i = 1 To FinalRow
Set wDoc = wApp.Documents.Open(folderPath & "/qa.docx")
With wDoc
    .Application.Selection.Find.Text = "TC1"
    .Application.Selection.Find.Execute
    .Application.Selection = Range("A" & i)
   '  .Application.Selection.EndOf
   '  .Application.Selection.Find.Text = "DESC1"
   '  .Application.Selection.Find.Execute
   '  .Application.Selection = Range("B" & i)
    .SaveAs2 Filename:=Path & "/" & Range("C" & i) & "-" & Range("A" & i) & ".docx", _
    FileFormat:=wdFormatXMLDocument, AddtoRecentFiles:=False
    wApp.ActiveDocument.Close
End With
Next i
wApp.Quit
End Sub
