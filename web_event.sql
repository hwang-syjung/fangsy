BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "web_event" (
	"event_id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	varchar(200) NOT NULL,
	"content"	text,
	"schedule"	datetime NOT NULL,
	"location"	varchar(100),
	"created_date"	datetime NOT NULL
);
INSERT INTO "web_event" VALUES (1,'fangsy','fangsy','2019-10-29 11:20:15',NULL,'2019-10-29 11:20:18.480316');
INSERT INTO "web_event" VALUES (2,'indie','indie','2019-11-04 07:27:23',NULL,'2019-11-04 07:27:36.000734');
INSERT INTO "web_event" VALUES (3,'황시정','황시정','2019-11-04 07:27:50',NULL,'2019-11-04 07:27:53.392078');
INSERT INTO "web_event" VALUES (4,'김채욱','김채욱','2019-11-04 07:28:04',NULL,'2019-11-04 07:28:06.059073');
INSERT INTO "web_event" VALUES (5,'연보라','연보라','2019-11-04 07:28:13',NULL,'2019-11-04 07:28:14.441023');
INSERT INTO "web_event" VALUES (6,'진수','진수','2019-11-04 07:28:23',NULL,'2019-11-04 07:28:24.716318');
INSERT INTO "web_event" VALUES (7,'오수빈','오수빈','2019-11-04 07:28:31',NULL,'2019-11-04 07:28:32.860099');
INSERT INTO "web_event" VALUES (8,'hwangsyjung','hwangsyjung','2019-11-04 07:28:44',NULL,'2019-11-04 07:28:45.905361');
INSERT INTO "web_event" VALUES (9,'홍세인','홍세인','2019-11-04 07:28:56',NULL,'2019-11-04 07:28:56.975220');
INSERT INTO "web_event" VALUES (10,'인디가수','인디가수입니다.','2019-11-04 07:29:05',NULL,'2019-11-04 07:29:07.016346');
COMMIT;
