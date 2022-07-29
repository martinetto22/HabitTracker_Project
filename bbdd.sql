USE HabitsProject;

CREATE TABLE Users(
		username VARCHAR(20),
            	pw VARCHAR(100),
            
            	PRIMARY KEY (username)
);

CREATE TABLE Objectives(
		username VARCHAR(20), 
		name_O VARCHAR(50),
		inici VARCHAR(20),
            	finally VARCHAR(20),
            	description_O VARCHAR(1000),
            	ID_O INT auto_increment,
            	ACHIVEMENT boolean not null default 0,
            	achivement_date VARCHAR(20),
            
            	PRIMARY KEY (ID_O),
            	FOREIGN KEY (username) REFERENCES Users(username)
);

CREATE TABLE DailyHabits(
		ID_O INT,
		daily_habits VARCHAR(1000),
		ID_DH INT auto_increment,
            
            	PRIMARY KEY (ID_DH),
       		FOREIGN KEY (ID_O) REFERENCES Objectives(ID_O)
);

CREATE TABLE DailyHabitsACHIEVED(
		ID_DH INT,
		username VARCHAR(20),
		Data VARCHAR(20), 
		YES_NO VARCHAR(20),
		
		FOREIGN KEY (ID_DH) REFERENCES DailyHabits(ID_DH),
		FOREIGN KEY (username) REFERENCES Users(username)
);


CREATE TABLE WeeklyHabits(
		ID_O INT,
		weekly_habits VARCHAR(1000),
		ID_WH INT auto_increment,
		
            	PRIMARY KEY (ID_WH),
            	FOREIGN KEY (ID_O) REFERENCES Objectives(ID_O)
);


CREATE TABLE WeeklyHabitsACHIEVED(
		ID_WH INT,
		username VARCHAR(20),
		Data VARCHAR(20), 
		YES_NO VARCHAR(20),
		
		FOREIGN KEY (ID_WH) REFERENCES WeeklyHabits(ID_WH),
		FOREIGN KEY (username) REFERENCES Users(username)
);


INSERT INTO Users (username, pw) VALUES ('''marti''', '''abc23''');

INSERT INTO Objectives (username, name_O, inici, finally, description_O) VALUES ('''marti''', '''Python''', '''2022-07-11''', '''2022-09-29''', '''Learn Python''');
INSERT INTO Objectives (username, name_O, inici, finally, description_O, ACHIVEMENT, achivement_date) VALUES ('''marti''', '''Artificial Intelligence''', '''2022-07-11''', '''2022-12-01''', '''Learn IA''', true, '''2022-07-23''');
INSERT INTO Objectives (username, name_O, inici, finally, description_O) VALUES ('''marti''', '''Grade''', '''2022-07-11''', '''2025-01-01''', '''Completion of the Artificial Intelligence degree''');

INSERT INTO DailyHabits (ID_O, daily_habits) VALUES (1, '''Study 1h''');
INSERT INTO DailyHabits (ID_O, daily_habits) VALUES (2, '''Study 1h''');
INSERT INTO DailyHabits (ID_O, daily_habits) VALUES (3, '''Do not procrastinate daily tasks''');

/*We keep the dates on which the daily habits have been fulfilled (or not).*/
HABIT 1 */
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-12''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-13''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-14''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-15''', '''no''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-16''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-17''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-18''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-19''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-20''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-21''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-22''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-23''', '''yes''');
/*INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-24''', '''no''');*/

/*HABIT 2*/
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-12''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-13''', '''no''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-14''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-15''', '''no''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-16''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-17''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-18''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-19''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-20''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-21''', '''no''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-22''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-23''', '''no''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-24''', '''yes''');


/*HABIT 3*/
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-12''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-13''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-14''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-15''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-16''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-17''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-18''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-19''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-20''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-21''', '''no''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-22''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-23''', '''yes''');
INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-24''', '''yes''');


/*WEEKLY HABITS creation*/
INSERT INTO WeeklyHabits (ID_O, weekly_habits) VALUES (1, '''Review the weekly agenda''');
INSERT INTO WeeklyHabits (ID_O, weekly_habits) VALUES (2, '''Staying motivated to learn''');
INSERT INTO WeeklyHabits (ID_O, weekly_habits) VALUES (3, '''Be sure that I have all weekly tasks completed.''');

/*We keep the dates on which the weekly habits have been fulfilled (or not).*/
INSERT INTO WeeklyHabitsACHIEVED (ID_WH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-17''', '''yes''');
/*INSERT INTO WeeklyHabitsACHIEVED (ID_WH, username, Data, YES_NO) VALUES (1, '''marti''', '''2022-07-24''', '''yes''');*/
INSERT INTO WeeklyHabitsACHIEVED (ID_WH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-17''', '''yes''');
/*INSERT INTO WeeklyHabitsACHIEVED (ID_WH, username, Data, YES_NO) VALUES (2, '''marti''', '''2022-07-24''', '''no''');*/
INSERT INTO WeeklyHabitsACHIEVED (ID_WH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-17''', '''no''');
/*INSERT INTO WeeklyHabitsACHIEVED (ID_WH, username, Data, YES_NO) VALUES (3, '''marti''', '''2022-07-24''', '''yes''');*/
