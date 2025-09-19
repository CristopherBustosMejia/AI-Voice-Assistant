from db.db import MySqlDatabase

class SakilaCrud:
    def __init__(self, host, user, password, database, pool_size=10):
        self.db = MySqlDatabase(host, user, password, database, pool_size)

    # --- FUNCIONES SEGURAS DE CONSULTA ---
    def get_all_films(self, limit=10):
        query = "SELECT film_id, title, release_year, rating FROM film LIMIT %s"
        return self.db.execute_query(query, (limit,))

    def get_film_by_id(self, film_id):
        query = "SELECT film_id, title, description, release_year, rating FROM film WHERE film_id = %s"
        return self.db.execute_query(query, (film_id,))

    def get_actors_by_film(self, film_id):
        query = """
        SELECT a.actor_id, a.first_name, a.last_name
        FROM actor a
        JOIN film_actor fa ON a.actor_id = fa.actor_id
        WHERE fa.film_id = %s
        """
        return self.db.execute_query(query, (film_id,))

    def search_films_by_keyword(self, keyword, limit=10):
        query = """
        SELECT film_id, title, description
        FROM film
        WHERE title LIKE %s OR description LIKE %s
        LIMIT %s
        """
        param = f"%{keyword}%"
        return self.db.execute_query(query, (param, param, limit))
