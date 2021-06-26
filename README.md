# Welcome to Twitter Biotify 👋
![Version](https://img.shields.io/badge/version-1-blue.svg?cacheSeconds=2592000)

> A python bot designed to update your Twitter bio with the current listening track on Spotify

## Dependecies
- [Spotipy](https://github.com/plamere/spotipy)
- [Rauth](https://github.com/litl/rauth)

## Run
1. Create an app on [Spotify for Developpers's Dashboard](https://developer.spotify.com/dashboard/)
2. Install [Spotipy](https://spotipy.readthedocs.io/en/2.18.0/#installation) and [Rauth](https://github.com/litl/rauth#installation)
3. Set the environment variables :
    - SPOTIPY_CLIENT_ID
    - SPOTIPY_CLIENT_SECRET
    - SPOTIPY_REDIRECT_URI
4. Create an app on [Twitter Developer Portal](https://developer.twitter.com/en)
5. Set the environment variables (Twitter Consumer Keys) :
    - TWITTER_API_KEY 
    - TWITTER_API_SECRET
6. Set up 3-legged OAuth and also Read and Write permissions 
7. Run:
```sh
py biotify.py
```

## Author

👤 **Marius ANDRÉ (marius.andre)** 

* Github: [@bobaiep](https://github.com/bobaiep)

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
