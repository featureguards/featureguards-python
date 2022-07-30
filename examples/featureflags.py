from os import getenv

from featureguards.feature_flags import feature_flags


def example() -> None:
    try:
        fg = feature_flags(api_key=getenv('FEATUREGUARDS_API_KEY'))
        print(fg.is_on('FOO'))
        print(fg.is_on('FOO', {'user_id': 123}))
    finally:
        if fg:
            fg.stop()


if __name__ == '__main__':
    example()
