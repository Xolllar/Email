import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
name_adresse = "Александр"
name_sender = "Никита"
website = "https://dvmn.org/referrals/vyX6uTFwbt4cGhpG2dbPiJB1HMZ1m3o0cJCpw7vJ/"
Sender = 'voroninnikita412@yandex.ru'
Adresse = 'Xohshg@yandex.ru'
Title= 'Приглашение на курс'
letter = '''From: {1}
To: {2}
Subject: {0}
Content-Type: text/plain; charset="UTF-8";
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(Title, Sender, Adresse)
letter = letter.replace('%website%', website)
letter = letter.replace("%friend_name%", name_adresse) 
letter = letter.replace('%my_name%', name_sender)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
server.login(login, password)
server.sendmail('voroninnikita412@yandex.ru', 'Xohshg@yandex.ru', letter)
server.quit()
print(letter)