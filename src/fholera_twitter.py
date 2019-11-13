"""Main module."""

import itertools
import os
import pickle
from typing import NamedTuple

import tweepy

consumer_key_env_name = "FHOLERA_TWITTER_APP_CONSUMER_KEY"
consumer_secret_env_name = "FHOLERA_TWITTER_APP_CONSUMER_SECRET"


class UserToken(NamedTuple):
    """
    Keep the user public key and secret linked together
    """

    key: str
    secret: str


def make_api(
    app_consumer_key: str, app_consumer_secret: str, pickled_user_token_path: str
) -> tweepy.API:
    """

    :param app_consumer_key:
    :param app_consumer_secret:
    :param pickled_user_token_path:
    :return:
    """

    auth = tweepy.OAuthHandler(app_consumer_key, app_consumer_secret)

    if os.path.exists(pickled_user_token_path):
        with open(pickled_user_token_path, "rb") as f:
            user_token = pickle.load(f)
    else:
        print(
            f"Click this link while signed into the account you "
            f"would like to do the following on {auth.get_authorization_url()}"
        )
        verifier = input("Paste the access code and press enter:")
        auth.get_access_token(verifier)
        user_token = UserToken(key=auth.access_token, secret=auth.access_token_secret)

    auth.set_access_token(user_token.key, user_token.secret)

    # save the token to the key file for next time
    with open(pickled_user_token_path, "wb") as f:
        pickle.dump(user_token, f)

    return tweepy.API(
        auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True
    )


def main() -> None:
    """
    Main entry point for fholera_twitter
    :return: None
    """

    api = make_api(
        app_consumer_key=os.environ[consumer_key_env_name],
        app_consumer_secret=os.environ[consumer_secret_env_name],
        pickled_user_token_path="./key.p",
    )

    # handles = ["spizzyspose", "bensbeendead"]
    handles = ["bensbeendead"]

    user_ids = list(
        itertools.chain.from_iterable(
            [
                itertools.chain.from_iterable(
                    [
                        followers_on_page
                        for followers_on_page in tweepy.Cursor(
                            api.followers_ids, screen_name=handle
                        ).pages()
                    ]
                )
                for handle in handles
            ]
        )
    )

    num_ids = len(user_ids)
    for index, account_id in enumerate(user_ids):
        print(f"Following ({index}/{num_ids}) account id: {account_id}")
        api.create_friendship(user_id=account_id)


if __name__ == "__main__":
    main()
