from plotly import offline
from hn_submissions import get_popular_hn_articles

"""
A file that generates a visual of the article with the most 
comments on Hacker News
"""


def hn_comments_visual():
    # Make an API call and store the response
    popular_articles = get_popular_hn_articles()

    # Process Results
    links, comments,full_titles = [], [], []
    for article in popular_articles:
        # Format the String used for the title
        article_title = article['title']
        full_title = article['title']
        split_title = article_title.split()
        split_title = split_title[:3]
        split_title.append('...')
        space = ' '
        article_title = space.join(split_title)

        article_comments = article['comments']
        unformatted_link = article['hn_link']
        formatted_link = f"<a href='{unformatted_link}'>{article_title}</a>"

        full_titles.append(full_title)
        links.append(formatted_link)
        comments.append(article_comments)

    # Make visualization
    data = [{
        'type': 'bar',
        'x': links,
        'y': comments,
        'hovertext': full_titles,
        'marker': {
            'color': 'rgb(60,100,150)',
            'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
        },
        'opacity': 0.6,
    }]
    my_layout = {
        'title': 'Most-Commented Articles on Hacker News',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Comments',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }

    fig = {'data': data, 'layout': my_layout}
    new_file = f"hn_comments_visual.html"
    offline.plot(fig, filename=new_file)


hn_comments_visual()
