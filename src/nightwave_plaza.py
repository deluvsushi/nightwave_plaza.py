import requests

class NightWavePlaza:
	def __init__(self) -> None:
		self.api = "https://api.plaza.one"
		self.headers = {
			"user-agent": "NightwavePlaza/1.4.1 (Android: SM-G9880; samsung z3q; ru)",
			"np-user-agent": "Nightwave Plaza Axios"
		}

	def get_status(self) -> dict:
		return requests.get(
			f"{self.api}/status",
			headers=self.headers).json()

	def get_random_background(self) -> dict:
		return requests.get(
			f"{self.api}/backgrounds/random",
			headers=self.headers).json()

	def get_captcha(self) -> dict:
		return requests.get(
			f"{self.api}/captcha",
			headers=self.headers).json()

	def login(self, username: str, password: str) -> dict:
		data = {
			"username": username,
			"password": password
		}
		response = requests.post(
			f"{self.api}/user/auth",
			data=data,
			headers=self.headers).json()
		if "token" in response:
			self.token = response["token"]
			self.headers["authorization"] = f"Bearer {self.token}"
		return response

	def register(
			self,
			email: str,
			captcha: str,
			username: str,
			password: str,
			captcha_key: str) -> dict:
		data = {
			"captcha": captcha,
			"email": email,
			"key": captcha_key,
			"password": password,
			"username": username
		}
		return requests.post(
			f"{self.api}/user/register",
			data=data,
			headers=self.headers).json()

	def set_reaction(self, reaction: int) -> dict:
		data = {"reaction": reaction}
		return requests.post(
			f"{self.api}/reactions",
			data=data,
			headers=self.headers).json()

	def get_backgrounds_list(self) -> dict:
		return requests.get(
			f"{self.api}/backgrounds",
			headers=self.headers).json()

	def get_play_history(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/history/{page}",
			headers=self.headers).json()

	def get_ratings(self, type: str = "overtime", page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/ratings/{type}/{page}",
			headers=self.headers).json()

	def get_news(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/news/{page}",
			headers=self.headers).json()

	def get_song_favorites(self, page: int = 1) -> dict:
		return requests.get(
			f"{self.api}/user/favorites/{page}",
			headers=self.headers).json()

	def change_password(
			self,
			current_password: str,
			new_password: str) -> dict:
		data = {
			"current_password": current_password,
			"password": new_password
		}
		return requests.put(
			f"{self.api}/user",
			data=data,
			headers=self.headers).json()

	def change_email(self, email: str, password: str) -> dict:
		data = {
			"current_password": password,
			"email": email
		}
		return requests.put(
			f"{self.api}/user",
			data=data,
			headers=self.headers).json()

	def reset_password(
			self,
			email: str,
			captcha: str,
			captcha_key: str) -> dict:
		data = {
			"captcha": captcha,
			"email": email,
			"key": captcha_key
		}
		return requests.post(
			f"{self.api}/user/reset",
			data=data,
			headers=self.headers).json()

	def get_song_info(self, song_id: str) -> dict:
		return requests.get(
			f"{self.api}/songs/{song_id}",
			headers=self.headers).json()

	def get_account_info(self) -> dict:
		return requests.get(
			f"{self.api}/user",
			headers=self.headers).json()

	def add_song_to_favorites(self, song_id: str) -> dict:
		data = {"song_id": song_id}
		return requests.post(
			f"{self.api}/user/favorites",
			data=data,
			headers=self.headers).json()
	
	def get_on_screen_data(self) -> dict:
		return requests.get(
			f"{self.api}/status/on-screen-data",
			headers=self.headers).json()
	
	def get_background_info(self, background_id: str) -> dict:
		return requests.get(
			f"{self.api}/backgrounds/{background_id}",
			headers=self.headers).json()
