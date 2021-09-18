from operator import itemgetter
import requests


def get_popular_hn_articles():
    """A function that retrieves the most popular Hacker News
    articles on the website"""

    # Make an API call and store the response
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)

    # Process information about each submission
    submission_ids = r.json()
    submission_dicts = []
    for submission_id in submission_ids[:30]:
        # Make a separate API call for each submission
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        response_dict = r.json()

        try:
            # Build a dictionary for each article
            submission_dict = {
                'title': response_dict['title'],
                'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
                'comments': response_dict['descendants'],
            }
        except KeyError:
            pass
        else:
            submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                              reverse=True)

    return submission_dicts
