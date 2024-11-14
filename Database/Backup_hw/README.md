# Домашнее задание к занятию "`Индексы`" - `Borodavkin Sergey`


### Инструкция по выполнению домашнего задания

   1. Сделайте `fork` данного репозитория к себе в Github и переименуйте его по названию или номеру занятия, например, https://github.com/имя-вашего-репозитория/git-hw или  https://github.com/имя-вашего-репозитория/7-1-ansible-hw).
   2. Выполните клонирование данного репозитория к себе на ПК с помощью команды `git clone`.
   3. Выполните домашнее задание и заполните у себя локально этот файл README.md:
      - впишите вверху название занятия и вашу фамилию и имя
      - в каждом задании добавьте решение в требуемом виде (текст/код/скриншоты/ссылка)
      - для корректного добавления скриншотов воспользуйтесь [инструкцией "Как вставить скриншот в шаблон с решением](https://github.com/netology-code/sys-pattern-homework/blob/main/screen-instruction.md)
      - при оформлении используйте возможности языка разметки md (коротко об этом можно посмотреть в [инструкции  по MarkDown](https://github.com/netology-code/sys-pattern-homework/blob/main/md-instruction.md))
   4. После завершения работы над домашним заданием сделайте коммит (`git commit -m "comment"`) и отправьте его на Github (`git push origin`);
   5. Для проверки домашнего задания преподавателем в личном кабинете прикрепите и отправьте ссылку на решение в виде md-файла в вашем Github.
   6. Любые вопросы по выполнению заданий спрашивайте в чате учебной группы и/или в разделе “Вопросы по заданию” в личном кабинете.
   
Желаем успехов в выполнении домашнего задания!
   
### Дополнительные материалы, которые могут быть полезны для выполнения задания

1. [Руководство по оформлению Markdown файлов](https://gist.github.com/Jekins/2bf2d0638163f1294637#Code)

---

### Задание 1

1.1 Восстановление данных за предыдущий день:
Полный бэкап - ежедневно, чтобы сохранить полную копию базы данных.
Инкрементальные/дифференциальные бэкапы - дополняют полный бэкап, сохраняя изменения за день.
1.2 Восстановление данных за час до поломки:
Журнал транзакций - позволяет восстановить базу данных до конкретного времени.
Точечное восстановление - использование журналов транзакций для восстановления базы данных на нужный момент времени.
Таким образом, для первого случая — полные и инкрементальные бэкапы, для второго — журналы транзакций и точечное восстановление.


### Задание 2
- pg_dump:
***bash 
pg_dump -U username -F c -b -v -f /path/to/backup/file.backup dbname
***
pg_restore:
***bash
pg_restore -U username -d dbname -v /path/to/backup/file.backup
***

Можно автоматизировать с помощью cron

- бэкап

***bash 
#!/bin/bash

USER="username"
DBNAME="dbname"
BACKUP_DIR="/path/to/backup"
BACKUP_FILE="$BACKUP_DIR/$(date +\%Y-\%m-\%d_\%H-\%M-\%S).backup"

pg_dump -U $USER -F c -b -v -f $BACKUP_FILE $DBNAME
***
-восстановление

***bash 
#!/bin/bash

USER="username"
DBNAME="dbname"
BACKUP_FILE="/path/to/backup/file.backup"

pg_restore -U $USER -d $DBNAME -v $BACKUP_FILE
***


### Задание 3
сперва нужно сделать полный бэкап
***bash
mysqlbackup --user=root --password=root_password --host=localhost --backup-dir=/path/to/backup/full --backup-image=full_backup.mbi --compress backup
***
после полного, инкрементальный
***bash
mysqlbackup --user=root --password=root_password --backup-dir=/path/to/incremental_backup --incremental-basedir=/path/to/full_backup backup
***