import os
import json
import argparse
import tweepy

bearer_token = os.environ.get("BEARER_TOKEN")


def connect_to_endpoint(query, limit):
    result = []
    client = tweepy.Client(bearer_token)
    for tweet in tweepy.Paginator(client.search_recent_tweets, query,
                                  max_results=100).flatten(limit=limit):
        result.append(tweet.data)
    return result


def main(query, limit):
    json_response = connect_to_endpoint(query, limit)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    print(len(json_response), "results retrieved")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Search recent tweets from the Twitter v2 API')
    parser.add_argument('query', help='query string for the Search Tweets API')
    parser.add_argument('--limit', type=int, default=100,
                        help='maximum number of results to retrieve')
    args = parser.parse_args()

    print('query:', args.query)
    main(args.query, args.limit)
