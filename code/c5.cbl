       IDENTIFICATION DIVISION.
       PROGRAM-ID. AnotherInvalidProgram.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  NUM1            PIC X(3) VALUE "100".
       01  NUM2            PIC 9(3) VALUE 50.
       01  RESULT          PIC 9(4).

       PROCEDURE DIVISION.
       IF NUM1 > NUM2
           DISPLAY "NUM1 is greater than NUM2"
       DISPLAY "Result: " RESULT.
       STOP RUN.
