       IDENTIFICATION DIVISION.
       PROGRAM-ID. EvenOddProgram.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  NUMBER          PIC 9(3).
       01  REMAINDER       PIC 9(1).

       PROCEDURE DIVISION.
       DISPLAY "Enter a number: ".
       ACCEPT NUMBER.
       COMPUTE REMAINDER = NUMBER MOD 2.

       IF REMAINDER = 0
           DISPLAY "The number is even."
       ELSE
           DISPLAY "The number is odd."
       END-IF.

       STOP RUN.
