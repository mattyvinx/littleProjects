Attribute VB_Name = "Module1"
Sub TableauWeatherDBPrep()
    Dim ws As Worksheet
    Dim wb As Workbook
    Dim savePath As String
    
    ' Set the active worksheet
    Set ws = ActiveSheet ' Modify if needed, e.g., Set ws = ThisWorkbook.Sheets("Sheet1")
    
    ' Delete rows 2 and 3
    ws.Rows("2:3").Delete Shift:=xlUp
    
    ' Update headers
    ws.Range("G1").Value = "2020 land area mi2"
    ws.Range("H1").Value = "2020 land area km2"
    ws.Range("I1").Value = "2020 density / mi2"
    ws.Range("J1").Value = "2020 density / km2"
    
    ' Create worksheet copy
    ws.Copy ' This creates a new workbook with only this sheet
    Set newWb = ActiveWorkbook ' The copied sheet is now in a new workbook
    
    
    MsgBox "New Tableau Data file created.", vbInformation
End Sub

