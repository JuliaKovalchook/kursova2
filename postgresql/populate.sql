INSERT INTO Groups VALUES('KM-61');
INSERT INTO Groups VALUES('KM-62');
INSERT INTO Groups VALUES('KM-63');
INSERT INTO Groups VALUES('KM-64');

INSERT INTO Subjects VALUES('Math');
INSERT INTO Subjects VALUES('English');
CREATE TABLE Subjects2(predmet text);
ALTER TABLE Subjects2
ADD CONSTRAINT predmet_pk PRIMARY KEY(predmet);

INSERT INTO Subjects2 VALUES('test');
INSERT INTO Subjects VALUES('Turkish');

INSERT INTO Students VALUES('Volodymyr', 'Drapak', 'KM6103', 'TBD', 'TBD', 'KM-61');
INSERT INTO Students VALUES('Random', 'Guy', 'KM6200', 'TBD', 'TBD', 'KM-62');
INSERT INTO Students VALUES('Always', 'Absent', 'KM6250', 'bad', 'otchislen', 'KM-63');

INSERT INTO SubjectSheet VALUES('Math', 'KM-61', 'KM6103', TO_DATE('28.10.19', 'DD.MM.YY'), 100);
INSERT INTO SubjectSheet VALUES('English', 'KM-61', 'KM6103', TO_DATE('21.10.19', 'DD.MM.YY'), 100);
INSERT INTO SubjectSheet VALUES('Ukrainian', 'KM-61', 'KM6103', TO_DATE('21.10.19', 'DD.MM.YY'), -200);

INSERT INTO group_subject VALUES(2015, 1, 'KM-61', 'Math');
INSERT INTO group_subject VALUES(2015, 1, 'KM-61', 'English');
INSERT INTO group_subject VALUES(2015, 2, 'KM-61', 'English');

INSERT INTO studentstatus VALUES('KM6103', 'handsome', 'scholarship', TO_DATE('11.11.19', 'DD.MM.YY'));
INSERT INTO studentstatus VALUES('KM6200', 'good', 'otchislen', TO_DATE('11.11.19', 'DD.MM.YY'));
INSERT INTO studentstatus VALUES('KM6250', 'handsome', 'dopobachennya', TO_DATE('11.11.19', 'DD.MM.YY'));

INSERT INTO subjects_marks VALUES('Math', 10, TO_DATE('11.11.19', 'DD.MM.YY'));
INSERT INTO subjects_marks VALUES('English', 50, TO_DATE('11.11.19', 'DD.MM.YY'));
INSERT INTO subjects_marks VALUES('Economy', 40, TO_DATE('11.11.19', 'DD.MM.YY'));


SELECT * FROM Groups;
SELECT * FROM Subjects;
SELECT * FROM Students;
SELECT * FROM SubjectSheet;
