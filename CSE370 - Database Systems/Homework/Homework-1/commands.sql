create table Developers ( member_id int, name char(20), email char(30), influence_count int, Joining_date date, multiplier int );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 1, 'Taylor Otwell', 'otwell@laravel.com', 739360, '2020-6-10', 10 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 2, 'Ryan Dahl', 'ryan@nodejs.org', 633632, '2020-04-22', 10 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 3, 'Brendan Eich', 'eich@javascript.com', 939570, '2020-05-07', 8 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 5, 'Evan You', 'you@vuejs.org', 982630, '2020-06-11', 7 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 6, 'Rasmus Lerdorf', 'lerdorf@php.net', 937927, '2020-06-3', 8 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 7, 'Guido van Rossum', 'guido@python.org', 968827, '2020-07-18', 19 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 8, 'Adrian Holovaty', 'adrian@djangoproject.com', 570724, '2020-05-07', 5 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 9, 'Simon Willison', 'simon@djangoproject.com', 864615, '2020-04-30', 4 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 10, 'James Gosling', 'james@java.com', 719491, '2020-05-18', 5 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 11, 'Rod Johnson', 'rod@spring.io', 601744, '2020-05-18', 7 );

insert into Developers(member_id, name, email, influence_count, Joining_date, multiplier) values ( 12, 'Satoshi Nakamoto', 'nakamoto@blockchain.com', 630488, '2020-05-10', 10 );

ALTER TABLE Developers CHANGE influence_count followers int;

UPDATE Developers SET  followers = followers + 10;

Select name, email, followers from Developers;

Select name, ((followers*100/1000000) * (multiplier*100/20))/100 as Efficiency from Developers;