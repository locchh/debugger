       IDENTIFICATION DIVISION.
       PROGRAM-ID. SumProgram.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  NUM1            PIC 9(3) VALUE 100.
       01  NUM2            PIC 9(3) VALUE 200.
       01  RESULT          PIC 9(4).

       PROCEDURE DIVISION.
       ADD NUM1 TO NUM2 GIVING RESULT.
       DISPLAY "The sum is: " RESULT.
       STOP RUN.
