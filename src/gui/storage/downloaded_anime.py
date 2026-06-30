import atexit
import os

from pydantic import BaseModel


class DownloadedAnime(BaseModel):
    anime_url: str
    image: str
    title: str
    lang: str
    season: str
    episode: int


class DownloadedAnimes(BaseModel):
    downloaded_episodes: dict[str, DownloadedAnime]

    def add_new_episode(self, downloaded_episode: DownloadedAnime):
        episode_key = self.construct_anime_key(
            downloaded_episode.title,
            downloaded_episode.season,
            downloaded_episode.lang,
            downloaded_episode.episode
        )
        self.downloaded_episodes[episode_key] = downloaded_episode

    def has_been_downloaded(self, title: str, season: str, lang: str, episode: int) -> bool:
        episode_key = self.construct_anime_key(title, season, lang, episode)
        return episode_key in self.downloaded_episodes
    
    @staticmethod
    def construct_anime_key(title: str, season: str, lang: str, episode: int) -> str:
        return f"{title}-{season}-{lang}-{episode}"

    def save(self):
        os.makedirs("config", exist_ok=True)
        with open(animes_path, "w", encoding="utf-8") as f:
            f.write(self.model_dump_json(indent=2))


def _load_downloaded_animes(path: str) -> DownloadedAnimes:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return DownloadedAnimes.model_validate_json(f.read())
    except FileNotFoundError:
        return DownloadedAnimes(
            downloaded_episodes={}
        )


animes_path = "config/downloaded_anime.json"
downloaded_animes: DownloadedAnimes = _load_downloaded_animes(animes_path)

atexit.register(downloaded_animes.save)
