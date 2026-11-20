% Q28: Student-Teacher-Subject database
student(101, arun).
student(102, bala).
student(103, charan).
student(104, david).

teacher(t1, ramesh).
teacher(t2, kumar).
teacher(t3, priya).

subject(c101, mathematics).
subject(c102, physics).
subject(c103, computer_science).

takes(101, t1, c101).
takes(102, t2, c102).
takes(103, t3, c103).
takes(104, t1, c103).

details(Id, StudentName, TeacherId, TeacherName, SubjectCode, SubjectName) :-
    student(Id, StudentName),
    takes(Id, TeacherId, SubjectCode),
    teacher(TeacherId, TeacherName),
    subject(SubjectCode, SubjectName).

% Query: ?- details(101, S, T, TN, C, SN).
% S = arun, T = t1, TN = ramesh, C = c101, SN = mathematics.
