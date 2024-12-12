def pytest_addoption(parser):
    parser.addoption(
        '--dog-api-url', 
        action='store', 
        default='https://dog.ceo/api/',
        help='Base URL for Dog API tests'
    )
    parser.addoption(
        '--brewery-api-url', 
        action='store', 
        default='https://api.openbrewerydb.org/v1/',
        help='Base URL for Brewery API tests'
    )
    parser.addoption(
        '--jsonplaceholder-api-url', 
        action='store', 
        default='https://jsonplaceholder.typicode.com/',
        help='Base URL for JSONPlaceholder API tests'
    )

class APIRoutes:
    @staticmethod
    def get_dog_breeds():
        return "https://dog.ceo/api/breeds/list/all"

    @staticmethod
    def get_random_dog_image():
        return "https://dog.ceo/api/breeds/image/random"

    @staticmethod
    def get_dog_images_by_breed(breed):
        return f"https://dog.ceo/api/breed/{breed}/images"

    @staticmethod
    def get_breweries_by_city(city):
        return f"https://api.openbrewerydb.org/v1/breweries?by_city={city}&per_page=3"

    @staticmethod
    def autocomplete_breweries(query):
        return f"https://api.openbrewerydb.org/v1/breweries/autocomplete?query={query}"

    @staticmethod
    def get_random_breweries(size):
        return f"https://api.openbrewerydb.org/v1/breweries/random?size={size}"

    @staticmethod
    def search_breweries(query):
        return f"https://api.openbrewerydb.org/v1/breweries/search?query={query}&per_page=3"

    @staticmethod
    def get_posts_by_user(user_id):
        return f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

    @staticmethod
    def get_posts_by_title(title):
        return f"https://jsonplaceholder.typicode.com/posts?title={title}"

    @staticmethod
    def get_posts_by_body(body):
        return f"https://jsonplaceholder.typicode.com/posts?body={body}"

    @staticmethod
    def get_post_by_id(post_id):
        return f"https://jsonplaceholder.typicode.com/posts/{post_id}"
