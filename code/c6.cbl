       IDENTIFICATION DIVISION.
       PROGRAM-ID. AskNameJapanese.

       ENVIRONMENT DIVISION.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 USER-NAME       PIC X(30).
       01 PROMPT           PIC X(50) VALUE "お名前を入力してください: ".

       PROCEDURE DIVISION.
       DISPLAY PROMPT.
       ACCEPT USER-NAME.
       DISPLAY "こんにちは, " USER-NAME "さん！".
       STOP RUN.
