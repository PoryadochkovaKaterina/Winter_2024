# -- количество книг по авторам
# CREATE VIEW min_amount AS
# SELECT author_name AS Автор, SUM(amount) AS sum_amount
# FROM book INNER JOIN author
# ON book.author_id = author.author_id
# GROUP BY author_name
#
# -- минимальное количество книг
# CREATE VIEW min_sum_amount AS
# SELECT MIN(sum_amount) AS min_sum_amount
# FROM
# 	(
# 	SELECT * FROM min_amount
# 	) query_in
#
# -- Всех авторы с минимальным количеством книг
# SELECT author_name AS Автор, SUM(amount) AS sum_amount
# FROM book INNER JOIN author
# ON book.author_id = author.author_id
# GROUP BY author_name
# HAVING SUM(amount) =
# 	(
# 	SELECT * FROM min_sum_amount
# 	)